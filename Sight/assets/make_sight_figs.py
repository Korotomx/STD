"""Teaching figures for the Sight note on the Smith Chart.

Usage:  python make_sight_figs.py
Output: PNG files next to this script.

Conventions
-----------
- Agg backend, dpi=200, English-only text.
- Fixed palette: RED / BLUE / GREEN / ORANGE / PURPLE / GRAY.
- clean(ax): light grid, no top/right spines.
- One figure = one concept; embedded as ![[name.png]] + italic caption.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

OUT = "/mnt/c/X/STD/STD/Sight/assets"
RED, BLUE, GREEN, ORANGE, PURPLE, GRAY = (
    "#d62728", "#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", "#7f7f7f")


def clean(ax, equal=True):
    ax.grid(alpha=0.22)
    if equal:
        ax.set_aspect("equal", adjustable="box")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def gamma_of(z):
    return (z - 1) / (z + 1)


def smith_background(ax, r_values=(0, 0.2, 0.5, 1, 2, 5),
                     x_values=(0.2, 0.5, 1, 2, 5), lw=0.75):
    """Draw the constant-r and constant-x families inside the unit circle."""
    for r in r_values:
        c = Circle((r / (1 + r), 0), 1 / (1 + r), fill=False,
                   color=GRAY, lw=lw, alpha=0.65)
        ax.add_patch(c)
    clip = Circle((0, 0), 1, transform=ax.transData)
    for x in x_values:
        for s in (1, -1):
            c = Circle((1, s / x), 1 / x, fill=False,
                       color=GRAY, lw=lw, alpha=0.65)
            ax.add_patch(c)
            c.set_clip_path(clip)
    ax.plot([-1, 1], [0, 0], color="black", lw=1.0)
    ax.add_patch(Circle((0, 0), 1, fill=False, color="black", lw=1.4))
    ax.set_xlim(-1.08, 1.08)
    ax.set_ylim(-1.08, 1.08)
    ax.set_xticks([])
    ax.set_yticks([])


# ---------------------------------------------------------------- S1
def fig_reflection():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 4.8))

    # (a) transmission-line schematic
    ax = axes[0]
    ax.plot([0, 7], [0.55, 0.55], color="black", lw=2)
    ax.plot([0, 7], [-0.55, -0.55], color="black", lw=2)
    ax.plot([0, 0], [-0.55, 0.55], color="black", lw=2)
    ax.add_patch(Circle((0, 0), 0.42, fill=False, color=BLUE, lw=2))
    ax.text(0, -1.0, "source", ha="center", fontsize=11, color=BLUE)
    # antenna at the far end
    ax.plot([7, 7], [-0.55, 0.55], color="black", lw=2)
    ax.plot([7, 7.55], [-0.55, 0.55], color=RED, lw=2)
    ax.plot([7, 7.55], [0.55, -0.55], color=RED, lw=2)
    ax.text(7.35, -1.0, "load $Z_L$", ha="center", fontsize=11, color=RED)
    # forward and reflected arrows
    ax.add_patch(FancyArrowPatch((1.0, 0.9), (4.2, 0.9), arrowstyle="-|>",
                                 mutation_scale=18, color=GREEN, lw=2.4))
    ax.text(2.6, 1.12, "forward wave", color=GREEN, fontsize=11, ha="center")
    ax.add_patch(FancyArrowPatch((5.9, -0.9), (2.7, -0.9), arrowstyle="-|>",
                                 mutation_scale=18, color=ORANGE, lw=2.4))
    ax.text(4.3, -1.25, "reflected wave", color=ORANGE, fontsize=11, ha="center")
    ax.text(3.5, -0.25, "$Z_0$", fontsize=12, ha="center")
    ax.text(3.5, 1.5, r"$\Gamma=\dfrac{Z_L-Z_0}{Z_L+Z_0}$",
            fontsize=14, ha="center")
    ax.text(3.5, -1.85, "mismatch at the boundary sends power back",
            fontsize=10.5, ha="center", color=GRAY)
    ax.set_xlim(-0.8, 8.1)
    ax.set_ylim(-2.1, 2.0)
    ax.axis("off")
    ax.set_title("(a) A wave on a transmission line", fontsize=13)

    # (b) standing-wave envelope
    ax = axes[1]
    d = np.linspace(0, 2, 600)
    for g, color, label in ((0.0, BLUE, r"matched ($\Gamma=0$)"),
                            (0.5, GREEN, r"partial mismatch ($|\Gamma|=0.5$)"),
                            (1.0, RED, r"open / short ($|\Gamma|=1$)")):
        ax.plot(d, np.abs(1 + g * np.exp(-2j * np.pi * d)), color=color,
                lw=2.2, label=label)
    ax.axhline(2.0, color=GRAY, ls=":", lw=1.2)
    ax.text(1.55, 2.06, "peak = $2|V^+|$", color=GRAY, fontsize=10)
    ax.set_xlabel("distance from load (wavelengths)")
    ax.set_ylabel(r"$|V|\,/\,|V^+|$")
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2.25)
    ax.set_title("(b) Standing wave: reflection can double the voltage",
                 fontsize=13)
    ax.legend(frameon=False, fontsize=9.5, loc="lower right")
    clean(ax, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S1_reflection_standing_wave.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- S2
def fig_phase():
    fig, axes = plt.subplots(1, 3, figsize=(13.4, 3.9), sharey=True)
    t = np.linspace(0, 2 * np.pi, 500)
    cases = [
        (np.sin(t), np.sin(t), "Resistor: V and I in phase", BLUE, RED),
        (np.sin(t), np.sin(t + np.pi / 2),
         "Capacitor: I leads V by $90^\\circ$", BLUE, RED),
        (np.sin(t + np.pi / 2), np.sin(t),
         "Inductor: V leads I by $90^\\circ$", BLUE, RED),
    ]
    for ax, (v, i, title, cv, ci) in zip(axes, cases):
        ax.plot(t, v, color=cv, lw=2.2, label="V")
        ax.plot(t, i, color=ci, lw=2.2, ls="--", label="I")
        ax.axhline(0, color="black", lw=0.7)
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.55, 1.55)
        ax.set_xticks([0, np.pi, 2 * np.pi])
        ax.set_xticklabels(["0", r"$\pi$", r"$2\pi$"])
        ax.set_title(title, fontsize=11.5)
        ax.set_xlabel("time")
        ax.legend(frameon=False, fontsize=9.5, loc="upper right")
        clean(ax, equal=False)
    axes[0].set_ylabel("amplitude")
    fig.tight_layout()
    fig.savefig(f"{OUT}/S2_phase_relation.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_complex_impedance():
    fig, ax = plt.subplots(figsize=(7.6, 6.2))
    ax.axhline(0, color="black", lw=0.9)
    ax.axvline(0, color="black", lw=0.9)
    # example Z = 10 - j30
    ax.add_patch(FancyArrowPatch((0, 0), (10, 0), arrowstyle="-|>",
                                 mutation_scale=16, color=BLUE, lw=2.2))
    ax.add_patch(FancyArrowPatch((10, 0), (10, -30), arrowstyle="-|>",
                                 mutation_scale=16, color=RED, lw=2.2))
    ax.add_patch(FancyArrowPatch((0, -30), (10, -30), arrowstyle="-|>",
                                 mutation_scale=16, color=BLUE, lw=1.4,
                                 ls="--"))
    ax.add_patch(FancyArrowPatch((0, 0), (10, -30), arrowstyle="-|>",
                                 mutation_scale=19, color=PURPLE, lw=2.8))
    # cancel the reactance (curved so it does not hide the -jX arrow)
    ax.add_patch(FancyArrowPatch((10, -30), (10, 0), arrowstyle="-|>",
                                 mutation_scale=16, color=ORANGE, lw=2.2,
                                 connectionstyle="arc3,rad=-0.35"))
    ax.text(14.0, -20, "add series\n$+j30$", color=ORANGE, fontsize=10.5)
    ax.text(2.0, 3.0, "$R=10\\,\\Omega$", color=BLUE, fontsize=11)
    ax.text(11.5, -30.8, "$-jX=-j30$", color=RED, fontsize=11)
    ax.text(2.0, -26, "$Z=10-j30$", color=PURPLE, fontsize=11.5)
    # target 50 ohm
    ax.axvline(50, color=GRAY, ls=":", lw=1.4)
    ax.text(50.7, 27, "$Z_0=50\\,\\Omega$", color=GRAY, fontsize=11,
            rotation=90, va="top")
    ax.annotate("", xy=(50, -8), xytext=(10, -8),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.3))
    ax.text(30, -13.5, "still need 40 $\\Omega$\n(a resistor only burns power)",
            color=GRAY, fontsize=9.8, ha="center")
    ax.set_xlim(-6, 62)
    ax.set_ylim(-42, 34)
    ax.set_xlabel("real part  $R$  (resistance)")
    ax.set_ylabel("imaginary part  $X$  (reactance)")
    ax.set_title(r"Impedance $Z=R+jX$: magnitude and phase in one complex number",
                 fontsize=12.5)
    clean(ax, equal=False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S3_complex_impedance.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- S4
def fig_smith_construction():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.8))

    # (a) impedance plane (right half only)
    ax = axes[0]
    ax.axhline(0, color="black", lw=0.9)
    ax.axvline(0, color="black", lw=0.9)
    rs = [0, 0.5, 1, 2, 5]
    xs = [-5, -2, -1, -0.5, 0, 0.5, 1, 2, 5]
    for r in rs:
        ax.plot([r, r], [-6.2, 6.2], color=GRAY, lw=0.8, alpha=0.7)
        ylab = 6.55 if r in (0, 1, 5) else 5.95
        ax.text(r, ylab, f"$r={r}$", ha="center", fontsize=8.5, color=GRAY)
    for x in xs:
        ax.plot([0, 6.2], [x, x], color=GRAY, lw=0.8, alpha=0.55)
        ax.text(6.35, x, f"$x={x}$", va="center", fontsize=8.5, color=GRAY)
    ax.scatter([0], [0], color=RED, s=55, zorder=5)
    ax.text(0.15, -0.7, "short", color=RED, fontsize=10)
    ax.annotate("open  $r\\to\\infty$", xy=(6.0, 0), xytext=(4.0, 2.7),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.5),
                color=ORANGE, fontsize=10.5)
    ax.set_xlim(-0.4, 7.2)
    ax.set_ylim(-6.8, 7.2)
    ax.set_xlabel("$r=R/Z_0$")
    ax.set_ylabel("$x=X/Z_0$")
    ax.set_title("(a) Normalized impedance plane: $0 \\leq r < \\infty$",
                 fontsize=12.5)
    clean(ax, equal=False)

    # (b) reflection-coefficient plane
    ax = axes[1]
    smith_background(ax)
    ax.scatter([0], [0], color=BLUE, s=55, zorder=6)
    ax.text(0.03, 0.07, "match\n$\\Gamma=0$", color=BLUE, fontsize=9.5)
    ax.scatter([-1], [0], color=RED, s=45, zorder=6)
    ax.text(-0.96, -0.13, "short", color=RED, fontsize=9.5)
    ax.scatter([1], [0], color=ORANGE, s=45, zorder=6)
    ax.text(0.66, -0.16, "open", color=ORANGE, fontsize=9.5)
    ax.text(0.0, -1.22, "entire right half-plane packed into the unit disk",
            ha="center", fontsize=10, color=GRAY)
    ax.set_title(r"(b) Reflection plane: $\Gamma=(z-1)/(z+1)$", fontsize=12.5)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S4_smith_construction.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- S5
def fig_smith_reading():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 6.0))

    z0 = 0.7 + 1.5j
    g0 = gamma_of(z0)
    R = abs(g0)

    # (a) locate the impedance and rotate to r = 1
    ax = axes[0]
    smith_background(ax)
    ax.add_patch(Circle((0, 0), R, fill=False, color=BLUE, lw=1.5, ls="--"))
    ax.plot([0, g0.real], [0, g0.imag], color=BLUE, lw=1.3)
    ax.scatter([g0.real], [g0.imag], color=BLUE, s=60, zorder=7)
    ax.text(-0.55, 0.55,
            f"$z=0.7+1.5j$\n$|\\Gamma|={R:.2f}$", color=BLUE, fontsize=9.5,
            ha="center")
    # both intersections with the r = 1 circle
    u = R ** 2
    v = R * np.sqrt(1 - R ** 2)
    for s, color in ((1, GREEN), (-1, ORANGE)):
        ax.scatter([u], [s * v], color=color, s=55, zorder=7)
    # arcs along the constant-|Gamma| circle
    th0 = np.angle(g0)
    th_up = np.angle(u + 1j * v)
    th_dn = np.angle(u - 1j * v)
    a1 = np.linspace(th0, th_up, 80)
    ax.plot(R * np.cos(a1), R * np.sin(a1), color=GREEN, lw=2.2)
    a2 = np.linspace(th0, th_dn, 140)
    ax.plot(R * np.cos(a2), R * np.sin(a2), color=ORANGE, lw=2.2)
    ax.annotate("first $r=1$ spot\n$12^\\circ$ = 3.1 mm",
                xy=(u, v), xytext=(-0.55, 0.90),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2),
                color=GREEN, fontsize=8.8, ha="center")
    ax.annotate("next spot\n$107^\\circ$ = 28 mm",
                xy=(u, -v), xytext=(-0.55, -0.82),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2),
                color=ORANGE, fontsize=8.8, ha="center")
    ax.set_title("(a) Find $z$, then rotate to the $r=1$ circle",
                 fontsize=12.5)

    # (b) cancel the remaining reactance
    ax = axes[1]
    smith_background(ax)
    z1 = 1 - 1.8j
    g1 = gamma_of(z1)
    ax.scatter([g1.real], [g1.imag], color=ORANGE, s=60, zorder=7)
    ax.text(g1.real + 0.04, g1.imag - 0.08,
            "$z=1-1.8j$", color=ORANGE, fontsize=9.5)
    # constant-r = 1 circle path from z1 up to the center (1, 0)
    # the r = 1 circle: center (0.5, 0), radius 0.5
    th_start = np.angle(g1 - 0.5)
    th_end = -np.pi  # center point (0,0) sits at angle -pi on this circle
    th = np.linspace(th_start, th_end, 160)
    cx, cy = 0.5 + 0.5 * np.cos(th), 0.5 * np.sin(th)
    ax.plot(cx, cy, color=ORANGE, lw=2.4)
    ax.annotate("add series $+j1.8$\n$L\\approx13.2$ nH",
                xy=(0.06, 0.05), xytext=(-0.72, 0.62),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.3),
                color=ORANGE, fontsize=9.2, ha="center")
    ax.scatter([0], [0], color=BLUE, s=55, zorder=7)
    ax.text(0.05, -0.12, "match", color=BLUE, fontsize=9.5)
    ax.set_title("(b) Series reactance walks along $r=1$ to the center",
                 fontsize=12.5)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S5_smith_reading.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- S6
def fig_stub():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.4))

    # (a) coax with an open stub
    ax = axes[0]
    ax.plot([0, 7], [0.25, 0.25], color="black", lw=2)
    ax.plot([0, 7], [-0.25, -0.25], color="black", lw=2)
    ax.plot([0, 0], [-0.25, 0.25], color="black", lw=2)
    ax.plot([7, 7.45], [-0.25, 0.25], color=RED, lw=2)
    ax.plot([7, 7.45], [0.25, -0.25], color=RED, lw=2)
    ax.text(7.22, -0.55, "load", color=RED, fontsize=10, ha="center")
    ax.plot([4, 4], [0.25, 2.5], color=BLUE, lw=2)
    ax.plot([4.12, 4.12], [0.25, 2.5], color=BLUE, lw=2)
    ax.plot([4, 4.12], [2.5, 2.5], color="white", lw=3)
    ax.add_patch(FancyArrowPatch((4.06, 2.75), (4.06, 2.2),
                                 arrowstyle="<->", color=GRAY, lw=1.2))
    ax.text(4.22, 2.45, "length $l$", color=GRAY, fontsize=10)
    ax.text(4.06, 2.85, "open end", color=BLUE, fontsize=10, ha="center")
    ax.text(3.95, 1.3, "stub", color=BLUE, fontsize=10.5,
            rotation=90, va="center", ha="right")
    ax.text(2.0, 0.55, "main line", fontsize=10, color=GRAY)
    ax.set_xlim(-0.5, 8.0)
    ax.set_ylim(-1.0, 3.2)
    ax.axis("off")
    ax.set_title("(a) A dangling open stub is still part of the circuit",
                 fontsize=12)

    # (b) outer-circle path on the Smith chart
    ax = axes[1]
    smith_background(ax)
    ax.scatter([1], [0], color=ORANGE, s=55, zorder=7)
    ax.text(0.72, 0.12, "open", color=ORANGE, fontsize=10)
    zst = 1.8j
    gst = gamma_of(zst)
    ax.scatter([gst.real], [gst.imag], color=GREEN, s=55, zorder=7)
    ax.text(gst.real - 0.04, gst.imag + 0.09, "$z=j1.8$",
            color=GREEN, fontsize=10, ha="right")
    th = np.linspace(0, np.angle(gst) - 2 * np.pi, 300)
    ax.plot(np.cos(th), np.sin(th), color=RED, lw=2.4)
    ax.add_patch(FancyArrowPatch(
        (np.cos(th[-7]), np.sin(th[-7])), (np.cos(th[-1]), np.sin(th[-1])),
        arrowstyle="-|>", mutation_scale=18, color=RED, lw=2.4))
    ax.annotate("rotate clockwise\n$302^\\circ$ = 77 mm",
                xy=(-0.25, -0.86), xytext=(-0.72, -1.02),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2),
                color=RED, fontsize=9.2, ha="center")
    ax.text(0.0, -1.24, "one more full lap adds 92 mm and reaches the same point",
            ha="center", fontsize=9.3, color=GRAY)
    ax.set_title("(b) Stub length moves the input reactance around the rim",
                 fontsize=12)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S6_stub_matching.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_reflection()
    fig_phase()
    fig_complex_impedance()
    fig_smith_construction()
    fig_smith_reading()
    fig_stub()
    print("done")
