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
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch

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


# ---------------------------------------------------------------- CNN
def _grid(ax, data, cmap="Blues", vmin=0.0, vmax=2.0, color="black",
          fmt="{:.1f}"):
    data = np.asarray(data, dtype=float)
    ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            v = data[i, j]
            txt = "" if np.isnan(v) else fmt.format(v)
            ax.text(j, i, txt, ha="center", va="center",
                    fontsize=10, color=color)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def fig_convolution():
    rng = np.random.default_rng(7)
    x = np.round(rng.uniform(0, 2, (5, 5)), 1)
    k = np.array([[0.5, -0.3, 0.8],
                  [0.2, 1.0, -0.4],
                  [-0.6, 0.7, 0.3]])
    win = x[0:3, 0:3]
    out00 = float(np.sum(win * k) + 0.1)

    fig = plt.figure(figsize=(13.2, 4.9))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.55, 1.0, 1.55], wspace=0.45)

    ax = fig.add_subplot(gs[0])
    _grid(ax, x, vmin=0, vmax=2)
    ax.add_patch(plt.Rectangle((-0.5, -0.5), 3, 3, fill=False,
                               edgecolor=RED, lw=2.4))
    ax.set_title("Input (5 x 5)", fontsize=12)
    ax.text(2.0, 5.55, "3 x 3 window", color=RED, fontsize=10, ha="center")

    ax = fig.add_subplot(gs[1])
    _grid(ax, k, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_title("Kernel (3 x 3)", fontsize=12)
    ax.text(1.0, 3.55, "learned weights", color=GRAY, fontsize=10,
            ha="center")

    ax = fig.add_subplot(gs[2])
    out = np.full((3, 3), np.nan)
    out[0, 0] = out00
    _grid(ax, out, vmin=-1, vmax=2, fmt="{:.2f}")
    for t in (0.5, 1.5):
        ax.plot([-0.5, 2.5], [t, t], color=GRAY, lw=0.8)
        ax.plot([t, t], [-0.5, 2.5], color=GRAY, lw=0.8)
    ax.add_patch(plt.Rectangle((-0.5, -0.5), 3, 3, fill=False,
                               edgecolor=GRAY, lw=1.0))
    ax.text(1.5, 1.5, "one value\nper position", ha="center", va="center",
            fontsize=9.5, color=GRAY)
    ax.set_title("Activation map (3 x 3)", fontsize=12)
    ax.text(1.0, 3.25,
            f"$\\sum x_{{ij}}k_{{ij}}+b={out00:.2f}$",
            ha="center", fontsize=10.5, color=RED)

    fig.suptitle("Convolution: slide one kernel over the input, "
                 "dot-product at every position", fontsize=12.5, y=1.03)
    fig.savefig(f"{OUT}/S03_convolution.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_pooling():
    x = np.array([[1, 3, 2, 4],
                  [5, 6, 1, 2],
                  [7, 2, 8, 3],
                  [1, 4, 5, 6]], dtype=float)
    fig, axes = plt.subplots(1, 3, figsize=(12.4, 4.6),
                             gridspec_kw={"width_ratios": [1.5, 0.55, 1.0],
                                          "wspace": 0.35})
    ax = axes[0]
    _grid(ax, x, vmin=0, vmax=8, fmt="{:.0f}")
    for i0 in (0, 2):
        for j0 in (0, 2):
            ax.add_patch(plt.Rectangle((j0 - 0.5, i0 - 0.5), 2, 2,
                                       fill=False, edgecolor=RED, lw=2.2))
    ax.set_title("Input (4 x 4), 2 x 2 windows", fontsize=11.5)

    ax = axes[1]
    ax.axis("off")
    ax.annotate("", xy=(1.0, 0.5), xytext=(0.05, 0.5),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2))
    ax.text(0.5, 0.62, "max", color=BLUE, fontsize=12, ha="center")
    ax.text(0.5, 0.3, "stride 2", color=GRAY, fontsize=9.5, ha="center")

    ax = axes[2]
    y = np.array([[x[0:2, 0:2].max(), x[0:2, 2:4].max()],
                  [x[2:4, 0:2].max(), x[2:4, 2:4].max()]])
    _grid(ax, y, vmin=0, vmax=8, fmt="{:.0f}")
    ax.set_title("Output (2 x 2)", fontsize=11.5)
    ax.text(0.5, 2.55, "size halves, 75% of values dropped",
            ha="center", fontsize=10, color=RED)

    fig.suptitle("Max pooling keeps only the strongest activation "
                 "in each window", fontsize=12.5, y=1.02)
    fig.savefig(f"{OUT}/S03_pooling.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_relu_softmax():
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.6))

    ax = axes[0]
    xs = np.linspace(-3, 3, 400)
    ax.plot(xs, np.maximum(0, xs), color=BLUE, lw=2.6)
    ax.axhline(0, color=GRAY, lw=0.9)
    ax.axvline(0, color=GRAY, lw=0.9)
    ax.scatter([2.24, -1.3], [2.24, 0], color=RED, zorder=5)
    ax.annotate("2.24 -> 2.24", xy=(2.24, 2.24), xytext=(1.25, 3.0),
                arrowprops=dict(arrowstyle="->", color=RED),
                color=RED, fontsize=10)
    ax.annotate("-1.30 -> 0", xy=(-1.3, 0), xytext=(-2.9, 0.9),
                arrowprops=dict(arrowstyle="->", color=RED),
                color=RED, fontsize=10)
    ax.text(-2.6, -0.85, "dead zone", color=GRAY, fontsize=10)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-1.2, 3.6)
    ax.set_xlabel("x")
    ax.set_ylabel("ReLU(x)")
    ax.set_title("(a) ReLU: max(0, x)", fontsize=12)
    ax.grid(alpha=0.22)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    ax = axes[1]
    logits = np.array([2.0, 1.0, 0.1])
    p = np.exp(logits) / np.exp(logits).sum()
    names = ["cat", "dog", "bird"]
    bars = ax.bar(names, p, color=[RED, BLUE, GRAY], width=0.58)
    for b, v in zip(bars, p):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.3f}",
                ha="center", fontsize=10)
    ax.set_ylim(0, 0.78)
    ax.set_ylabel("probability")
    ax.set_title("(b) Softmax turns logits into a distribution",
                 fontsize=12)
    ax.text(0.5, 0.68,
            "logits [2.0, 1.0, 0.1]\nsum of bars = 1, max is amplified",
            transform=ax.transAxes, ha="center", fontsize=10, color=GRAY)
    ax.grid(alpha=0.22, axis="y")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S03_relu_softmax.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- Shannon
def fig_knee_curve():
    x = np.linspace(0, 10, 500)
    y = x - 0.9 + 1.8 / (1 + np.exp(-(x - 5.2)))
    fig, ax = plt.subplots(figsize=(7.6, 6.0))
    ax.plot(x, x, "--", color=GRAY, lw=1.4, label="$y=x$")
    ax.plot(x, y, color=BLUE, lw=2.8, label="ideas out vs ideas in")
    ax.fill_between(x, 0, x, where=(y < x), color=RED, alpha=0.08)
    ax.fill_between(x, x, 10.5, where=(y > x), color=GREEN, alpha=0.08)
    ax.axvline(5.2, color=ORANGE, lw=1.2, ls=":")
    ax.scatter([5.2], [5.2], color=ORANGE, s=60, zorder=5)
    ax.annotate("knee of the curve\ncritical mass", xy=(5.2, 5.2),
                xytext=(2.0, 7.6),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.3),
                color=ORANGE, fontsize=10.5, ha="center")
    ax.text(2.5, 2.05, "one idea in, < 1 idea out\nchain reaction dies",
            color=RED, fontsize=10, ha="center")
    ax.text(7.6, 9.55, "one idea in, > 1 idea out\nself-amplifying",
            color=GREEN, fontsize=10, ha="center")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10.5)
    ax.set_xlabel("ideas in")
    ax.set_ylabel("ideas out")
    ax.set_title("Shannon's uranium analogy: creative output vs input")
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.grid(alpha=0.22)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S04_knee_curve.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_heuristics():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.2))
    for ax in axes:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")
        ax.scatter([0.9], [0.9], color=BLUE, s=95, zorder=5)
        ax.scatter([8.9], [8.9], color=RED, s=95, zorder=5)
        ax.text(0.5, 0.35, "P", fontsize=13, color=BLUE)
        ax.text(8.7, 9.25, "S", fontsize=13, color=RED)

    # (a) one big jump vs a staircase of small jumps
    ax = axes[0]
    ax.annotate("", xy=(8.55, 8.55), xytext=(1.25, 1.25),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2,
                                connectionstyle="arc3,rad=-0.22"))
    ax.text(4.8, 7.55, "one big jump\n(often impossible)", color=RED,
            fontsize=10, ha="center")
    pts = [(0.9, 0.9), (2.8, 1.0), (2.8, 2.6), (4.5, 2.6),
           (4.5, 4.6), (6.4, 4.6), (6.4, 6.7), (8.9, 8.9)]
    px, py = zip(*pts)
    ax.plot(px, py, color=GREEN, lw=2.4, marker="o", ms=4.5)
    ax.text(4.6, 1.55, "small steps via sub-theorems", color=GREEN,
            fontsize=10, ha="center")
    ax.set_title("(a) Structural analysis: split the jump", fontsize=12)

    # (b) forward direction blocked; solve the reverse problem instead
    ax = axes[1]
    ax.annotate("", xy=(7.9, 7.9), xytext=(1.5, 1.5),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2))
    ax.scatter([4.7], [4.7], marker="x", color=RED, s=110, zorder=5)
    ax.text(5.25, 4.95, "forward proof stuck", color=RED, fontsize=10,
            ha="left")
    ax.annotate("", xy=(1.7, 1.7), xytext=(8.1, 8.1),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.4,
                                connectionstyle="arc3,rad=0.30"))
    ax.text(7.15, 3.15, "assume S,\nderive P", color=GREEN, fontsize=10,
            ha="center")
    ax.text(5.7, 1.85, "then reverse the\nsteps to get P -> S",
            color=GREEN, fontsize=9.5, ha="center")
    ax.set_title("(b) Inversion: solve the reverse problem", fontsize=12)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S04_heuristics.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- code review
