"""Quantization figure for the Unlimited note.

Usage:  python make_quant_fig.py
Output: quantization_memory.png in this folder.

Conventions: Agg backend, English-only labels, fixed palette, dpi=200.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/mnt/c/X/STD/STD/Artificial_Intelligence/Unlimited/assets"
RED, BLUE, GREEN, ORANGE, PURPLE, GRAY = (
    "#d62728", "#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", "#7f7f7f")


def clean(ax, equal=False):
    ax.grid(alpha=0.22)
    if equal:
        ax.set_aspect("equal", adjustable="box")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(12.8, 4.9), gridspec_kw={"width_ratios": [1.0, 1.35]})

# (a) memory of a 70B model
labels = ["FP16/BF16", "FP8", "INT8", "INT4"]
gb = [140, 70, 70, 35]
colors = [GRAY, BLUE, GREEN, ORANGE]
bars = ax1.bar(labels, gb, color=colors, width=0.60)
for b, v in zip(bars, gb):
    ax1.text(b.get_x() + b.get_width() / 2, v + 4, f"{v} GB",
             ha="center", fontsize=11)
ax1.axhline(8, color=RED, ls="--", lw=1.4)
ax1.text(3.38, 12, "8 GB consumer GPU", color=RED, ha="right", fontsize=9.5)
ax1.set_ylabel("weight memory (GB)")
ax1.set_ylim(0, 160)
ax1.set_title("70B parameters: memory scales with bits", fontsize=12.5)
clean(ax1)

# (b) layer-wise mapping: range 0-100 -> 11 levels
ax2.plot([0, 100], [1.0, 1.0], color=BLUE, lw=3.0)
for v in range(0, 101, 20):
    ax2.plot([v, v], [0.92, 1.08], color=BLUE, lw=1.2)
    ax2.text(v, 1.18, str(v), ha="center", fontsize=9.5, color=BLUE)
ax2.plot([0, 100], [-1.0, -1.0], color=GREEN, lw=3.0)
for v in range(0, 101, 10):
    ax2.plot([v, v], [-1.08, -0.92], color=GREEN, lw=1.2)
    ax2.text(v, -1.30, str(v), ha="center", fontsize=8.5, color=GREEN)
ax2.scatter([53], [1.0], color=RED, s=70, zorder=5)
ax2.text(53, 1.36, "53", color=RED, ha="center", fontsize=11)
ax2.scatter([50], [-1.0], color=ORANGE, s=70, zorder=5)
ax2.text(50, -1.55, "50", color=ORANGE, ha="center", fontsize=11)
ax2.annotate("", xy=(50, -0.88), xytext=(53, 0.88),
             arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.6))
ax2.text(67, 0.08, "$\\div 10$, then round", color=GRAY, fontsize=10.5)
ax2.text(0, 1.55, "original values: 0 to 100", color=BLUE, fontsize=10.5)
ax2.text(0, -1.92, "stored levels: 0, 10, ..., 100 (simplified; INT4 has 16 levels)",
         color=GREEN, fontsize=9.5)
ax2.set_xlim(-8, 108)
ax2.set_ylim(-2.15, 1.80)
ax2.axis("off")
ax2.set_title("Layer-wise mapping: keep the nearest level", fontsize=12.5)

fig.tight_layout()
fig.savefig(f"{OUT}/quantization_memory.png", dpi=200, bbox_inches="tight")
plt.close(fig)
print("ok")
