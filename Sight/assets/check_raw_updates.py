#!/usr/bin/env python3
"""List Raw files that are new or newer than their Sight note.

Usage: python3 check_raw_updates.py
Prints nothing when every Raw file has an up-to-date Sight note.
"""
from pathlib import Path

ROOT = Path("/mnt/c/X/STD/STD")
RAW = ROOT / "Raw"
SIGHT = ROOT / "Sight"

notes = {p: p.read_text(encoding="utf-8") for p in SIGHT.glob("*.md")}

for raw in sorted(RAW.rglob("*.md")):
    rel = raw.relative_to(ROOT).with_suffix("").as_posix()
    key = f"[[{rel}]]"
    matches = [p for p, text in notes.items() if key in text]
    if not matches:
        print(f"NEW\t{raw.relative_to(ROOT)}\tno note")
    elif max(p.stat().st_mtime for p in matches) < raw.stat().st_mtime:
        print(f"STALE\t{raw.relative_to(ROOT)}\t{matches[0].name}")
