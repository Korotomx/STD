#!/usr/bin/env python3
"""检查各科 Ref/Capture 原始材料是否已有对应笔记，以及笔记是否过期。

用法：
    python3 Scripts/check_updates.py          # 人读格式
    python3 Scripts/check_updates.py --json   # 机器读格式

输出为空表示全部已处理且同步。判定（mtime 容差 5 分钟，避免拷贝时间戳误报）：
    NEW        原始材料没有被任何笔记或索引引用
    CATALOGED  只登记在 Ref/Ref.md 索引里，还没有笔记正文引用
    STALE      引用了它的笔记比原始材料旧
    UNINDEXED  笔记没有被该科索引（STDY.md / Overview.md）链接
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path("/mnt/c/X/STD/STD")
MTIME_TOLERANCE = 300  # 秒

SKIP_NAMES = {
    "Ref.md", "Overview.md", "STDY.md", "Errors.md", "Problems.md",
    "README.md", "Concentrated.md",
}
SKIP_DIRS = {"assets", "attachments", "__pycache__", ".obsidian", ".git"}

LINK_RE = re.compile(r"!?\[\[([^\]|#]+)")

TARGETS = [
    {
        "name": "Sight",
        "raw_roots": [ROOT / "Raw"],
        "note_roots": [ROOT / "Sight"],
        "index_files": [ROOT / "Sight" / "Overview.md"],
    },
    {
        "name": "ALGO",
        "raw_roots": [ROOT / "Artificial_Intelligence" / "ALGO" / "Ref"],
        "note_roots": [ROOT / "Artificial_Intelligence" / "ALGO" / "STDY"],
        "index_files": [ROOT / "Artificial_Intelligence" / "ALGO" / "STDY" / "STDY.md"],
    },
    {
        "name": "Unlimited",
        "raw_roots": [ROOT / "Artificial_Intelligence" / "Unlimited" / "Capture"],
        "note_roots": [ROOT / "Artificial_Intelligence" / "Unlimited"],
        "index_files": [ROOT / "Artificial_Intelligence" / "Unlimited" / "Overview.md"],
        "notes_flat": True,
    },
    {
        "name": "Math",
        "raw_roots": [ROOT / "Math"],
        "note_roots": [ROOT / "Math"],
        "raw_only_in": {"Ref"},
        "notes_under": {"STDY"},
        "index_globs": ["Math/Overview.md", "Math/*/Overview.md",
                        "Math/*/STDY/STDY.md", "Math/*/Ref/Ref.md"],
    },
    {
        "name": "Writing",
        "raw_roots": [ROOT / "Writing" / "Ref"],
        "note_roots": [ROOT / "Writing" / "STDY"],
        "index_files": [ROOT / "Writing" / "Overview.md"],
    },
]


def should_skip(path: Path) -> bool:
    if path.name in SKIP_NAMES:
        return True
    return any(part in SKIP_DIRS for part in path.parts)


def collect_raw(target: dict) -> list[Path]:
    files: list[Path] = []
    for root in target["raw_roots"]:
        if not root.exists():
            continue
        for p in root.rglob("*.md"):
            if should_skip(p):
                continue
            if target.get("raw_only_in") and not (set(p.parts) & target["raw_only_in"]):
                continue
            files.append(p)
    return sorted(files)


def collect_notes(target: dict) -> list[Path]:
    files: list[Path] = []
    for root in target["note_roots"]:
        if not root.exists():
            continue
        if target["name"] == "Math":
            for sub in root.iterdir():
                if not sub.is_dir():
                    continue
                for p in sub.glob("*.md"):
                    if not should_skip(p):
                        files.append(p)
                stdy = sub / "STDY"
                if stdy.exists():
                    for p in stdy.rglob("*.md"):
                        if not should_skip(p):
                            files.append(p)
        elif target.get("notes_flat"):
            for p in root.glob("*.md"):
                if not should_skip(p):
                    files.append(p)
        else:
            for p in root.rglob("*.md"):
                if not should_skip(p):
                    files.append(p)
    return sorted(set(files))


def index_files(target: dict) -> list[Path]:
    if "index_files" in target:
        return [p for p in target["index_files"] if p.exists()]
    files = []
    for pattern in target.get("index_globs", []):
        files.extend(ROOT.glob(pattern))
    return sorted(set(files))


def link_keys(raw: Path) -> set[str]:
    rel = raw.relative_to(ROOT).with_suffix("").as_posix()
    return {rel, raw.stem, f"{rel}.md", raw.name}


def links_in(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return set()
    return {m.group(1).strip() for m in LINK_RE.finditer(text)}


PROCESSED_HINTS = ("已整理", "已并入", "已用于", "已提炼", "已作为", "已补",
                   "暂不", "复习课", "并入", "提炼", "用于")
PENDING_HINTS = ("尚未成篇", "未成篇", "待整理", "待写", "待补")


def processed_index_links() -> set[str]:
    """索引里已登记的原始材料链接。

    Ref.md 是原始材料的权威登记表，列进去就算已处理；Overview 里写明
    `已整理为 [[笔记]]` 或同一行有两个链接的也算。
    """
    processed: set[str] = set()
    for ref in ROOT.glob("Math/*/Ref/Ref.md"):
        for line in ref.read_text(encoding="utf-8", errors="ignore").splitlines():
            links = [m.group(1).strip() for m in LINK_RE.finditer(line)]
            if not links:
                continue
            if any(h in line for h in PENDING_HINTS):
                continue
            if (len(links) >= 2 or any(h in line for h in PROCESSED_HINTS)
                    or re.search(r"\bL\d+\b", line)):
                processed.update(links)
    for path in ROOT.glob("Math/*/Overview.md"):
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            links = [m.group(1).strip() for m in LINK_RE.finditer(line)]
            if not links:
                continue
            if len(links) >= 2 or any(h in line for h in PROCESSED_HINTS):
                processed.update(links)
    return processed


def check() -> list[dict]:
    findings: list[dict] = []
    processed_index = processed_index_links()
    for target in TARGETS:
        raws = collect_raw(target)
        notes = collect_notes(target)
        note_links = {n: links_in(n) for n in notes}
        idxs = index_files(target)
        idx_links = {i: links_in(i) for i in idxs}
        idx_text = "\n".join(i.read_text(encoding="utf-8", errors="ignore") for i in idxs)

        for raw in raws:
            keys = link_keys(raw)
            matched = [n for n, ls in note_links.items() if keys & ls]
            # 索引里已经写明去向的，算已处理
            if any(key in processed_index for key in keys):
                continue
            cataloged = any(keys & ls for ls in idx_links.values())
            if not matched:
                status = "CATALOGED" if cataloged else "NEW"
                findings.append({
                    "subject": target["name"], "status": status,
                    "raw": raw.relative_to(ROOT).as_posix(), "note": None,
                })
            elif max(n.stat().st_mtime for n in matched) + MTIME_TOLERANCE < raw.stat().st_mtime:
                findings.append({
                    "subject": target["name"], "status": "STALE",
                    "raw": raw.relative_to(ROOT).as_posix(),
                    "note": matched[0].relative_to(ROOT).as_posix(),
                })

        if idxs:
            for note in notes:
                if note in idxs:
                    continue
                if f"[[{note.stem}]]" not in idx_text and note.stem not in idx_text:
                    findings.append({
                        "subject": target["name"], "status": "UNINDEXED",
                        "raw": None, "note": note.relative_to(ROOT).as_posix(),
                    })
    return findings


def main() -> int:
    findings = check()
    if "--json" in sys.argv:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        return 0
    if not findings:
        return 0
    for f in findings:
        subject, status = f["subject"], f["status"]
        if status == "NEW":
            print(f"{status}\t{subject}\t{f['raw']}\t没有笔记引用")
        elif status == "CATALOGED":
            print(f"{status}\t{subject}\t{f['raw']}\t只在索引中登记")
        elif status == "STALE":
            print(f"{status}\t{subject}\t{f['raw']}\t笔记较旧：{f['note']}")
        else:
            print(f"{status}\t{subject}\t{f['note']}\t索引未链接")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