def fig_convergence_metrics():
    fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.6))
    labels = ["before", "after"]
    colors = [GRAY, BLUE]

    data = [
        ("pass after 1 round (%)", [65, 78], (0, 100), "{:.0f}%"),
        ("needing 5+ rounds (%)", [8.9, 1.5], (0, 10), "{:.1f}%"),
        ("mean rounds", [2.08, 1.32], (0, 2.6), "{:.2f}"),
    ]
    for ax, (title, vals, ylim, fmt) in zip(axes, data):
        bars = ax.bar(labels, vals, color=colors, width=0.55)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v + ylim[1] * 0.025,
                    fmt.format(v), ha="center", fontsize=11)
        ax.set_ylim(*ylim)
        ax.set_title(title, fontsize=11.5)
        ax.grid(alpha=0.22, axis="y")
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)

    fig.suptitle("Review convergence after capping rounds and "
                 "re-reviewing only the diff", fontsize=12.5, y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S05_convergence_metrics.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- LLM Wiki
def fig_rag_vs_wiki():
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.2))

    def box(ax, xy, text, color, w=2.2, h=0.85):
        x, y = xy
        ax.add_patch(plt.Rectangle((x - w / 2, y - h / 2), w, h,
                                   facecolor=color, alpha=0.12,
                                   edgecolor=color, lw=1.6))
        ax.text(x, y, text, ha="center", va="center", fontsize=9.5,
                color="black")

    def arrow(ax, a, b, color=GRAY, style="-|>"):
        ax.annotate("", xy=b, xytext=a,
                    arrowprops=dict(arrowstyle=style, color=color, lw=1.6))

    for ax, title in zip(axes, ["(a) RAG: retrieve at query time",
                                "(b) Wiki: compile once, query many"]):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")
        ax.set_title(title, fontsize=11.5)

    ax = axes[0]
    for i, y in enumerate((8.3, 7.4, 6.5)):
        box(ax, (2.0, y), f"document {i + 1}", GRAY, w=2.4, h=0.62)
    box(ax, (2.0, 4.2), "embedding index", ORANGE, w=2.8, h=0.75)
    box(ax, (5.4, 4.2), "retriever\n(top-k chunks)", BLUE, w=2.5, h=0.85)
    box(ax, (5.4, 1.9), "LLM", RED, w=2.0, h=0.75)
    box(ax, (8.4, 1.9), "answer", GREEN, w=1.8, h=0.75)
    arrow(ax, (2.0, 6.1), (2.0, 4.6))
    arrow(ax, (3.4, 4.2), (4.1, 4.2))
    arrow(ax, (6.0, 3.75), (5.7, 2.3))
    arrow(ax, (6.4, 1.9), (7.5, 1.9))
    ax.text(5.0, 0.7, "raw text stays raw;\nevery query rebuilds context",
            ha="center", fontsize=9.3, color=GRAY)

    ax = axes[1]
    box(ax, (1.5, 8.4), "raw sources\n(papers, chats)", GRAY, w=2.4, h=0.8)
    box(ax, (4.3, 6.6), "ingest", ORANGE, w=1.9, h=0.75)
    box(ax, (7.4, 6.6), "wiki pages\n+ index.md", BLUE, w=2.6, h=0.9)
    box(ax, (7.4, 3.3), "query reads\ncompiled pages", PURPLE, w=2.6, h=0.9)
    box(ax, (3.9, 3.3), "lint\n(consistency)", GREEN, w=2.0, h=0.75)
    box(ax, (5.6, 1.0), "answer", RED, w=1.9, h=0.7)
    arrow(ax, (1.7, 7.95), (3.8, 6.9))
    arrow(ax, (5.3, 6.6), (6.0, 6.6))
    arrow(ax, (7.4, 6.1), (7.4, 3.8))
    arrow(ax, (6.1, 3.3), (4.9, 3.3))
    ax.annotate("", xy=(6.3, 6.1), xytext=(4.6, 3.6),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5,
                                ls="--",
                                connectionstyle="arc3,rad=-0.25"))
    arrow(ax, (7.4, 2.8), (6.5, 1.35))
    ax.text(5.0, 0.25, "knowledge accumulates between queries",
            ha="center", fontsize=9.3, color=GRAY)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S06_rag_vs_wiki.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- Veritasium: clocks
def fig_time_dilation():
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.2),
                             gridspec_kw={"width_ratios": [1.15, 1.0]})

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.plot([0, 10], [1.0, 1.0], color="black", lw=2)
    ax.fill_between([0, 10], 0, 1.0, color=GRAY, alpha=0.12)
    ax.plot([4.8, 5.6, 7.4], [1.0, 6.4, 1.0], color=GRAY, lw=1.5)
    ax.fill_between([4.8, 5.6, 7.4], [1.0, 6.4, 1.0], 1.0,
                    color=GRAY, alpha=0.18)
    ax.text(6.1, 2.5, "Mount Blue Sky\n4,326 m", ha="center", fontsize=9.5,
            color=GRAY)
    ax.text(2.7, 1.3, "Boulder\n~1,650 m", ha="center", fontsize=9.5,
            color=GRAY)
    for x, y, c, lab in [(1.6, 1.55, BLUE, "lab clock"),
                         (6.0, 6.75, RED, "mountain clock")]:
        ax.add_patch(plt.Rectangle((x - 0.42, y), 0.84, 0.62,
                                   facecolor=c, alpha=0.18,
                                   edgecolor=c, lw=1.6))
        ax.text(x, y + 0.31, "clock", ha="center", va="center",
                fontsize=9, color=c)
        ax.text(x, y + 0.85, lab, ha="center", fontsize=9.5, color=c)
    ax.annotate("", xy=(5.7, 6.55), xytext=(2.1, 2.25),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.4,
                                ls="--"))
    ax.text(2.45, 4.55, "2.7 km higher\nfaster by 25 ns/day",
            ha="center", fontsize=10, color=ORANGE)
    ax.set_title("(a) Same experiment, two elevations", fontsize=11.5)

    ax = axes[1]
    h = np.linspace(0, 3000, 300)
    df = 9.81 * h / (3.0e8) ** 2
    ax.plot(h, df * 1e13, color=BLUE, lw=2.4)
    ax.scatter([2670], [2.885], color=RED, s=70, zorder=5)
    ax.annotate("2.885 x 10$^{-13}$ per second",
                xy=(2670, 2.885), xytext=(1250, 3.9),
                arrowprops=dict(arrowstyle="->", color=RED),
                color=RED, fontsize=10)
    ax.annotate("about 25 ns after one day",
                xy=(2670, 2.885), xytext=(1350, 0.65),
                arrowprops=dict(arrowstyle="->", color=RED),
                color=RED, fontsize=10)
    ax.set_xlabel("height difference (m)")
    ax.set_ylabel("fractional rate difference (x 10$^{-13}$)")
    ax.set_title("(b) General relativity: $\\Delta f/f = g\\Delta h/c^2$",
                 fontsize=11.5)
    ax.grid(alpha=0.22)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S07_time_dilation.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_atomic_clock():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.8))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.plot([1.5, 8.5], [2.2, 2.2], color=BLUE, lw=2.2)
    ax.plot([1.5, 8.5], [7.4, 7.4], color=RED, lw=2.2)
    ax.text(0.8, 2.2, "E$_1$", fontsize=12, color=BLUE, va="center")
    ax.text(0.8, 7.4, "E$_2$", fontsize=12, color=RED, va="center")
    ax.annotate("", xy=(5.4, 7.15), xytext=(5.4, 2.45),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0,
                                connectionstyle="arc3,rad=0.0"))
    ax.text(5.7, 4.8, "photon\n$hf=\\Delta E$", color=ORANGE,
            fontsize=10.5)
    ax.scatter([5.4], [2.2], color=BLUE, s=45, zorder=5)
    ax.text(5.4, 1.4, "electron", ha="center", fontsize=9.5, color=BLUE)
    ax.text(5.0, 9.2, "tune the laser until the transition happens",
            ha="center", fontsize=10, color=GRAY)
    ax.set_title("(a) Atoms have fixed energy levels", fontsize=11.5)

    ax = axes[1]
    x = np.linspace(-1.0, 1.0, 500)
    y = 1 / (1 + (x / 0.14) ** 2)
    ax.plot(x, y, color=BLUE, lw=2.6)
    ax.axvline(0, color=RED, lw=1.2, ls=":")
    ax.scatter([0], [1], color=RED, s=55, zorder=5)
    ax.annotate("resonance\n$f_0$", xy=(0, 1.0), xytext=(0.28, 0.72),
                arrowprops=dict(arrowstyle="->", color=RED),
                color=RED, fontsize=10)
    ax.text(-0.95, 0.18, "detuning", fontsize=10, color=GRAY)
    ax.set_xlabel("laser frequency - $f_0$")
    ax.set_ylabel("excited atoms (a.u.)")
    ax.set_title("(b) Lock the laser to the peak", fontsize=11.5)
    ax.grid(alpha=0.22)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S07_atomic_clock.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_optical_lattice():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.9))

    ax = axes[0]
    x = np.linspace(0, 4, 800)
    ax.plot(x, np.cos(2 * np.pi * x), color=BLUE, lw=1.2, alpha=0.75,
            label="outgoing wave")
    ax.plot(x, -np.cos(2 * np.pi * x), color=RED, lw=1.2, alpha=0.75,
            ls="--", label="reflected wave")
    ax.fill_between(x, 0, np.cos(2 * np.pi * x) ** 2, color=GREEN,
                    alpha=0.25, label="intensity")
    for n in range(5):
        ax.scatter([n], [-0.05], color=PURPLE, s=40, zorder=6)
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.set_xlim(0, 4)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xlabel("position")
    ax.set_ylabel("field / intensity")
    ax.set_title("(a) Standing wave: atoms sit at antinodes", fontsize=11.5)
    ax.legend(loc="lower right", fontsize=8.2, frameon=False, ncol=1)
    ax.grid(alpha=0.18)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    ax = axes[1]
    U = -(np.cos(2 * np.pi * x) ** 2)
    ax.plot(x, U, color=PURPLE, lw=2.4)
    ax.scatter([1.0], [-1.0], color=RED, s=60, zorder=5)
    ax.annotate("trapped atom\n(300 nm well)", xy=(1.0, -1.0),
                xytext=(1.7, -0.35),
                arrowprops=dict(arrowstyle="->", color=RED),
                color=RED, fontsize=10)
    ax.text(2.0, -0.08, "potential minimum = stable trap",
            fontsize=9.8, color=GRAY)
    ax.set_xlim(0, 4)
    ax.set_ylim(-1.35, 0.25)
    ax.set_xlabel("position")
    ax.set_ylabel("dipole potential")
    ax.set_title("(b) Optical lattice: a bowl for each atom", fontsize=11.5)
    ax.grid(alpha=0.18)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S07_optical_lattice.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_frequency_comb():
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.8))

    ax = axes[0]
    teeth = np.arange(0, 40, 1.0)
    ax.vlines(teeth, 0, 1, color=BLUE, lw=1.4)
    ax.set_xlim(-0.5, 40)
    ax.set_ylim(0, 1.45)
    ax.set_yticks([])
    ax.set_xlabel("frequency (schematic)")
    ax.set_title("(a) A comb spans microwave to optical", fontsize=11.5)
    ax.annotate("", xy=(2.0, 1.22), xytext=(0.0, 1.22),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.3))
    ax.text(1.0, 1.3, "$f_{rep}$", color=RED, fontsize=11, ha="center")
    ax.axvspan(0, 3, color=ORANGE, alpha=0.10)
    ax.text(1.5, 0.18, "microwave\n(electronics)", color=ORANGE,
            fontsize=8.8, ha="center",
            bbox=dict(facecolor="white", alpha=0.85, edgecolor="none"))
    ax.axvspan(30, 39, color=GREEN, alpha=0.10)
    ax.text(34.5, 0.18, "optical\n(unknown)", color=GREEN,
            fontsize=8.8, ha="center",
            bbox=dict(facecolor="white", alpha=0.85, edgecolor="none"))
    ax.text(17, 0.55, "many teeth, evenly spaced", color=GRAY,
            fontsize=9.5, ha="center",
            bbox=dict(facecolor="white", alpha=0.85, edgecolor="none"))
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)

    ax = axes[1]
    x = np.linspace(29.2, 31.8, 500)
    ax.vlines([29.5, 30.5], 0, 1, color=BLUE, lw=2.0)
    ax.vlines([31.05], 0, 1, color=GREEN, lw=2.0)
    ax.text(29.5, 1.06, "comb tooth", color=BLUE, fontsize=9.5,
            ha="center")
    ax.text(31.05, 1.06, "unknown $f_{opt}$", color=GREEN, fontsize=9.5,
            ha="center")
    ax.annotate("", xy=(30.5, 0.45), xytext=(31.05, 0.45),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.4))
    ax.text(30.78, 0.22, "$f_{beat}$", color=RED, fontsize=11, ha="center")
    ax.text(30.0, 0.72,
            "$f_{opt}=n f_{rep}+f_{beat}$\nall terms are electronic",
            fontsize=9.8, color=GRAY, ha="center")
    ax.set_xlim(29.2, 31.8)
    ax.set_ylim(0, 1.45)
    ax.set_yticks([])
    ax.set_xlabel("frequency (schematic)")
    ax.set_title("(b) Beat note against the nearest tooth", fontsize=11.5)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S07_frequency_comb.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- EUV lithography
def _substrate(ax):
    ax.add_patch(plt.Rectangle((1, 1), 8, 2, facecolor=GRAY, alpha=0.35,
                               edgecolor=GRAY, lw=1.0))
    ax.text(5, 0.55, "silicon wafer", ha="center", fontsize=8.5,
            color=GRAY)


def fig_litho_cycle():
    fig, axes = plt.subplots(1, 4, figsize=(14.0, 4.0))
    titles = ["1. coat photoresist", "2. expose through mask",
              "3. etch the pattern", "4. deposit metal + strip"]

    for ax, title in zip(axes, titles):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6.4)
        ax.axis("off")
        ax.set_title(title, fontsize=10.5)
        _substrate(ax)

    # 1: resist on top
    ax = axes[0]
    ax.add_patch(plt.Rectangle((1, 3), 8, 0.75, facecolor=BLUE,
                               alpha=0.35, edgecolor=BLUE, lw=1.2))
    ax.text(5, 3.38, "photoresist", ha="center", va="center",
            fontsize=9, color=BLUE)

    # 2: mask with gaps and light
    ax = axes[1]
    ax.add_patch(plt.Rectangle((1, 3), 8, 0.75, facecolor=BLUE,
                               alpha=0.35, edgecolor=BLUE, lw=1.2))
    for x0, w in [(1, 2.2), (4.2, 1.6), (6.9, 2.1)]:
        ax.add_patch(plt.Rectangle((x0, 5.0), w, 0.35, facecolor="black"))
    for x in (2.6, 4.8, 7.4):
        ax.annotate("", xy=(x, 3.85), xytext=(x, 4.9),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.8))
    ax.text(5, 5.65, "mask / reticle", ha="center", fontsize=9,
            color="black")
    ax.text(5, 2.55, "exposed resist becomes soluble", ha="center",
            fontsize=8.2, color=GRAY)

    # 3: developed resist and etched trenches
    ax = axes[2]
    for x0, w in [(1, 1.6), (3.4, 1.0), (5.2, 1.6), (7.6, 1.4)]:
        ax.add_patch(plt.Rectangle((x0, 3), w, 0.75, facecolor=BLUE,
                                   alpha=0.35, edgecolor=BLUE, lw=1.0))
    for x0, w in [(2.6, 0.8), (6.8, 0.8)]:
        ax.add_patch(plt.Rectangle((x0, 1.7), w, 1.3,
                                   facecolor="white", edgecolor=GRAY,
                                   lw=1.0))
    ax.text(5, 2.35, "trenches", ha="center", fontsize=8.5, color=RED)

    # 4: metal fill
    ax = axes[3]
    for x0, w in [(1, 1.6), (3.4, 1.0), (5.2, 1.6), (7.6, 1.4)]:
        ax.add_patch(plt.Rectangle((x0, 3), w, 0.75, facecolor=BLUE,
                                   alpha=0.35, edgecolor=BLUE, lw=1.0))
    for x0, w in [(2.6, 0.8), (6.8, 0.8)]:
        ax.add_patch(plt.Rectangle((x0, 1.7), w, 1.3,
                                   facecolor=ORANGE, alpha=0.75,
                                   edgecolor=ORANGE, lw=1.0))
    ax.text(5, 2.35, "copper wires", ha="center", fontsize=8.5,
            color=ORANGE)

    fig.suptitle("One layer of a chip: coat, expose, etch and deposit; "
                 "repeat 10-100 times", fontsize=12, y=1.03)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S08_litho_cycle.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_rayleigh():
    fig = plt.figure(figsize=(13.6, 4.6))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.15, 1.15, 1.0], wspace=0.3)
    axes = [fig.add_subplot(gs[0, i]) for i in range(3)]

    def orders(ax, lam, color, title):
        ax.set_xlim(-5, 5)
        ax.set_ylim(-0.5, 6)
        ax.axis("off")
        ax.plot([-4, 4], [0, 0], color="black", lw=2)
        for x in (-0.3, 0.3):
            ax.plot([x, x], [0, 0.35], color="black", lw=3)
        for m in (-1, 0, 1):
            x = m * 2.2 * (lam / 650)
            ax.scatter([x], [5.2], color=color, s=45)
            ax.text(x, 5.55, f"{m:+d}" if m else "0", ha="center",
                    fontsize=9, color=color)
            ax.plot([0, x], [0.4, 5.1], color=color, lw=0.8, alpha=0.6)
        ax.text(0, -0.35, f"$\\lambda={lam}$ nm", ha="center",
                fontsize=10, color=color)
        ax.set_title(title, fontsize=11)

    orders(axes[0], 650, RED, "(a) red light: wide spacing")
    orders(axes[1], 532, GREEN, "(b) green light: orders move closer")

    ax = axes[2]
    k1, NA_imm = 0.25, 1.35
    labels = ["193 nm\nimmersion", "EUV\nNA 0.33", "high-NA\nEUV 0.55"]
    cds = [k1 * 193 / NA_imm, k1 * 13.5 / 0.33, k1 * 13.5 / 0.55]
    bars = ax.bar(labels, cds, color=[RED, BLUE, GREEN], width=0.6)
    for b, v in zip(bars, cds):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.8, f"{v:.1f} nm",
                ha="center", fontsize=9.5)
    ax.set_ylim(0, 42)
    ax.set_ylabel("minimum feature (nm)")
    ax.set_title("(c) Rayleigh limit\n$CD=k_1\\lambda/NA$", fontsize=11)
    ax.grid(alpha=0.22, axis="y")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    fig.suptitle("Diffraction sets the resolution: capture the 0 and "
                 "$\\pm1$ orders, then shorten the wavelength",
                 fontsize=12, y=1.03)
    fig.savefig(f"{OUT}/S08_rayleigh.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_multilayer():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8),
                             gridspec_kw={"width_ratios": [1.25, 1.0]})

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    for i in range(8):
        y = 0.8 + i * 0.62
        c = "#4c4c4c" if i % 2 == 0 else "#c9c9c9"
        ax.add_patch(plt.Rectangle((1.5, y), 7.0, 0.44, facecolor=c,
                                   edgecolor="white", lw=0.8))
    ax.annotate("", xy=(2.5, 7.4), xytext=(1.0, 8.2),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8))
    ax.text(1.0, 7.2, "13.5 nm", color=RED, fontsize=9.5)
    for i, y in enumerate([1.02, 1.64, 2.26, 2.88]):
        ax.annotate("", xy=(7.0, y + 0.2), xytext=(2.8, y),
                    arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.1,
                                    connectionstyle="arc3,rad=-0.15"))
    ax.text(8.2, 4.7, "quarter-wave\nlayers add\nin phase", color=BLUE,
            fontsize=9.5, ha="center")
    ax.text(5.0, 0.35, "Mo/Si bilayer stack (schematic)", ha="center",
            fontsize=9, color=GRAY)

    ax = axes[1]
    n = np.arange(0, 10)
    T = 0.7 ** n * 100
    bars = ax.bar(n, T, color=BLUE, width=0.62)
    for i, v in enumerate(T):
        ax.text(i, v + 2, f"{v:.0f}", ha="center", fontsize=8.2)
    ax.set_xlabel("number of mirror bounces")
    ax.set_ylabel("photons surviving (%)")
    ax.set_ylim(0, 110)
    ax.set_title("(b) 70% per mirror: 9 bounces leave only 4%",
                 fontsize=11)
    ax.grid(alpha=0.22, axis="y")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S08_multilayer.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_tin_source():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 4.9),
                             gridspec_kw={"width_ratios": [1.1, 1.3]})

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.add_patch(plt.Rectangle((1.0, 5.2), 2.2, 1.2, facecolor=GRAY,
                               alpha=0.35, edgecolor=GRAY))
    ax.text(2.1, 5.8, "tin oven\n500 C", ha="center", va="center",
            fontsize=8.5)
    for x, y in [(2.1, 4.8), (2.1, 4.2), (2.1, 3.6)]:
        ax.scatter([x], [y], color=ORANGE, s=35)
    ax.annotate("", xy=(4.8, 3.3), xytext=(2.3, 3.8),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.2))
    ax.text(2.6, 3.05, "50,000 droplets/s", fontsize=8.5, color=ORANGE)

    th = np.linspace(np.pi / 2, 3 * np.pi / 2, 200)
    ax.plot(6.0 + 2.0 * np.cos(th), 3.3 + 2.6 * np.sin(th), color=BLUE,
            lw=2.2)
    ax.text(6.0, 0.35, "collector mirror", ha="center", fontsize=9,
            color=BLUE)
    ax.scatter([5.7], [3.3], color="white", edgecolor=RED, s=160, lw=2.0,
               zorder=5)
    ax.text(5.7, 3.9, "plasma\n220,000 K", ha="center", fontsize=8.5,
            color=RED)
    ax.annotate("", xy=(5.5, 3.3), xytext=(8.6, 3.3),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2))
    ax.text(8.7, 3.55, "CO$_2$\nlaser", fontsize=8.5, color=RED,
            ha="right")
    for y in (2.0, 2.6, 4.0, 4.6):
        ax.annotate("", xy=(8.4, y), xytext=(7.0, y),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=0.9))
    ax.text(8.5, 4.95, "H$_2$ flow", fontsize=8.5, color=GREEN,
            ha="right")
    ax.set_title("(a) Make a tiny sun inside the machine", fontsize=11)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    stages = [(1.4, "droplet\n~30 um"), (4.2, "pancake\nafter pre-pulse"),
              (7.0, "low-density\ngas"), (9.3, "plasma\nEUV")]
    for x, lab in stages:
        ax.text(x, 1.0, lab, ha="center", fontsize=8.3, color=GRAY)
    ax.scatter([1.4], [4.2], color=ORANGE, s=90)
    ax.add_patch(Ellipse((4.2, 4.2), 1.1, 0.28, facecolor=ORANGE,
                         alpha=0.8))
    ax.scatter(np.random.default_rng(3).normal(7.0, 0.28, 40),
               np.random.default_rng(4).normal(4.2, 0.28, 40),
               color=ORANGE, s=12, alpha=0.55)
    ax.scatter([9.3], [4.2], color=RED, s=180, alpha=0.45)
    ax.annotate("", xy=(2.9, 4.2), xytext=(2.1, 4.2),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.8))
    ax.annotate("", xy=(5.6, 4.2), xytext=(4.9, 4.2),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.8))
    ax.annotate("", xy=(8.4, 4.2), xytext=(7.7, 4.2),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.8))
    ax.text(2.5, 5.0, "pre-pulse", fontsize=8.2, color=BLUE, ha="center")
    ax.text(5.25, 5.0, "pre-pulse 2", fontsize=8.2, color=BLUE,
            ha="center")
    ax.text(8.05, 5.0, "main pulse", fontsize=8.2, color=BLUE,
            ha="center")
    ax.text(5.0, 2.9, "three hits in 20 microseconds, "
            "same power -> more EUV", ha="center", fontsize=9, color=RED)
    ax.set_title("(b) Three pulses per droplet", fontsize=11)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S08_tin_source.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_euv_path():
    fig, ax = plt.subplots(figsize=(13.0, 4.2))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5)
    ax.axis("off")

    boxes = [(1.1, "source\n+ collector"), (3.8, "illuminator\nmirrors"),
             (6.5, "reticle"), (9.1, "projection\noptics"),
             (11.6, "wafer")]
    for x, lab in boxes:
        ax.add_patch(plt.Rectangle((x - 0.85, 2.2), 1.7, 1.2,
                                   facecolor=BLUE, alpha=0.10,
                                   edgecolor=BLUE, lw=1.3))
        ax.text(x, 2.8, lab, ha="center", va="center", fontsize=8.8)
    for x0, x1 in zip([1.95, 4.65, 7.35, 9.95], [2.95, 5.65, 8.25, 10.75]):
        ax.annotate("", xy=(x1, 2.8), xytext=(x0, 2.8),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0))
    ax.text(6.5, 4.4, "6 mirrors + reticle, each about 70% reflective",
            ha="center", fontsize=10, color=GRAY)
    ax.text(6.5, 1.3, "about 8% of the light reaches the wafer; "
            "with the collector, 9 bounces -> 4%",
            ha="center", fontsize=10, color=RED)
    ax.set_title("EUV optical path: every element is a mirror, "
                 "because lenses absorb 13.5 nm light", fontsize=11.5)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S08_euv_path.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- Polymorphs
def fig_polymorph_energy():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.9))

    def well(x, x0, depth, width):
        return depth * (1 - np.exp(-((x - x0) / width) ** 2))

    ax = axes[0]
    x = np.linspace(0, 10, 700)

    def y_choc(xx):
        return 1.9 - (0.25 + 0.85 * np.exp(-((xx - 3.2) / 0.75) ** 2)
                      + 1.55 * np.exp(-((xx - 6.8) / 0.9) ** 2))

    ax.plot(x, y_choc(x), color=BLUE, lw=2.6)
    ax.scatter([3.2], [y_choc(3.2)], color=ORANGE, s=65, zorder=5)
    ax.scatter([6.8], [y_choc(6.8)], color=GREEN, s=65, zorder=5)
    ax.text(3.2, y_choc(3.2) + 0.28, "Form IV\nmp 27 C", ha="center",
            fontsize=9.5, color=ORANGE)
    ax.text(6.8, y_choc(6.8) + 0.62, "Form V\nmp 34 C", ha="center",
            fontsize=9.5, color=GREEN)
    ax.annotate("heat can cross\nback and forth", xy=(5.0, y_choc(5.0)),
                xytext=(4.9, 2.1), ha="center", fontsize=9.5,
                color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.set_ylim(0, 2.6)
    ax.set_xlim(0, 10)
    ax.set_yticks([])
    ax.set_xlabel("crystal packing")
    ax.set_ylabel("free energy")
    ax.set_title("(a) Chocolate: shallow barrier, reversible", fontsize=11.5)

    ax = axes[1]

    def y_rito(xx):
        return 3.9 - 0.55 * np.exp(-((xx - 2.8) / 0.7) ** 2) \
            - 3.55 * np.exp(-((xx - 7.0) / 0.8) ** 2)

    ax.plot(x, y_rito(x), color=BLUE, lw=2.6)
    ax.scatter([2.8], [y_rito(2.8)], color=ORANGE, s=65, zorder=5)
    ax.scatter([7.0], [y_rito(7.0)], color=GREEN, s=65, zorder=5)
    ax.text(2.8, y_rito(2.8) + 0.22, "Form I", ha="center", fontsize=10,
            color=ORANGE)
    ax.annotate("Form II", xy=(7.1, y_rito(7.0) + 0.05), xytext=(8.4, 0.5),
                ha="center", fontsize=10, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.0))
    ax.annotate("", xy=(6.4, 0.75), xytext=(3.1, 3.3),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.8,
                                ls="--", connectionstyle="arc3,rad=-0.35"))
    ax.text(5.1, 3.45, "a seed crystal lowers\nthe activation energy",
            ha="center", fontsize=9.3, color=GREEN)
    ax.text(3.9, 0.55, "deep well: cannot go back", ha="center",
            fontsize=9.5, color=RED)
    ax.set_ylim(0, 3.9)
    ax.set_xlim(0, 10)
    ax.set_yticks([])
    ax.set_xlabel("crystal packing")
    ax.set_ylabel("free energy")
    ax.set_title("(b) Ritonavir: high barrier, one-way trap", fontsize=11.5)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S09_polymorph_energy.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_ir_spectrum():
    fig, axes = plt.subplots(2, 1, figsize=(9.2, 5.6), sharex=True)
    x = np.linspace(500, 2500, 1200)

    ax = axes[0]
    y = 0.08 + 0.75 * np.exp(-((x - 1350) / 260) ** 2)
    ax.plot(x, y, color=BLUE, lw=2.0)
    ax.text(1350, 0.9, "silver cyanate\nAg-O-C$\\equiv$N", ha="center",
            fontsize=9.5, color=BLUE)
    ax.annotate("one broad band", xy=(1450, 0.82), xytext=(2050, 0.62),
                fontsize=9.2, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.set_ylim(0, 1.15)
    ax.set_yticks([])
    ax.set_ylabel("absorbance")
    ax.set_title("(a) Wöhler's compound: stable, one broad feature",
                 fontsize=11)
    ax.grid(alpha=0.18, axis="x")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    ax = axes[1]
    y = 0.08 + 0.70 * np.exp(-((x - 2150) / 45) ** 2) \
        + 0.55 * np.exp(-((x - 1050) / 70) ** 2)
    ax.plot(x, y, color=RED, lw=2.0)
    ax.text(1250, 0.9, "silver fulminate\nAg-C$\\equiv$N-O", ha="center",
            fontsize=9.5, color=RED)
    ax.annotate("C$\\equiv$N stretch", xy=(2150, 0.78), xytext=(1750, 0.95),
                fontsize=8.8, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.annotate("weak N-O bond", xy=(1050, 0.63), xytext=(700, 0.9),
                fontsize=8.8, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.set_ylim(0, 1.15)
    ax.set_yticks([])
    ax.set_xlabel("wavenumber (cm$^{-1}$), high to low")
    ax.set_ylabel("absorbance")
    ax.set_title("(b) Liebig's compound: explosive, two distinct bands",
                 fontsize=11)
    ax.grid(alpha=0.18, axis="x")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.invert_xaxis()

    fig.suptitle("Same atoms, different bonds: infrared spectra are a "
                 "fingerprint", fontsize=12, y=1.01)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S09_ir_spectrum.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_chocolate_temper():
    fig, ax = plt.subplots(figsize=(9.6, 5.2))
    t = np.array([0, 2, 4, 5, 8, 11, 13, 17, 20, 25, 30, 34, 40, 46])
    T = np.array([22, 48, 48, 40, 27, 27, 32, 32, 32, 20, 12, 12, 12, 12])
    ax.plot(t, T, color=BLUE, lw=2.4, marker="o", ms=4)
    ax.axhline(34, color=GREEN, lw=1.0, ls=":")
    ax.axhline(27, color=ORANGE, lw=1.0, ls=":")
    ax.axhline(13, color=GRAY, lw=1.0, ls=":")
    ax.text(1, 50.5, "melt all crystals (45-50 C)", fontsize=9.2,
            color=RED)
    ax.text(8.3, 22.6, "cool to 27 C:\nnucleate many forms", fontsize=9.2,
            color=ORANGE)
    ax.text(14.6, 35.2, "warm to 32 C:\nmelt III and IV,\nkeep V", fontsize=9.2,
            color=GREEN)
    ax.text(31.0, 14.2, "cool fast to 12 C:\nlock Form V", fontsize=9.2,
            color=BLUE)
    ax.set_xlim(0, 46)
    ax.set_ylim(8, 52)
    ax.set_xlabel("time (min)")
    ax.set_ylabel("temperature (C)")
    ax.set_title("Tempering chocolate: temperature and time select the "
                 "polymorph")
    ax.grid(alpha=0.22)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S09_chocolate_temper.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_tin_pest():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8),
                             gridspec_kw={"width_ratios": [1.0, 1.15]})

    ax = axes[0]
    T = np.linspace(-40, 80, 400)
    # schematic free energies crossing at 13 C
    E_white = 1.0 - 0.004 * (T - 13)
    E_gray = 1.0 + 0.004 * (T - 13)
    ax.plot(T, E_white, color=BLUE, lw=2.4, label="white (silver) tin")
    ax.plot(T, E_gray, color=GRAY, lw=2.4, label="gray tin")
    ax.axvline(13, color=RED, lw=1.1, ls=":")
    ax.text(15, 1.35, "13 C", color=RED, fontsize=9.5)
    ax.text(45, 0.78, "white tin\nstable", color=BLUE, fontsize=9.5,
            ha="center")
    ax.text(-34, 0.66, "gray tin\nstable", color=GRAY, fontsize=9.5,
            ha="center")
    ax.set_xlim(-40, 80)
    ax.set_ylim(0.6, 1.45)
    ax.set_yticks([])
    ax.set_xlabel("temperature (C)")
    ax.set_ylabel("free energy")
    ax.set_title("(a) Below 13 C, gray tin is favoured", fontsize=11)
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    ax.grid(alpha=0.18)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    times = ["0 h", "3 h", "8 h", "14 h"]
    fracs = [0.02, 0.18, 0.45, 0.9]
    for i, (lab, f) in enumerate(zip(times, fracs)):
        y = 4.4 - i * 1.15
        ax.add_patch(plt.Rectangle((0.8, y), 7.6, 0.7,
                                   facecolor="#d9d9d9", edgecolor=GRAY,
                                   lw=1.0))
        ax.add_patch(plt.Rectangle((0.8, y), 7.6 * f, 0.7,
                                   facecolor="#7f7f7f", edgecolor="none"))
        ax.text(0.2, y + 0.35, lab, fontsize=8.8, ha="right",
                va="center", color=GRAY)
    ax.text(4.6, 5.5, "one gray speck nucleates and spreads",
            ha="center", fontsize=9.8, color=RED)
    ax.text(4.6, 0.55, "gray tin is less dense: the metal swells and crumbles",
            ha="center", fontsize=9.2, color=GRAY)
    ax.set_title("(b) Tin pest: a self-seeding phase change", fontsize=11)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S09_tin_pest.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def _box(ax, x, y, w, h, text, color, fs=9.5):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.03",
                                facecolor=color, edgecolor="black",
                                lw=1.0, alpha=0.13))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs)


def fig_enigma_path():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.0),
                             gridspec_kw={"width_ratios": [1.55, 1.0]})

    ax = axes[0]
    ax.set_xlim(0, 10.2)
    ax.set_ylim(0, 6)
    ax.axis("off")

    y_top, y_bot, h = 3.7, 1.2, 1.0
    boxes = [(0.15, "Keyboard"), (1.55, "Plugboard"), (2.95, "Rotor I"),
             (4.25, "Rotor II"), (5.55, "Rotor III")]
    for x, name in boxes:
        _box(ax, x, y_top, 1.05, h, name, BLUE, fs=8.6)
        _box(ax, x, y_bot, 1.05, h, name, GRAY, fs=8.6)
    _box(ax, 7.9, 1.35, 0.8, 3.5, "Reflector", PURPLE, fs=9.2)

    segs = [(1.2, 1.55), (2.6, 2.95), (4.0, 4.25), (5.3, 5.55),
            (6.6, 7.9)]
    for x1, x2 in segs:
        ax.annotate("", xy=(x2, y_top + h / 2), xytext=(x1, y_top + h / 2),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.1))
        ax.annotate("", xy=(x1, y_bot + h / 2), xytext=(x2, y_bot + h / 2),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.1))

    ax.annotate("", xy=(7.0, y_bot + h + 0.1),
                xytext=(7.0, y_top - 0.1),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
    ax.text(6.85, 2.55, "current turns\naround here", fontsize=8.4,
            color=GRAY, ha="right")

    ax.text(0.15, 5.55, "forward path", fontsize=11, color=BLUE,
            weight="bold")
    ax.text(0.15, 0.35, "return path (different wires)", fontsize=11,
            color=GRAY, weight="bold")

    labels_top = [(0.67, "Y"), (2.07, "Y"), (3.47, "H"),
                  (4.77, "B"), (6.07, "Q")]
    for x, s in labels_top:
        ax.text(x, 5.15, s, ha="center", fontsize=12, color=BLUE)
    labels_bot = [(6.07, "E"), (4.77, "?"), (3.47, "?"), (2.07, "?"),
                  (0.67, "E")]
    for x, s in labels_bot:
        ax.text(x, 2.5, s, ha="center", fontsize=11, color=GRAY)
    ax.text(0.67, 0.95, "lamp", fontsize=8.5, color=GRAY, ha="center")

    ax.text(4.3, 3.05, "no letter ever encrypts to itself",
            fontsize=9.6, color=RED, ha="center")
    ax.set_title("(a) Signal path through the Enigma", fontsize=11.5)

    ax = axes[1]
    p = np.roll(np.arange(26), 1)
    for i in range(26):
        ax.scatter(i, p[i], color=BLUE, s=16, zorder=3)
    ax.plot([-0.8, 25.8], [-0.8, 25.8], color=RED, lw=1.2, ls="--")
    ax.text(4.0, 22.0, "no dots on y = x", color=RED, fontsize=9.3,
            ha="left")
    letters = [chr(65 + i) for i in range(26)]
    ax.set_xticks(range(0, 26, 5))
    ax.set_xticklabels([letters[i] for i in range(0, 26, 5)], fontsize=8)
    ax.set_yticks(range(0, 26, 5))
    ax.set_yticklabels([letters[i] for i in range(0, 26, 5)], fontsize=8)
    ax.set_xlabel("input letter", fontsize=9.5)
    ax.set_ylabel("output letter", fontsize=9.5)
    ax.set_xlim(-1.5, 26.5)
    ax.set_ylim(-1.5, 26.5)
    ax.grid(alpha=0.15)
    ax.set_title("(b) A permutation with no fixed point", fontsize=11.5)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S10_enigma_path.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_keyspace():
    fig, ax = plt.subplots(figsize=(10.2, 4.3))
    names = ["Commercial Enigma (1918)\n6 rotor orders x 26^3 windows",
             "Military Enigma, mid-1930s\n+ rings + 6 plugboard swaps",
             "Military Enigma, 1939\n5 rotors, 10 plugboard swaps"]
    vals = [6 * 26 ** 3, 7.1e18, 1.0e23]
    colors = [BLUE, ORANGE, RED]
    bars = ax.barh([2, 1, 0], vals, color=colors, height=0.55, alpha=0.85)
    txt = ["about 100,000", "7 x 10^18", "over 10^23"]
    for bar, t in zip(bars, txt):
        ax.text(bar.get_width() * 1.35, bar.get_y() + bar.get_height() / 2,
                t, va="center", fontsize=9.5)
    ax.set_yticks([2, 1, 0])
    ax.set_yticklabels(names, fontsize=9.2)
    ax.set_xscale("log")
    ax.set_xlim(1e4, 1e28)
    ax.set_xlabel("number of possible daily settings (log scale)",
                  fontsize=9.5)
    ax.grid(axis="x", alpha=0.2)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.text(1.2e20, 1.62, "another cipher used by Hitler: ~10^170  (off scale)",
            fontsize=9.2, color=PURPLE, ha="left")
    ax.set_title("Each upgrade multiplied the search space", fontsize=11.5)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S10_keyspace.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_crib_loop():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.0))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    angles = np.linspace(np.pi / 2, np.pi / 2 - 2 * np.pi, 6)[:-1]
    cx, cy, r = 5.0, 3.3, 1.9
    pts = [(cx + r * np.cos(a), cy + r * np.sin(a)) for a in angles]
    nodes = ["R", "W", "E", "O", "S"]
    col = [RED, ORANGE, GREEN, BLUE, PURPLE]
    for (x, y), s, c in zip(pts, nodes, col):
        ax.scatter([x], [y], s=900, color=c, alpha=0.18, zorder=2)
        ax.text(x, y, s, ha="center", va="center", fontsize=13,
                weight="bold", zorder=4)
    for i in range(5):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % 5]
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.5,
                                    shrinkA=18, shrinkB=18,
                                    connectionstyle="arc3,rad=-0.2"))
    ax.text(5.0, 3.3, "crib\nmenu", ha="center", va="center",
            fontsize=10, color=GRAY)
    ax.text(5.0, 5.6, "Each edge is one Enigma state;\n"
                       "a correct setting closes the cycle",
            ha="center", fontsize=9.5, color=GRAY)
    ax.set_title("(a) A crib becomes a loop of constraints", fontsize=11.5)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    for i, (x, lab) in enumerate(zip([1.2, 4.0, 6.8],
                                     ["Enigma at 6", "Enigma at 22",
                                      "Enigma at 9"])):
        _box(ax, x, 3.2, 1.9, 1.1, lab, BLUE, fs=8.8)
    ax.text(0.45, 3.75, "R", fontsize=12, weight="bold")
    ax.text(3.55, 3.75, "Y", fontsize=11, color=ORANGE)
    ax.text(6.35, 3.75, "S", fontsize=11, color=GREEN)
    ax.text(9.35, 3.75, "R", fontsize=12, weight="bold")
    for x in [0.7, 3.1, 5.9, 8.7]:
        ax.annotate("", xy=(x + 0.4, 3.75), xytext=(x, 3.75),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.2))
    ax.annotate("", xy=(0.7, 2.2), xytext=(9.3, 2.2),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.3,
                                connectionstyle="arc3,rad=0.35"))
    ax.text(5.0, 0.95, "loop closes only when rotor order,\n"
                       "ring settings and positions all match",
            ha="center", fontsize=9.3, color=RED)
    ax.text(5.0, 5.5, "the plugboard cancels between chained machines:\n"
                       "only the rotors have to form the loop",
            ha="center", fontsize=9.4, color=GRAY)
    ax.set_title("(b) Three Enigma clones wired back to back",
                 fontsize=11.5)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S10_crib_loop.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_xz_chain():
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.8),
                             gridspec_kw={"width_ratios": [1.15, 1.0]})

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    names = [("Applications and services", BLUE),
             ("OpenSSH (remote login)", PURPLE),
             ("Shared libraries", BLUE),
             ("liblzma / XZ", RED),
             ("one unpaid maintainer", RED)]
    ys = [5.0, 3.95, 2.9, 1.85, 0.75]
    for (name, c), y in zip(names, ys):
        _box(ax, 2.3, y, 5.4, 0.72, name, c, fs=9.2)
    for y1, y2 in zip(ys[:-1], ys[1:]):
        ax.annotate("", xy=(5.0, y2 + 0.72), xytext=(5.0, y1),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.2))
    ax.text(8.0, 2.2, "a dependency\nnobody reviews", fontsize=9.2,
            color=RED, ha="left")
    ax.text(8.0, 0.95, "20 years of work,\nno salary", fontsize=9.2,
            color=RED, ha="left")
    ax.set_title("(a) The dependency chain behind remote login", fontsize=11)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    _box(ax, 1.2, 3.2, 3.0, 1.1, "OpenSSH\nheavily reviewed", BLUE, fs=9.2)
    _box(ax, 5.8, 3.2, 3.0, 1.1, "XZ\none maintainer", RED, fs=9.2)
    rng = np.random.default_rng(3)
    for _ in range(18):
        x = 1.2 + 3.0 * rng.random()
        y = 4.3 + 0.9 * rng.random()
        ax.scatter([x], [y], s=18, color=BLUE, alpha=0.7)
    ax.scatter([7.3], [5.0], s=45, color=RED)
    ax.text(2.7, 2.25, "Linus's law:\nwith enough eyeballs,\nall bugs are shallow",
            ha="center", fontsize=9.0, color=GRAY)
    ax.text(7.3, 2.25, "but most projects\nnever get those eyeballs",
            ha="center", fontsize=9.0, color=RED)
    ax.set_title("(b) Many eyes on the wrong layer", fontsize=11)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S11_xz_chain.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_compression():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    nodes = {
        "root": (5.0, 5.2), "N": (2.6, 3.9), "i1": (6.8, 3.9),
        "E": (5.5, 2.5), "i2": (8.0, 2.5), "sp": (7.2, 1.1),
        "J": (8.9, 1.1)}
    edges = [("root", "N", "0"), ("root", "i1", "1"),
             ("i1", "E", "0"), ("i1", "i2", "1"),
             ("i2", "sp", "0"), ("i2", "J", "1")]
    for a, b, lab in edges:
        x1, y1 = nodes[a]
        x2, y2 = nodes[b]
        ax.plot([x1, x2], [y1, y2], color=GRAY, lw=1.3)
        ax.text((x1 + x2) / 2 + 0.15, (y1 + y2) / 2,
                lab, fontsize=9, color=GRAY)
    labels = {"root": "", "N": "N\n430", "i1": "", "E": "E\n250",
              "i2": "", "sp": "space\n200", "J": "J\n1"}
    for k, (x, y) in nodes.items():
        ax.scatter([x], [y], s=520 if k in ("N", "E", "sp", "J") else 260,
                   color=BLUE if k in ("N", "E", "sp", "J") else GRAY,
                   alpha=0.18, zorder=2)
        ax.text(x, y, labels[k], ha="center", va="center", fontsize=8.6,
                zorder=3)
    ax.text(5.0, 0.3, "N = 0   E = 10   space = 110   J = 111",
            ha="center", fontsize=9.6, family="monospace")
    ax.set_title("(a) Huffman coding: frequent symbols get short codes",
                 fontsize=10.8)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    chunks = [(0.3, "NEVER", GREEN), (2.0, "GONNA", GRAY),
              (3.6, "GIVE", GRAY), (5.0, "YOU", GRAY),
              (6.2, "UP", GRAY), (7.4, "NEVER", RED)]
    for x, s, c in chunks:
        _box(ax, x, 3.6, 1.2, 0.7, s, c, fs=8.8)
    ax.annotate("", xy=(7.5, 3.5), xytext=(1.5, 3.5),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.5,
                                connectionstyle="arc3,rad=0.35"))
    ax.text(4.5, 2.0, "copy 5 characters\nfrom 24 positions back",
            ha="center", fontsize=9.6, color=RED)
    ax.text(5.0, 4.8, "the second NEVER is never stored as text:\n"
                       "it is a (distance, length) pointer",
            ha="center", fontsize=9.4, color=GRAY)
    ax.text(5.0, 0.8, "LZ77 finds repeated chunks; Huffman then encodes "
                       "the pointers",
            ha="center", fontsize=9.2, color=BLUE)
    ax.set_title("(b) LZ77: replace a repeated chunk with a pointer",
                 fontsize=10.8)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S11_compression.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_ssh_paint():
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.8))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.text(0.3, 5.55, "Alice", ha="left", fontsize=11, weight="bold")
    ax.text(0.3, 1.35, "Bob", ha="left", fontsize=11, weight="bold")
    alice = [(0.6, 4.4, "#f2c200", "private\nyellow"),
             (2.1, 4.4, "#ff4d4d", "public red"),
             (3.6, 4.4, "#ff9a00", "orange\nsent")]
    bob = [(0.6, 2.6, "#4d79ff", "private\nblue"),
           (2.1, 2.6, "#ff4d4d", "public red"),
           (3.6, 2.6, "#2e8b57", "green\nsent")]
    for x, y, c, lab in alice + bob:
        ax.add_patch(Circle((x, y), 0.42, color=c, alpha=0.85))
        ax.text(x, y - 0.72, lab, ha="center", fontsize=8.2)
    ax.annotate("", xy=(3.4, 4.4), xytext=(3.1, 4.4),
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.annotate("exchange", xy=(4.8, 3.5), xytext=(3.9, 3.5),
                arrowprops=dict(arrowstyle="<->", color=GRAY),
                fontsize=8.8, color=GRAY, ha="center")
    ax.add_patch(Circle((5.7, 3.5), 0.46, color="#6b8e23", alpha=0.9))
    ax.text(5.7, 2.8, "same olive\nsecret", ha="center", fontsize=8.4)
    ax.text(5.0, 1.1, "an eavesdropper sees orange and green,\n"
                       "but cannot unmix the private colors",
            ha="center", fontsize=9.2, color=GRAY)
    ax.set_title("(a) Diffie-Hellman: agree on a secret in public",
                 fontsize=10.8)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    _box(ax, 0.4, 3.2, 2.0, 1.0, "Alice", BLUE, fs=10)
    _box(ax, 4.0, 3.2, 2.0, 1.0, "Casper\n(attacker)", RED, fs=9.3)
    _box(ax, 7.6, 3.2, 2.0, 1.0, "Bob", GREEN, fs=10)
    ax.annotate("", xy=(3.8, 4.2), xytext=(2.6, 4.2),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.2))
    ax.annotate("", xy=(7.4, 4.2), xytext=(6.2, 4.2),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.2))
    ax.text(3.2, 4.5, "secret k1", ha="center", fontsize=8.8, color=PURPLE)
    ax.text(6.8, 4.5, "secret k2", ha="center", fontsize=8.8, color=PURPLE)
    ax.text(5.0, 2.2, "Alice and Bob each think they share a key\n"
                       "with the other, but Casper relays and reads everything",
            ha="center", fontsize=9.2, color=RED)
    ax.text(5.0, 0.9, "RSA certificates break the symmetry:\n"
                       "only the real Bob can decrypt the challenge",
            ha="center", fontsize=9.2, color=GREEN)
    ax.set_title("(b) The man in the middle", fontsize=10.8)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S11_ssh_paint.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_xz_backdoor():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.2),
                             gridspec_kw={"width_ratios": [1.05, 1.25]})

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.text(5.0, 5.65, "build time", ha="center", fontsize=11,
            color=BLUE, weight="bold")
    _box(ax, 1.0, 4.4, 8.0, 0.7,
         "Git history: ordinary-looking source", BLUE, fs=9.0)
    _box(ax, 1.0, 3.2, 8.0, 0.7,
         "binary test blob: payload hidden as 'random data'", RED, fs=9.0)
    _box(ax, 1.0, 2.0, 8.0, 0.7,
         "build script unpacks it into liblzma", RED, fs=9.0)
    for y1, y2 in [(4.4, 3.9), (3.2, 2.7)]:
        ax.annotate("", xy=(5.0, y2), xytext=(5.0, y1),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.2))
    ax.text(5.0, 1.0, "reviewers read the source,\nnot the blob",
            ha="center", fontsize=9.2, color=GRAY)
    ax.set_title("(a) Step 1: hide the payload", fontsize=10.8)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    _box(ax, 0.3, 4.6, 4.2, 0.7, "IFUNC resolver runs early", PURPLE,
         fs=8.8)
    _box(ax, 5.3, 4.6, 4.4, 0.7, "installs a dynamic audit hook", PURPLE,
         fs=8.8)
    ax.annotate("", xy=(5.3, 4.95), xytext=(4.5, 4.95),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.1))
    _box(ax, 0.3, 3.4, 4.2, 0.7, "linker fills RSA_Decrypt\nentry in the GOT",
         BLUE, fs=8.6)
    _box(ax, 5.3, 3.4, 4.4, 0.7, "hook swaps in the payload", RED, fs=8.8)
    ax.annotate("", xy=(5.3, 3.75), xytext=(4.5, 3.75),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.1))
    _box(ax, 2.8, 2.2, 4.4, 0.7, "GOT becomes read-only: too late",
         GRAY, fs=8.8)
    ax.annotate("", xy=(5.0, 2.9), xytext=(5.0, 3.4),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.1))
    _box(ax, 2.8, 1.0, 4.4, 0.7, "SSH calls RSA_Decrypt", GREEN, fs=9.0)
    ax.annotate("", xy=(5.0, 1.7), xytext=(5.0, 2.2),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.1))
    ax.text(7.35, 1.5, "payload checks\nthe secret key,\nthen opens a\nroot shell",
            ha="left", va="center", fontsize=8.0, color=RED)

    ax2 = ax.inset_axes([0.05, 0.02, 0.9, 0.12])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 1)
    ax2.add_patch(plt.Rectangle((3.6, 0.2), 2.0, 0.6, color=ORANGE,
                                alpha=0.55))
    ax2.text(4.6, 0.5, "window", ha="center", va="center", fontsize=8.2)
    ax2.annotate("", xy=(3.5, 0.5), xytext=(0.3, 0.5),
                 arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
    ax2.annotate("", xy=(6.2, 0.5), xytext=(5.7, 0.5),
                 arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
    ax2.text(0.3, 0.8, "GOT filling", fontsize=7.6, color=GRAY)
    ax2.text(6.3, 0.8, "read-only", fontsize=7.6, color=GRAY)
    ax2.set_xticks([])
    ax2.set_yticks([])
    for s in ax2.spines.values():
        s.set_visible(False)
    ax.text(5.0, 5.6, "runtime: the Goldilocks window", ha="center",
            fontsize=11, color=RED, weight="bold")
    ax.set_title("(b) Steps 2 and 3: hijack and hide", fontsize=10.8)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S11_xz_backdoor.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- S12
def fig_speed_limit():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.6))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(Circle((1.7, 3), 0.65, color=ORANGE, alpha=0.9))
    ax.text(1.7, 3, "Sun", ha="center", va="center", fontsize=9,
            color="white", weight="bold")
    ax.add_patch(Circle((8.5, 3), 0.45, color=BLUE))
    ax.text(8.5, 3, "Earth", ha="center", va="center", fontsize=8.5,
            color="white")
    for r in (1.2, 1.8, 2.4):
        ax.add_patch(Circle((1.7, 3), r, fill=False, ls="--",
                            color=GRAY, lw=0.9, alpha=0.7))
    ax.annotate("", xy=(7.9, 3), xytext=(2.5, 3),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.8))
    ax.text(5.3, 3.35, "gravity ripple at c", ha="center", fontsize=9.5,
            color=RED)
    ax.text(5.3, 2.55, "about 8 minutes", ha="center", fontsize=9.5,
            color=GRAY)
    ax.set_title("(a) If the Sun vanished", fontsize=10.8)

    ax = axes[1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 9)
    ax.plot([0, 8.8], [0, 8.8], color=BLUE, lw=1.2, ls="--")
    ax.plot([0, -0.9], [0, 8.8], color=BLUE, lw=1.2, ls="--")
    ax.plot([8, 8], [0, 8.7], color=GREEN, lw=1.4)
    ax.plot([0, 8], [0, 8], color=BLUE, lw=1.8)
    ax.plot([0, 8], [0, 0], color=ORANGE, lw=1.5, ls="--")
    ax.plot(0, 0, "o", color=RED, ms=6)
    ax.text(0.15, -0.55, "Sun vanishes", fontsize=9, color=RED)
    ax.plot(8, 8, "o", color=BLUE, ms=6)
    ax.text(7.75, 8.2, "Earth feels it\n8 min later", fontsize=8.5,
            color=BLUE, ha="right", va="bottom")
    ax.plot(8, 0, "o", color=ORANGE, ms=6)
    ax.text(6.1, -0.55, "Newton: instant effect", fontsize=9, color=ORANGE)
    ax.text(2.3, 4.4, "light cone", fontsize=9, color=BLUE)
    clean(ax, equal=False)
    ax.set_xlabel("distance x (light-minutes)", fontsize=9)
    ax.set_ylabel("time ct (minutes)", fontsize=9)
    ax.set_title("(b) Why instant action breaks causality", fontsize=10.8)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S12_speed_limit.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_epr():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 4.8))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(Ellipse((5, 3), 1.1, 0.55, color=ORANGE, alpha=0.85))
    ax.text(5, 3, "source", ha="center", va="center", fontsize=8.5)
    ax.annotate("", xy=(2.0, 4.4), xytext=(4.6, 3.2),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.4))
    ax.annotate("", xy=(8.0, 1.6), xytext=(5.4, 2.8),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.4))
    _box(ax, 0.5, 3.9, 1.7, 0.9, "SG magnet\nelectron", BLUE, fs=8.4)
    _box(ax, 7.8, 1.0, 1.7, 0.9, "SG magnet\npositron", RED, fs=8.4)
    ax.text(2.2, 5.25, "spin +/− ?", fontsize=8.8, color=BLUE)
    ax.text(7.3, 2.35, "spin −/+ ?", fontsize=8.8, color=RED)
    ax.text(5.0, 2.25, "total spin = 0", ha="center", fontsize=8.8,
            color=GRAY)
    ax.set_title("(a) One measurement fixes the distant partner",
                 fontsize=10.6)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(Circle((1.1, 4.2), 0.22, color=BLUE))
    ax.add_patch(Circle((1.1, 1.8), 0.22, color=RED))
    ax.text(1.1, 5.0, "electron", ha="center", fontsize=8.5, color=BLUE)
    ax.text(1.1, 1.0, "positron", ha="center", fontsize=8.5, color=RED)
    for y in (4.2, 1.8):
        ax.add_patch(plt.Rectangle((2.0, y - 0.32), 1.15, 0.64,
                                   facecolor="white", edgecolor=PURPLE,
                                   lw=1.1))
        ax.plot([2.0, 2.575, 3.15], [y + 0.32, y + 0.06, y + 0.32],
                color=PURPLE, lw=1.0)
        ax.text(2.575, y - 0.02, "3 answers", ha="center", va="center",
                fontsize=7.6, color=PURPLE)
    ax.text(1.0, 3.0, "pre-agreed at the source", fontsize=8.6,
            color=PURPLE)
    ax.annotate("", xy=(7.0, 4.2), xytext=(3.5, 4.2),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.3))
    ax.annotate("", xy=(7.0, 1.8), xytext=(3.5, 1.8),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
    _box(ax, 7.1, 3.75, 2.1, 0.9, "measure A", BLUE, fs=8.5)
    _box(ax, 7.1, 1.35, 2.1, 0.9, "measure B", RED, fs=8.5)
    ax.text(5.0, 5.1, "local hidden variables", ha="center", fontsize=10,
            color=PURPLE, weight="bold")
    ax.set_title("(b) The loophole: answers were fixed in advance",
                 fontsize=10.6)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S12_epr.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_bell():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.8))

    ax = axes[0]
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Circle((0, 0), 1.0, fill=False, color=GRAY, lw=1.0,
                        ls="--"))
    for angle, label, color in [(0, "A: 0°", BLUE),
                                 (120, "B: 120°", GREEN),
                                 (240, "C: 240°", ORANGE)]:
        t = np.deg2rad(angle)
        ax.plot([0, 0.95 * np.cos(t)], [0, 0.95 * np.sin(t)],
                color=color, lw=2.0)
        ax.text(1.15 * np.cos(t), 1.15 * np.sin(t), label,
                ha="center", va="center", fontsize=9.5, color=color)
    ax.set_title("(a) Three settings, 120° apart", fontsize=10.6)

    ax = axes[1]
    vals = [25.0, 100.0 / 3.0]
    ax.bar([0, 1], vals, color=[BLUE, RED], width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["quantum\nmechanics", "local hidden\nvariables"],
                       fontsize=9)
    ax.set_ylabel("disagreement rate (%)", fontsize=9)
    ax.set_ylim(0, 42)
    ax.axhline(25, color=GRAY, ls=":", lw=1.0)
    for x, v in zip([0, 1], vals):
        ax.text(x, v + 1.3, f"{v:.0f}%", ha="center", fontsize=10)
    ax.text(0.5, 37, "an experiment can tell them apart", ha="center",
            fontsize=8.8, color=GRAY)
    clean(ax, equal=False)
    ax.set_title("(b) Bell's inequality: 25% vs 33%", fontsize=10.6)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S12_bell.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_many_worlds():
    fig, ax = plt.subplots(figsize=(9.6, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.plot(1.0, 3.0, "o", color=RED, ms=7)
    ax.text(1.0, 3.35, "measure", ha="center", fontsize=9, color=RED)
    ax.plot([1.05, 3.2], [3.0, 4.6], color=GRAY, lw=1.4)
    ax.plot([1.05, 3.2], [3.0, 1.4], color=GRAY, lw=1.4)
    _box(ax, 3.3, 4.25, 6.1, 0.75,
         "World A:  electron +,  positron −,  you see +", BLUE, fs=8.8)
    _box(ax, 3.3, 1.0, 6.1, 0.75,
         "World B:  electron −,  positron +,  you see −", RED, fs=8.8)
    ax.text(6.3, 3.0, "both outcomes happen", ha="center", fontsize=9.5,
            color=GRAY)
    ax.text(6.3, 2.55, "the branches already contain\ncorrelated answers",
            ha="center", fontsize=8.8, color=GRAY)
    ax.text(5.0, 5.45, "no collapse, no faster-than-light message",
            ha="center", fontsize=10.2, color=PURPLE, weight="bold")
    fig.tight_layout()
    fig.savefig(f"{OUT}/S12_many_worlds.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- S13
def fig_metabolic_scaling():
    fig, ax = plt.subplots(figsize=(8.8, 5.6))
    M = np.logspace(-3, 4, 200)
    B3 = 250.0 * (M / 3.0) ** 0.75
    B2 = 250.0 * (M / 3.0) ** (2.0 / 3.0)
    ax.loglog(M, B3, color=RED, lw=2.0, label="Kleiber: B ∝ M^(3/4)")
    ax.loglog(M, B2, color=BLUE, lw=2.0, ls="--",
              label="surface law: B ∝ M^(2/3)")
    points = [(0.002, "Etruscan shrew", (8, -15)),
              (3.0, "cat", (8, -15)),
              (70.0, "human", (-40, 10)),
              (3000.0, "elephant", (-58, 9))]
    for m, name, off in points:
        b = 250.0 * (m / 3.0) ** 0.75
        ax.plot(m, b, "o", color=GREEN, ms=6, zorder=5)
        ax.annotate(name, (m, b), xytext=off,
                    textcoords="offset points", fontsize=8.5)
    ax.text(1.4e-3, 2.2e4,
            "same 1000× mass:\n178× energy (3/4)\nvs 100× energy (2/3)",
            fontsize=8.6, color=GRAY)
    ax.set_xlabel("body mass M (kg)", fontsize=9.5)
    ax.set_ylabel("metabolic rate B (kcal/day)", fontsize=9.5)
    ax.legend(fontsize=8.8, loc="lower right")
    clean(ax, equal=False)
    ax.set_title("Metabolic rate vs body mass (log–log)", fontsize=11)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S13_metabolic_scaling.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_network():
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.8))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.plot(0.7, 3.0, "o", color=RED, ms=7)
    ax.text(0.7, 3.4, "source", ha="center", fontsize=8.5, color=RED)
    ax.plot([0.75, 4.3], [3.0, 4.6], color=GRAY, lw=1.5)
    ax.plot([0.75, 4.3], [3.0, 1.4], color=GRAY, lw=1.5)
    ax.plot(4.3, 4.6, "o", color=BLUE, ms=5)
    ax.plot(4.3, 1.4, "o", color=BLUE, ms=5)
    ax.text(2.3, 4.35, "two full paths", fontsize=8.6, color=GRAY)
    ax.text(2.6, 1.05, "wasteful", fontsize=9.5, color=GRAY,
            weight="bold")
    ax.plot([5.6, 7.2], [3.0, 3.0], color=GREEN, lw=3.0)
    ax.plot([7.2, 9.1], [3.0, 4.6], color=GREEN, lw=1.8)
    ax.plot([7.2, 9.1], [3.0, 1.4], color=GREEN, lw=1.8)
    ax.plot(5.6, 3.0, "o", color=RED, ms=7)
    ax.plot(9.1, 4.6, "o", color=BLUE, ms=5)
    ax.plot(9.1, 1.4, "o", color=BLUE, ms=5)
    ax.text(7.9, 3.35, "share the trunk", ha="center", fontsize=8.6,
            color=GREEN)
    ax.text(7.9, 1.05, "efficient", fontsize=9.5, color=GREEN,
            weight="bold")
    ax.set_title("(a) Branch late, not everywhere", fontsize=10.6)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    levels = [
        [(5.0, 0.7, 0.50)],
        [(4.1, 1.9, 0.354), (5.9, 1.9, 0.354)],
        [(3.55, 3.1, 0.250), (4.65, 3.1, 0.250),
         (5.35, 3.1, 0.250), (6.45, 3.1, 0.250)],
        [(2.9, 4.3, 0.177), (3.5, 4.3, 0.177), (4.1, 4.3, 0.177),
         (4.7, 4.3, 0.177), (5.3, 4.3, 0.177), (5.9, 4.3, 0.177),
         (6.5, 4.3, 0.177), (7.1, 4.3, 0.177)],
    ]
    for i in range(len(levels) - 1):
        for j, (x0, y0, r0) in enumerate(levels[i]):
            for k in (2 * j, 2 * j + 1):
                x1, y1, r1 = levels[i + 1][k]
                ax.plot([x0, x1], [y0, y1], color=GRAY,
                        lw=10 * r1, solid_capstyle="round")
                ax.plot(x1, y1, "o", color=BLUE, ms=2.5)
    ax.plot(5.0, 0.7, "o", color=RED, ms=7)
    ax.text(5.0, 0.18, "aorta", ha="center", fontsize=8.5, color=RED)
    ax.text(5.0, 5.05, "terminal units: same width in every species",
            ha="center", fontsize=9.0, color=BLUE)
    ax.text(8.15, 3.3, "A₀ = 2A₁\nat each split", ha="left", fontsize=8.8,
            color=GREEN)
    ax.set_title("(b) Self-similar branching with conserved area",
                 fontsize=10.6)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S13_network.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_heartbeats():
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    life = np.logspace(-0.1, 2.2, 200)
    hr1 = 1e9 / (life * 525600.0)
    hr3 = 3e9 / (life * 525600.0)
    ax.loglog(life, hr1, color=RED, lw=2.2, label="1 billion heartbeats")
    ax.loglog(life, hr3, color=RED, lw=1.2, ls=":", label="3 billion")
    points = [(1.5, 1200, "Etruscan shrew", (7, 7)),
              (15, 160, "cat", (7, 7)),
              (65, 30, "African elephant", (-70, -25)),
              (79, 70, "human", (9, 6))]
    for x, y, name, off in points:
        ax.plot(x, y, "o", color=BLUE if name != "human" else PURPLE,
                ms=6, zorder=5)
        ax.annotate(name, (x, y), xytext=off, textcoords="offset points",
                    fontsize=8.5)
    ax.text(2.0, 28, "almost every mammal", fontsize=9, color=RED)
    ax.text(28, 250, "humans: ~3 billion", fontsize=9, color=PURPLE)
    ax.set_xlim(0.8, 200)
    ax.set_ylim(10, 2200)
    ax.set_xlabel("lifespan (years)", fontsize=9.5)
    ax.set_ylabel("heart rate (beats per minute)", fontsize=9.5)
    ax.legend(fontsize=8.8, loc="lower left")
    clean(ax, equal=False)
    ax.set_title("Heart rate × lifespan ≈ constant", fontsize=11)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S13_heartbeats.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_city_scaling():
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.9))

    P = np.logspace(4, 7, 200)
    base = 1e5
    infra = (P / base) ** 0.85
    socio = (P / base) ** 1.15

    ax = axes[0]
    ax.loglog(P, infra, color=BLUE, lw=2.0,
              label="infrastructure: 0.85")
    ax.loglog(P, socio, color=RED, lw=2.0,
              label="wages, GDP, patents, crime: 1.15")
    ax.axvline(base, color=GRAY, ls=":", lw=1.0)
    ax.text(1.15e5, 0.22, "reference city", fontsize=8.2, color=GRAY,
            rotation=90)
    ax.text(1.35e4, 3.8, "×2 population\n→ ×1.8 infra\n→ ×2.2 socio",
            fontsize=8.2, color=GRAY)
    ax.set_xlabel("population P", fontsize=9.5)
    ax.set_ylabel("total quantity (normalized)", fontsize=9.5)
    ax.legend(fontsize=8.3, loc="upper left")
    clean(ax, equal=False)
    ax.set_title("(a) Total quantities scale as power laws", fontsize=10.6)

    ax = axes[1]
    ax.semilogx(P, (P / base) ** -0.15, color=BLUE, lw=2.0,
                label="infrastructure per person")
    ax.semilogx(P, (P / base) ** 0.15, color=RED, lw=2.0,
                label="wages / patents / crime per person")
    ax.set_ylim(0.4, 2.2)
    ax.set_yticks([0.5, 1.0, 1.5, 2.0])
    ax.axvline(base, color=GRAY, ls=":", lw=1.0)
    ax.set_xlabel("population P", fontsize=9.5)
    ax.set_ylabel("per-capita quantity (normalized)", fontsize=9.5)
    ax.legend(fontsize=8.3, loc="upper left")
    clean(ax, equal=False)
    ax.set_title("(b) Per person: cheaper infrastructure, denser activity",
                 fontsize=10.6)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S13_city_scaling.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_ai_brain_rot():
    """Conceptual: default AI use raises the floor and compresses the top."""
    x = np.linspace(-3.4, 3.4, 500)
    before = np.exp(-x ** 2 / 2)
    after = 1.35 * np.exp(-(x - 0.55) ** 2 / (2 * 0.55 ** 2))

    fig, ax = plt.subplots(figsize=(8.8, 4.5))
    ax.fill_between(x, before, color=GRAY, alpha=0.12)
    ax.fill_between(x, after, color=PURPLE, alpha=0.14)
    ax.plot(x, before, color=GRAY, lw=2.0, label="Before AI")
    ax.plot(x, after, color=PURPLE, lw=2.2, label="After default AI use")
    ax.axvline(0, color=GRAY, ls=":", lw=1.0)
    ax.annotate("floor rises", xy=(-2.2, 0.24), xytext=(-3.1, 0.72),
                fontsize=9.2, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
    ax.annotate("distribution narrows:\neveryone pulled to the mean",
                xy=(0.55, 1.30), xytext=(1.20, 1.10),
                fontsize=9.2, color=PURPLE,
                arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.1))
    ax.annotate("aim for the upper tail", xy=(2.05, 0.22),
                xytext=(1.35, 0.55), fontsize=9.6, color=BLUE,
                fontstyle="italic",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0))
    ax.set_xlim(-3.4, 3.4)
    ax.set_ylim(0, 1.5)
    ax.set_yticks([])
    ax.set_xlabel("relative skill / quality of work", fontsize=9.8)
    ax.set_ylabel("density (schematic)", fontsize=9.8)
    ax.legend(fontsize=8.8, loc="upper left", frameon=False)
    clean(ax, equal=False)
    ax.set_title("Default AI use compresses the distribution, not just the mean",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S14_ai_brain_rot.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_km_twoflux():
    """Kubelka-Munk two-flux transmittance and its angular dependence."""
    K, S = 8.0, 0.5
    A = 1.0 + K / S
    B = np.sqrt(A ** 2 - 1.0)

    def transmittance(U):
        return B / (A * np.sinh(U) + B * np.cosh(U))

    U = np.linspace(0.001, 6.0, 400)
    T = transmittance(U)
    asymptote = 2.0 * B / (A + B) * np.exp(-U)

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.4))
    ax = axes[0]
    ax.plot(U, T, color=BLUE, lw=2.0, label="exact two-flux")
    ax.plot(U, asymptote, color=ORANGE, ls="--", lw=1.4,
            label=r"large-$U$ asymptote")
    ax.set_xlabel(r"optical thickness  $U = B S X$", fontsize=9.6)
    ax.set_ylabel("transmittance  T", fontsize=9.6)
    ax.set_ylim(0, 1.0)
    ax.legend(fontsize=8.6, frameon=False)
    clean(ax, equal=False)
    ax.set_title(r"(a) $T = B/(A\sinh U + B\cosh U)$", fontsize=10.4)

    ax = axes[1]
    theta = np.linspace(0, 85, 400)
    cos_t = np.clip(np.cos(np.deg2rad(theta)), 0.12, 1.0)
    for U0, color, label in (
        (0.9, GREEN, r"thin  $U_0 = 0.9$"),
        (2.2, ORANGE, r"medium  $U_0 = 2.2$"),
        (3.6, PURPLE, r"dense  $U_0 = 3.6$"),
    ):
        ax.plot(theta, transmittance(U0 / cos_t), color=color, lw=2.0,
                label=label)
    ax.set_xlabel(r"view angle  $\theta$  (deg)", fontsize=9.6)
    ax.set_ylabel("transmittance  T", fontsize=9.6)
    ax.set_ylim(0, 1.0)
    ax.legend(fontsize=8.4, frameon=False, loc="center right")
    clean(ax, equal=False)
    ax.set_title(r"(b) $X = D/\cos\theta$: silhouette turns opaque",
                 fontsize=10.4)
    ax.text(58, 0.80, "grazing angle", color=RED, fontsize=8.6,
            fontstyle="italic")

    fig.tight_layout()
    fig.savefig(f"{OUT}/S15_km_twoflux.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_markov_chain():
    """Pushkin letter pairs and convergence of the vowel fraction."""
    p_vv = 0.06 / 0.43
    p_cv = (0.43 - 0.06) / 0.57
    P = np.array([[p_vv, 1 - p_vv], [p_cv, 1 - p_cv]])

    rng = np.random.default_rng(7)
    n = 5000
    state = 0
    states = np.empty(n, dtype=int)
    for i in range(n):
        states[i] = state
        state = 0 if rng.random() < P[state, 0] else 1
    ratio = np.cumsum(states == 0) / np.arange(1, n + 1)

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.4))
    ax = axes[0]
    labels = ["VV", "VC", "CV", "CC"]
    actual = [0.06, 0.37, 0.37, 0.20]
    independent = [0.43 ** 2, 0.43 * 0.57, 0.57 * 0.43, 0.57 ** 2]
    xpos = np.arange(4)
    ax.bar(xpos - 0.19, actual, width=0.36, color=BLUE, label="Pushkin pairs")
    ax.bar(xpos + 0.19, independent, width=0.36, color=GRAY,
           label="if independent")
    ax.set_xticks(xpos, labels)
    ax.set_ylabel("pair frequency", fontsize=9.6)
    ax.set_ylim(0, 0.42)
    ax.legend(fontsize=8.6, frameon=False)
    clean(ax, equal=False)
    ax.set_title("(a) Letters are not independent", fontsize=10.4)

    ax = axes[1]
    ax.plot(np.arange(1, n + 1), ratio, color=PURPLE, lw=1.6,
            label="running vowel fraction")
    ax.axhline(0.43, color=ORANGE, ls="--", lw=1.2, label="43% target")
    ax.set_xscale("log")
    ax.set_xlabel("generated letters", fontsize=9.6)
    ax.set_ylabel("vowel fraction", fontsize=9.6)
    ax.set_ylim(0.0, 1.0)
    ax.legend(fontsize=8.6, frameon=False)
    clean(ax, equal=False)
    ax.set_title("(b) A dependent chain still obeys the LLN",
                 fontsize=10.4)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S16_markov_chain.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- AI learning
def fig_learning_edge():
    """An optimum lesson sits on the learner's edge; probing binary-searches it."""
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.5),
                             gridspec_kw={"width_ratios": [1.12, 1.0]})

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(plt.Rectangle((0.4, 3.0), 3.5, 0.95, facecolor=GRAY,
                               alpha=0.18, edgecolor=GRAY, lw=1.0))
    ax.add_patch(plt.Rectangle((3.9, 3.0), 1.7, 0.95, facecolor=BLUE,
                               alpha=0.22, edgecolor=BLUE, lw=1.6))
    ax.add_patch(plt.Rectangle((5.6, 3.0), 3.9, 0.95, facecolor=GRAY,
                               alpha=0.18, edgecolor=GRAY, lw=1.0))
    ax.text(2.15, 3.47, "already held", ha="center", va="center",
            fontsize=9.5, color=GRAY)
    ax.text(4.75, 3.47, "the edge", ha="center", va="center",
            fontsize=9.5, color=BLUE)
    ax.text(7.55, 3.47, "not reachable yet", ha="center", va="center",
            fontsize=9.5, color=GRAY)
    ax.annotate("teaching here\nis redundant", xy=(1.7, 3.95),
                xytext=(1.5, 4.95), ha="center", fontsize=9.3, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.1))
    ax.annotate("no foothold\nhere yet", xy=(7.4, 3.95),
                xytext=(7.9, 4.95), ha="center", fontsize=9.3, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.1))
    ax.annotate("one reasoning step\nabove what you hold", xy=(4.75, 3.95),
                xytext=(4.75, 5.35), ha="center", fontsize=9.6, color=BLUE,
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.annotate("", xy=(9.5, 2.4), xytext=(0.4, 2.4),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.2))
    ax.text(5.0, 1.85, "from current understanding to the goal",
            ha="center", fontsize=9.2, color="black")
    ax.text(5.0, 0.7, "a course written for many people\n"
            "must pick one edge for everybody", ha="center",
            fontsize=9.6, color=RED)
    ax.set_title("(a) Optimal teaching lives on the edge of understanding",
                 fontsize=11.5)

    ax = axes[1]
    edge = 0.62
    lo, hi = 0.0, 1.0
    los, his, pts, ok = [], [], [], []
    qs = [0.5, 0.75, 0.625, 0.6875, 0.65625, 0.640625, 0.6328125]
    for q in qs:
        los.append(lo)
        his.append(hi)
        pts.append(q)
        if q <= edge:
            ok.append(True)
            lo = q
        else:
            ok.append(False)
            hi = q
    los.append(lo)
    his.append(hi)
    ax.fill_between(np.arange(len(los)), los, his, step="post",
                    color=BLUE, alpha=0.18)
    for i, (q, good) in enumerate(zip(pts, ok)):
        ax.scatter([i], [q], color=GREEN if good else RED, s=55, zorder=6)
    ax.axhline(edge, color=ORANGE, ls="--", lw=1.3)
    ax.text(7.45, edge, "true edge\n0.62", ha="left", va="center",
            fontsize=9.3, color=ORANGE,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))
    ax.text(0.1, 0.93, "green: answered correctly\nred: not yet",
            fontsize=9.0, color=GRAY, va="top")
    ax.set_xlim(-0.5, 9.3)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("question number", fontsize=9.6)
    ax.set_ylabel("position on one strand", fontsize=9.6)
    ax.set_title("(b) Probe: each question halves the interval", fontsize=11.5)
    clean(ax, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S17_learning_edge.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_covector():
    """A covector counts level lines; alpha = 3dx - 2dy on v = (2, 5)."""
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.1))
    v = np.array([2.0, 5.0])

    ax = axes[0]
    xs = np.linspace(-1.0, 4.0, 2)
    for c in range(-6, 7):
        y = (3 * xs - c) / 2
        crossed = c in (-1, -2, -3, -4)
        ax.plot(xs, y, color=ORANGE if crossed else GRAY,
                lw=1.9 if crossed else 0.9, alpha=0.95 if crossed else 0.5)
    ax.annotate("", xy=(v[0], v[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.6,
                                mutation_scale=18))
    ax.scatter([0], [0], color=BLUE, s=50, zorder=6)
    ax.text(0.12, -0.5, "$c=0$", color=BLUE, fontsize=10, ha="left")
    ax.text(3.0, -1.55, "highlighted level lines: $c=-1,-2,-3,-4$",
            ha="center", fontsize=9.2, color=ORANGE)
    ax.text(3.05, 1.2, "$\\alpha(v)=-4$:\nfour level lines,\n"
            "counted with a minus sign", color=RED, fontsize=9.4,
            ha="center")
    ax.set_xlim(-0.9, 4.2)
    ax.set_ylim(-2.6, 6.6)
    ax.set_xlabel("$x$", fontsize=10)
    ax.set_ylabel("$y$", fontsize=10)
    ax.set_title("(a) One covector = one family of level lines",
                 fontsize=11.5)
    clean(ax)
    ax.grid(False)

    ax = axes[1]
    for xv in range(0, 4):
        ax.plot([xv, xv], [-0.6, 6.0], color=BLUE, lw=0.9, alpha=0.35)
    for yh in range(0, 6):
        ax.plot([-0.6, 4.0], [yh, yh], color=ORANGE, lw=0.9, alpha=0.35)
    for xv in (1, 2):
        ax.plot([xv, xv], [-0.6, 6.0], color=BLUE, lw=2.0)
    for yh in range(1, 6):
        ax.plot([-0.6, 4.0], [yh, yh], color=ORANGE, lw=1.8)
    ax.annotate("", xy=(v[0], v[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.6,
                                mutation_scale=18))
    ax.scatter([v[0]], [0], color=BLUE, s=35, zorder=6)
    ax.scatter([0], [v[1]], color=ORANGE, s=35, zorder=6)
    ax.plot([v[0], v[0]], [0, v[1]], color=GRAY, ls=":", lw=1.0)
    ax.plot([0, v[0]], [v[1], v[1]], color=GRAY, ls=":", lw=1.0)
    ax.text(1.0, -0.38, "$dx(v)=2$", color=BLUE, fontsize=10, ha="center",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))
    ax.text(3.9, 0.55, "$dx$: 2 vertical lines\n$dy$: 5 horizontal lines",
            color=GRAY, fontsize=9.2, ha="right", va="center",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.85))
    ax.text(3.7, 5.6, "$\\alpha(v)=3\\cdot 2-2\\cdot 5=-4$",
            color=RED, fontsize=11.5, ha="right")
    ax.set_xlim(-0.7, 4.0)
    ax.set_ylim(-0.7, 6.0)
    ax.set_xlabel("$x$", fontsize=10)
    ax.set_ylabel("$y$", fontsize=10)
    ax.set_title("(b) $dx$ and $dy$ count crossings; $\\alpha$ weighs them",
                 fontsize=11.5)
    clean(ax)
    ax.grid(False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/S17_covector.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_wedge():
    """Wedge product: signed area, antisymmetric, zero on parallel inputs."""
    fig, axes = plt.subplots(1, 3, figsize=(12.9, 3.5))

    def panel(ax, u, w, color, value, title, note, parallel=False):
        if not parallel:
            quad = np.array([[0, 0], u, np.array(u) + np.array(w), w])
            ax.fill(quad[:, 0], quad[:, 1], color=color, alpha=0.22)
        # draw w first so that a parallel u stays visible on top of it
        ax.annotate("", xy=w, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.2,
                                    mutation_scale=16))
        ax.annotate("", xy=u, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2,
                                    mutation_scale=16))
        ax.text(u[0] * 0.3 - 0.05, u[1] * 0.3 - 0.22, "$u$",
                color=BLUE, fontsize=10.5, ha="right",
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.75))
        ax.text(w[0] * 0.62 + 0.10, w[1] * 0.62 + 0.14, "$w$",
                color=PURPLE, fontsize=10.5, ha="left",
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.75))
        ax.set_xlim(-0.45, 3.5)
        ax.set_ylim(-0.45, 1.5)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=11)
        ax.text(0.5, 0.06, value, transform=ax.transAxes, ha="center",
                fontsize=11.5, color=color)
        ax.text(0.5, -0.08, note, transform=ax.transAxes, ha="center",
                fontsize=9.4, color=GRAY)

    panel(axes[0], (1, 0), (0, 1), GREEN, "$dx\\wedge dy\\,(u,w)=+1$",
          "(a) $u$ then $w$", "counter-clockwise: area +1")
    panel(axes[1], (0, 1), (1, 0), ORANGE, "$dx\\wedge dy\\,(w,u)=-1$",
          "(b) the two inputs swapped", "clockwise: the sign flips")
    panel(axes[2], (1.2, 0.3), (2.0, 0.5), RED, "$dx\\wedge dy\\,(u,w)=0$",
          "(c) $w$ parallel to $u$", "no area, so the machine returns 0",
          parallel=True)

    fig.suptitle("A wedge product is bilinear and antisymmetric: "
                 "subtracting the two orderings kills the symmetric part",
                 fontsize=11.8, y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/S17_wedge.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_reflection()
    fig_phase()
    fig_complex_impedance()
    fig_smith_construction()
    fig_smith_reading()
    fig_stub()
    fig_convolution()
    fig_pooling()
    fig_relu_softmax()
    fig_knee_curve()
    fig_heuristics()
    fig_convergence_metrics()
    fig_rag_vs_wiki()
    fig_time_dilation()
    fig_atomic_clock()
    fig_optical_lattice()
    fig_frequency_comb()
    fig_litho_cycle()
    fig_rayleigh()
    fig_multilayer()
    fig_tin_source()
    fig_euv_path()
    fig_polymorph_energy()
    fig_ir_spectrum()
    fig_chocolate_temper()
    fig_tin_pest()
    fig_enigma_path()
    fig_keyspace()
    fig_crib_loop()
    fig_xz_chain()
    fig_compression()
    fig_ssh_paint()
    fig_xz_backdoor()
    fig_speed_limit()
    fig_epr()
    fig_bell()
    fig_many_worlds()
    fig_metabolic_scaling()
    fig_network()
    fig_heartbeats()
    fig_city_scaling()
    fig_ai_brain_rot()
    fig_km_twoflux()
    fig_markov_chain()
    fig_learning_edge()
    fig_covector()
    fig_wedge()
    print("done")
