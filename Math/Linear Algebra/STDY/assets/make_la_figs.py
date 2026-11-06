"""Linear-algebra teaching figures for the Obsidian vault.

Usage:  python make_la_figs.py
Output: PNG files written next to this script (STDY/assets/).

Conventions
-----------
- Agg backend, dpi=200, English-only text (avoids CJK font issues).
- Fixed palette: RED / BLUE / GREEN / ORANGE / PURPLE / GRAY.
- clean(ax): light grid, no top/right spines, equal aspect by default.
- One figure = one concept; panels share the same axis scale when sizes matter.
- Labels that sit on top of lines get a white bbox; 3D labels use text2D.
- File name: L<lecture>_<topic>.png; embedded as ![[name.png]] + italic caption.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch, Rectangle, Circle, Patch
from matplotlib.lines import Line2D
from matplotlib.colors import LinearSegmentedColormap

OUT = "/mnt/c/X/STD/STD/Math/Linear Algebra/STDY/assets"

PAPER, PANEL, INK, MUTED, GRID = "#131312", "#1E1E2E", "#E5E7EB", "#9CA3AF", "#3A3A4A"
RED, BLUE, GREEN, ORANGE, PURPLE, GRAY = (
    "#ff6b6b", "#4dabf7", "#51cf66", "#ffa94d", "#b197fc", "#9CA3AF")
PAPER_RGB = (0.0745, 0.0745, 0.0706)
PANEL_RGB = (0.1176, 0.1176, 0.1804)

plt.rcParams.update({
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "text.color": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "grid.color": GRID,
    "legend.facecolor": PAPER,
    "legend.edgecolor": GRID,
    "figure.dpi": 100,
})


def dark3d(ax):
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color(PANEL_RGB + (1.0,))
        axis._axinfo["grid"]["color"] = GRID
        axis._axinfo["axisline"]["color"] = MUTED
        axis._axinfo["tick"]["color"] = MUTED


def clean(ax, equal=True):
    ax.grid(alpha=0.25)
    if equal:
        ax.set_aspect("equal", adjustable="box")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# ---------------------------------------------------------------- L1
def fig_l1():
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.0))

    ax = axes[0]
    x = np.linspace(-0.6, 3.2, 200)
    ax.plot(x, 2 * x, color=BLUE, lw=2.2, label="2x - y = 0")
    ax.plot(x, (3 + x) / 2, color=RED, lw=2.2, label="-x + 2y = 3")
    ax.scatter([1], [2], color=INK, s=60, zorder=5)
    ax.annotate("solution (1, 2)", (1, 2), textcoords="offset points",
                xytext=(12, 20), fontsize=11)
    ax.axhline(0, color=INK, lw=0.8)
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(-0.6, 3.2); ax.set_ylim(-0.6, 3.4)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Row picture: two lines meet at one point", fontsize=13)
    ax.legend(frameon=False, loc="upper left")
    clean(ax)

    ax = axes[1]
    c1 = np.array([2.0, -1.0]); c2 = np.array([-1.0, 2.0]); b = np.array([0.0, 3.0])
    ax.add_patch(FancyArrowPatch((0, 0), c1, arrowstyle="-|>", mutation_scale=18,
                                 color=BLUE, lw=2.4))
    ax.add_patch(FancyArrowPatch((0, 0), c2, arrowstyle="-|>", mutation_scale=16,
                                 color=GREEN, lw=2.2))
    ax.add_patch(FancyArrowPatch(c1, c1 + 2 * c2, arrowstyle="-|>", mutation_scale=18,
                                 color=GREEN, lw=2.2, alpha=0.55, linestyle="--"))
    ax.add_patch(FancyArrowPatch((0, 0), b, arrowstyle="-|>", mutation_scale=20,
                                 color=RED, lw=2.8))
    ax.plot([2 * c2[0], b[0]], [2 * c2[1], b[1]], ls=":", color=GRAY, lw=1.2)
    ax.plot([c1[0], b[0]], [c1[1], b[1]], ls=":", color=GRAY, lw=1.2)
    ax.text(2.1, -0.8, "$c_1 = (2,-1)$", color=BLUE, fontsize=11)
    ax.text(-3.05, 2.25, "$c_2 = (-1,2)$", color=GREEN, fontsize=11)
    ax.text(-1.75, 3.3, "$b = (0,3)$", color=RED, fontsize=11)
    ax.text(1.05, 1.15, "$2\\,c_2$", color=GREEN, fontsize=10, alpha=0.9)
    ax.text(-2.9, 0.55, "$1\\,c_1 + 2\\,c_2 = b$", fontsize=12)
    ax.axhline(0, color=INK, lw=0.8)
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(-3.2, 3.2); ax.set_ylim(-1.8, 5.2)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Column picture: combine columns to reach b", fontsize=13)
    clean(ax)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L1_row_vs_column.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L10
def fig_l10():
    fig = plt.figure(figsize=(12.6, 5.2))

    # left: R^3, row space = z-axis, null space = xy-plane (v = (0,0,1))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    dark3d(ax)
    s, t = np.meshgrid(np.linspace(-1.3, 1.3, 2), np.linspace(-1.3, 1.3, 2))
    ax.plot_surface(s, t, 0 * s, color=BLUE, alpha=0.45, linewidth=0)
    ax.plot([0, 0], [0, 0], [-1.5, 1.5], color=RED, lw=3)
    d = 0.25
    ax.plot([0, d, d, 0], [0, 0, 0, 0], [d, d, 0, 0], color=INK, lw=1.2)
    ax.scatter([0], [0], [0], color=INK, s=25)
    ax.text2D(0.58, 0.78, "row space = span(v)\ndim 1", color=RED, fontsize=10,
              transform=ax.transAxes)
    ax.text2D(0.04, 0.38, "null space = plane v.x = 0\ndim 2", color=BLUE,
              fontsize=10, transform=ax.transAxes)
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4); ax.set_zlim(-1.6, 1.6)
    ax.set_title("R^3: row space and null space\nare orthogonal complements",
                 fontsize=12.5)
    ax.view_init(elev=17, azim=-55)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.set_xlabel(""); ax.set_ylabel(""); ax.set_zlabel("")
    ax.grid(False)

    # right: R^2, column space and left null space lines
    ax = axes = fig.add_subplot(1, 2, 2)
    q = np.array([1.0, 2.0]); m = np.array([-2.0, 1.0])
    ax.plot([-3 * q[0], 3 * q[0]], [-3 * q[1], 3 * q[1]], color=GREEN, lw=3)
    ax.plot([-3 * m[0], 3 * m[0]], [-3 * m[1], 3 * m[1]], color=PURPLE, lw=3,
            linestyle="--")
    ax.add_patch(FancyArrowPatch((0, 0), q, arrowstyle="-|>", mutation_scale=16,
                                 color=GREEN, lw=2.4))
    ax.add_patch(FancyArrowPatch((0, 0), m, arrowstyle="-|>", mutation_scale=16,
                                 color=PURPLE, lw=2.4))
    # right-angle marker
    u1, u2 = q / np.linalg.norm(q), m / np.linalg.norm(m)
    d = 0.28
    ax.plot([d * u1[0], d * (u1[0] + u2[0]), d * u2[0]],
            [d * u1[1], d * (u1[1] + u2[1]), d * u2[1]], color=INK, lw=1.2)
    ax.text(1.45, 2.1, "column space\n(Ax), dim 1", color=GREEN, fontsize=10)
    ax.text(-3.45, -2.1, "left null space\n(A^T y = 0), dim 1", color=PURPLE,
            fontsize=10)
    ax.scatter([0], [0], color=INK, s=25, zorder=5)
    ax.set_xlim(-3.6, 3.2); ax.set_ylim(-3.4, 3.6)
    ax.set_xlabel("y1"); ax.set_ylabel("y2")
    ax.set_title("R^2: column space and left null space\nare orthogonal complements",
                 fontsize=12.5)
    clean(ax)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L10_four_subspaces.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L14
def fig_l14():
    fig = plt.figure(figsize=(12.6, 5.4))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    dark3d(ax)

    a1 = np.array([1.0, 0.0, 0.35]); a2 = np.array([0.0, 1.0, 0.55])
    b = np.array([1.2, 1.2, -0.6])
    n = np.cross(a1, a2)
    p = b - (b @ n) / (n @ n) * n
    s, t = np.meshgrid(np.linspace(-1.15, 1.15, 2), np.linspace(-1.15, 1.15, 2))
    X = s * a1[0] + t * a2[0]; Y = s * a1[1] + t * a2[1]; Z = s * a1[2] + t * a2[2]
    ax.plot_surface(X, Y, Z, color=BLUE, alpha=0.4, linewidth=0)
    ax.quiver(0, 0, 0, *b, color=RED, lw=2.6, arrow_length_ratio=0.09)
    ax.quiver(0, 0, 0, *p, color=BLUE, lw=2.6, arrow_length_ratio=0.09)
    ax.quiver(*p, *(b - p), color=ORANGE, lw=2.6, arrow_length_ratio=0.14)
    ax.text(*(b + np.array([0.05, 0.05, -0.18])), "b", color=RED, fontsize=12)
    ax.text(*(p + np.array([0.12, 0.1, 0.08])), "p", color=BLUE, fontsize=12)
    ax.text2D(0.60, 0.80, "e = b - p", color=ORANGE, fontsize=11,
              transform=ax.transAxes)
    # right-angle marker between p and e
    u1 = p / np.linalg.norm(p); u2 = (b - p) / np.linalg.norm(b - p); d = 0.16
    c = p + d * u1
    ax.plot([c[0], c[0] + d * u2[0]], [c[1], c[1] + d * u2[1]], [c[2], c[2] + d * u2[2]],
            color=INK, lw=1.2)
    ax.set_xlim(-0.8, 1.5); ax.set_ylim(-0.8, 1.5); ax.set_zlim(-0.9, 1.0)
    ax.set_xticks([-0.5, 0.0, 0.5, 1.0, 1.5])
    ax.set_yticks([-0.5, 0.0, 0.5, 1.0, 1.5])
    ax.set_zticks([-0.5, 0.0, 0.5, 1.0])
    ax.set_xlabel("x", labelpad=3); ax.set_ylabel("y", labelpad=3)
    ax.set_zlabel("z", labelpad=3)
    ax.set_title("Projection onto a plane:\ne = b - p is perpendicular to the plane",
                 fontsize=12.5)
    ax.view_init(elev=24, azim=-68)

    ax = fig.add_subplot(1, 2, 2)
    rng = np.random.default_rng(3)
    t = np.linspace(0.2, 5.0, 14)
    y = 1.0 + 1.8 * t + rng.normal(0, 0.55, t.size)
    coef = np.polyfit(t, y, 1)
    fit = np.polyval(coef, t)
    ax.scatter(t, y, color=BLUE, s=34, zorder=3, label="data")
    ax.plot(t, fit, color=RED, lw=2.4, label="least squares line")
    for ti, yi, fi in zip(t, y, fit):
        ax.plot([ti, ti], [yi, fi], ls="--", color=GRAY, lw=0.9)
    ax.set_xlabel("t"); ax.set_ylabel("y")
    ax.set_title("Least squares: choose the line that\nminimizes the sum of squared residuals",
                 fontsize=12.5)
    ax.legend(frameon=False)
    clean(ax, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L14_projection_least_squares.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L15
def fig_l15():
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.2))
    a1 = np.array([3.0, 1.0]); a2 = np.array([1.0, 2.0])
    proj = (a2 @ a1) / (a1 @ a1) * a1
    e = a2 - proj

    ax = axes[0]
    for vec, col, lab, off in [(a1, BLUE, "$a_1$", (-0.35, 0.15)),
                               (a2, ORANGE, "$a_2$", (0.12, 0.14))]:
        ax.add_patch(FancyArrowPatch((0, 0), vec, arrowstyle="-|>", mutation_scale=18,
                                     color=col, lw=2.6))
        ax.text(*(vec + np.array(off)), lab, color=col, fontsize=13)
    ax.plot([0, proj[0]], [0, proj[1]], ls="--", color=GRAY, lw=1.6)
    ax.scatter([proj[0]], [proj[1]], color=INK, s=25, zorder=5)
    ax.add_patch(FancyArrowPatch(proj, a2, arrowstyle="-|>", mutation_scale=16,
                                 color=GREEN, lw=2.2))
    ax.text(0.95, 1.35, "$e = a_2 - \\mathrm{proj}$", color=GREEN, fontsize=11)
    ax.text(proj[0] + 0.1, proj[1] - 0.25, "proj", color=INK, fontsize=10)
    ax.set_xlim(-0.4, 3.6); ax.set_ylim(-0.3, 2.6)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Step 1: subtract the projection onto $a_1$", fontsize=13)
    clean(ax)

    ax = axes[1]
    q1 = a1 / np.linalg.norm(a1); q2 = e / np.linalg.norm(e)
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(th), np.sin(th), ls=":", color=GRAY, lw=1.0)
    for vec, col, lab in [(q1, BLUE, "$q_1$"), (q2, GREEN, "$q_2$")]:
        ax.add_patch(FancyArrowPatch((0, 0), vec, arrowstyle="-|>", mutation_scale=18,
                                     color=col, lw=2.6))
        ax.text(*(vec * 1.08), lab, color=col, fontsize=13)
    d = 0.12
    ax.plot([d * q1[0], d * (q1[0] + q2[0]), d * q2[0]],
            [d * q1[1], d * (q1[1] + q2[1]), d * q2[1]], color=INK, lw=1.2)
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Step 2: normalize -> orthonormal $q_1, q_2$", fontsize=13)
    clean(ax)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L15_gram_schmidt.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L18
def fig_l18():
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.2))
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

    ax = axes[0]
    A = np.array([[2.0, 1.0], [0.0, 2.0]])
    img = sq @ A.T
    ax.add_patch(Polygon(sq, closed=True, facecolor="#2A2A2A", edgecolor=GRAY,
                         ls="--", lw=1.6, label="unit square, area 1"))
    ax.add_patch(Polygon(img, closed=True, facecolor=BLUE, alpha=0.35,
                         edgecolor=BLUE, lw=2.0, label="image, area |det A| = 4"))
    for v, col in [(A[:, 0], RED), (A[:, 1], GREEN)]:
        ax.add_patch(FancyArrowPatch((0, 0), v, arrowstyle="-|>", mutation_scale=18,
                                     color=col, lw=2.4))
    ax.text(0.15, -0.35, "$(2, 0)$", color=RED, fontsize=11)
    ax.text(0.35, 2.15, "$(1, 2)$", color=GREEN, fontsize=11)
    ax.text(1.0, 1.05, "area = 4", fontsize=12)
    ax.set_xlim(-0.4, 3.4); ax.set_ylim(-0.6, 2.8)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("det A = 4: area is multiplied by 4", fontsize=13)
    ax.legend(frameon=False, loc="upper left")
    clean(ax)

    ax = axes[1]
    B = np.array([[1.0, 1.0], [2.0, 2.0]])
    img = sq @ B.T
    ax.add_patch(Polygon(sq, closed=True, facecolor="#2A2A2A", edgecolor=GRAY,
                         ls="--", lw=1.6))
    ax.plot(img[:, 0], img[:, 1], color=RED, lw=4, solid_capstyle="round")
    ax.scatter(img[:, 0], img[:, 1], color=RED, s=30, zorder=4)
    ax.text(1.05, 0.95, "unit square", color=GRAY, fontsize=10)
    ax.text(1.25, 0.35, "image collapses to a segment", color=RED, fontsize=10)
    ax.text(0.05, -0.45, "det B = 0, area = 0", color=RED, fontsize=12)
    ax.set_xlim(-0.4, 3.0); ax.set_ylim(-0.6, 2.9)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("det A = 0: the square collapses to a segment", fontsize=13)
    clean(ax)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L18_determinant_area.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L19
def fig_l19():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.2))
    ax = axes[0]
    A = np.array([[3.0, 1.0], [1.0, 3.0]])
    v1 = np.array([1.0, 1.0]); v2 = np.array([1.0, -1.0])
    ax.plot([-6, 6], [-6, 6], ls="--", color=GRAY, lw=1.0)
    ax.plot([-6, 6], [6, -6], ls="--", color=GRAY, lw=1.0)
    for v, lam, col, off, lab in [
            (v1, 4, BLUE, np.array([0.12, -0.55]), "$A v_1 = 4 v_1$"),
            (v2, 2, GREEN, np.array([-0.25, -0.62]), "$A v_2 = 2 v_2$")]:
        ax.add_patch(FancyArrowPatch((0, 0), v, arrowstyle="-|>", mutation_scale=16,
                                     color=col, lw=2.0, alpha=0.55))
        ax.add_patch(FancyArrowPatch((0, 0), lam * v, arrowstyle="-|>",
                                     mutation_scale=18, color=col, lw=2.8))
        ax.text(*(lam * v + off), lab, color=col, fontsize=12)
    u = np.array([1.0, 0.0]); Au = A @ u
    ax.add_patch(FancyArrowPatch((0, 0), u, arrowstyle="-|>", mutation_scale=16,
                                 color=ORANGE, lw=2.4))
    ax.add_patch(FancyArrowPatch((0, 0), Au, arrowstyle="-|>", mutation_scale=16,
                                 color=PURPLE, lw=2.4))
    ax.text(1.1, -0.35, "$u$", color=ORANGE, fontsize=12)
    ax.text(3.05, 1.05, "$Au$ is not parallel to $u$", color=PURPLE, fontsize=10)
    ax.set_xlim(-4.5, 4.8); ax.set_ylim(-4.5, 4.8)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Eigenvectors keep their direction;\nother vectors get rotated",
                 fontsize=13)
    clean(ax)

    ax = axes[1]
    A = np.array([[0.95, -0.30], [0.30, 0.95]])
    xs = [np.array([1.0, 0.0])]
    for _ in range(70):
        xs.append(A @ xs[-1])
    xs = np.array(xs)
    ax.plot(xs[:, 0], xs[:, 1], color=BLUE, lw=1.8)
    ax.scatter([xs[0, 0]], [xs[0, 1]], color=GREEN, s=45, zorder=4)
    ax.scatter([xs[-1, 0]], [xs[-1, 1]], color=RED, s=45, zorder=4)
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(th), np.sin(th), ls=":", color=GRAY, lw=1.0)
    ax.text(-1.32, 1.18, "orbit of $x_{k+1} = A x_k$", color=BLUE, fontsize=10)
    ax.text(-1.32, -1.42, "$\\lambda = 0.95 \\pm 0.30i$,\nno real eigenvector",
            fontsize=11)
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Complex eigenvalues: rotation plus scaling", fontsize=13)
    clean(ax)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L19_eigenvector_geometry.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L20
def fig_l20():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.4))
    A = np.array([[3.0, 1.0], [1.0, 3.0]])

    ax = axes[0]
    for i in np.arange(-3, 4):
        seg = np.array([[i, -3.0], [i, 3.0]]) @ A.T
        ax.plot(seg[:, 0], seg[:, 1], color=BLUE, lw=0.9, alpha=0.55)
        seg = np.array([[-3.0, i], [3.0, i]]) @ A.T
        ax.plot(seg[:, 0], seg[:, 1], color=BLUE, lw=0.9, alpha=0.55)
    ax.plot([-8, 8], [-8, 8], ls="--", color=RED, lw=1.6)
    ax.plot([-8, 8], [8, -8], ls="--", color=GREEN, lw=1.6)
    ax.text(5.0, 5.6, "eigen-direction $v_1$", color=RED, fontsize=10)
    ax.text(-7.9, 6.4, "eigen-direction $v_2$", color=GREEN, fontsize=10)
    ax.set_xlim(-8.5, 8.5); ax.set_ylim(-8.5, 8.5)
    ax.set_xlabel("x1"); ax.set_ylabel("x2")
    ax.set_title("Standard basis:\nA skews the square grid", fontsize=13)
    clean(ax)

    ax = axes[1]
    for i in np.arange(-2, 3):
        ax.plot([i, i], [-2.6, 2.6], ls=":", color=GRAY, lw=1.0, alpha=0.8)
        ax.plot([-2.6, 2.6], [i, i], ls=":", color=GRAY, lw=1.0, alpha=0.8)
    for i in np.arange(-1, 2):
        ax.plot([4 * i, 4 * i], [-6, 6], color=BLUE, lw=1.2, alpha=0.8)
        ax.plot([-6, 6], [2 * i, 2 * i], color=BLUE, lw=1.2, alpha=0.8)
    ax.add_patch(FancyArrowPatch((0, 0), (4, 0), arrowstyle="-|>", mutation_scale=18,
                                 color=RED, lw=2.6))
    ax.add_patch(FancyArrowPatch((0, 0), (0, 2), arrowstyle="-|>", mutation_scale=18,
                                 color=GREEN, lw=2.6))
    ax.text(4.15, -0.95, "$\\lambda_1 = 4$", color=RED, fontsize=12)
    ax.text(-1.1, 2.2, "$\\lambda_2 = 2$", color=GREEN, fontsize=12)
    handles = [Line2D([], [], ls=":", color=GRAY, lw=1.2, label="unit grid"),
               Line2D([], [], color=BLUE, lw=1.4, label="grid after scaling")]
    ax.legend(handles=handles, frameon=False, loc="lower left", fontsize=9)
    ax.set_xlim(-6.2, 6.2); ax.set_ylim(-6.2, 6.2)
    ax.set_xlabel("coordinate along $v_1$"); ax.set_ylabel("coordinate along $v_2$")
    ax.set_title("Eigenvector basis:\nA becomes pure scaling", fontsize=13)
    clean(ax)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L20_change_of_basis.png", dpi=200, bbox_inches="tight")
    plt.close(fig)



def fig_l12():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.2, 5.2),
                                  gridspec_kw={"width_ratios": [1.0, 1.0]})
    pos = {1: (0.0, 1.1), 2: (1.9, 1.1), 3: (1.9, -0.3), 4: (0.0, -0.3)}
    edges = [
        ("e1", 1, 2, True), ("e2", 2, 3, True), ("e3", 1, 3, False),
        ("e4", 1, 4, True), ("e5", 3, 4, False),
    ]
    for name, a, b, tree in edges:
        col = BLUE if tree else ORANGE
        ls = "-" if tree else (0, (4, 3))
        lw = 2.6 if tree else 2.2
        ax.add_patch(FancyArrowPatch(pos[a], pos[b], arrowstyle="-|>",
                                     mutation_scale=16, color=col, lw=lw,
                                     linestyle=ls, shrinkA=15, shrinkB=18,
                                     zorder=3))
        mx = (pos[a][0] + pos[b][0]) / 2
        my = (pos[a][1] + pos[b][1]) / 2
        dx = pos[b][0] - pos[a][0]
        dy = pos[b][1] - pos[a][1]
        L = np.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        off = 0.17
        ax.text(mx + nx * off, my + ny * off, name, color=col, fontsize=12,
                ha="center", va="center", fontweight="bold", zorder=5)
    for n, (x, y) in pos.items():
        ax.add_patch(plt.Circle((x, y), 0.17, facecolor=PANEL,
                                edgecolor=INK, lw=1.8, zorder=4))
        ax.text(x, y, str(n), fontsize=13, ha="center", va="center", zorder=5)
    ax.set_xlim(-0.6, 2.5)
    ax.set_ylim(-0.9, 1.65)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Graph: spanning tree (blue, solid) + extra edges (orange, dashed)",
                 fontsize=11.5)

    A = np.array([[-1, 1, 0, 0], [0, -1, 1, 0], [-1, 0, 1, 0],
                  [-1, 0, 0, 1], [0, 0, -1, 1]])
    cmap = {-1: "#5A2430", 1: "#1E3A2A", 0: PANEL}
    for i in range(5):
        for j in range(4):
            v = int(A[i, j])
            ax2.add_patch(plt.Rectangle((j, 4 - i), 1, 1, facecolor=cmap[v],
                                        edgecolor=GRID, lw=1.2))
            ax2.text(j + 0.5, 4 - i + 0.5, f"{v:+d}" if v else "0",
                     ha="center", va="center", fontsize=14,
                     color=RED if v < 0 else (GREEN if v > 0 else GRAY))
    for j in range(4):
        ax2.text(j + 0.5, 5.2, f"node {j + 1}", fontsize=10.5, ha="center")
    for i, name in enumerate(["e1", "e2", "e3", "e4", "e5"]):
        ax2.text(-0.12, 4 - i + 0.5, name, fontsize=12, ha="right",
                 va="center", fontweight="bold")
    ax2.text(2.0, 5.75, "Incidence matrix  $A$  (5 x 4)", fontsize=13,
             ha="center", fontweight="bold")
    ax2.text(2.0, -0.35, "$-1$ = tail, $+1$ = head", fontsize=11.5,
             ha="center", color=MUTED)
    ax2.set_xlim(-0.85, 4.2)
    ax2.set_ylim(-0.65, 6.05)
    ax2.set_aspect("equal")
    ax2.axis("off")
    fig.tight_layout()
    fig.savefig(f"{OUT}/L12_graph_incidence.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_l13():
    fig = plt.figure(figsize=(12.6, 5.6))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    dark3d(ax)
    u1 = np.array([1.0, 0.0, 0.30])
    u2 = np.array([0.0, 1.0, 0.45])
    s = np.linspace(-1.2, 1.2, 2)
    S, T = np.meshgrid(s, s)
    ax.plot_surface(S * u1[0] + T * u2[0], S * u1[1] + T * u2[1],
                    S * u1[2] + T * u2[2], color=BLUE, alpha=0.16,
                    linewidth=0, shade=False)
    for k in np.linspace(-1.2, 1.2, 5):
        ax.plot([k * u1[0], k * u1[0] + 1.2 * u2[0]],
                [k * u1[1], k * u1[1] + 1.2 * u2[1]],
                [k * u1[2], k * u1[2] + 1.2 * u2[2]], color=BLUE, lw=0.6, alpha=0.35)
        ax.plot([k * u2[0], k * u2[0] + 1.2 * u1[0]],
                [k * u2[1], k * u2[1] + 1.2 * u1[1]],
                [k * u2[2], k * u2[2] + 1.2 * u1[2]], color=BLUE, lw=0.6, alpha=0.35)
    n = np.cross(u1, u2)
    n = n / np.linalg.norm(n)
    b = np.array([0.65, 0.70, 1.30])
    p = b - (b @ n) / (n @ n) * n
    e = b - p

    ax.plot(*np.outer([-1.15, 1.15], n).T, color=GRAY, lw=1.6, ls=(0, (5, 4)))
    ax.quiver(0, 0, 0, *p, color=BLUE, lw=2.6, arrow_length_ratio=0.09)
    ax.quiver(0, 0, 0, *b, color=GREEN, lw=2.6, arrow_length_ratio=0.09)
    ax.quiver(*p, *e, color=ORANGE, lw=2.6, arrow_length_ratio=0.12)
    ax.scatter(*p, color=BLUE, s=35, zorder=5)
    ax.scatter(0, 0, 0, color=INK, s=25, zorder=5)

    a = 0.16
    ph = p / np.linalg.norm(p)
    eh = e / np.linalg.norm(e)
    c1 = p - a * ph
    c2 = p - a * ph - a * eh
    c3 = p - a * eh
    ax.plot([c1[0], c2[0], c3[0]], [c1[1], c2[1], c3[1]],
            [c1[2], c2[2], c3[2]], color=INK, lw=1.3)

    ax.text(*(p + np.array([0.02, 0.02, -0.22])), "$p$", color=BLUE, fontsize=14)
    ax.text(*(b + np.array([0.06, 0.06, 0.08])), "$b$", color=GREEN, fontsize=14)
    ax.text(*((p + b) / 2 + np.array([0.20, -0.16, 0.02])), "$e$", color=ORANGE, fontsize=14)
    ax.text(*(-0.85 * u1 + 0.85 * u2 + np.array([0.0, 0.0, 0.08])), "$V$", color=BLUE,
            fontsize=15, ha="center")
    ax.text(*(1.05 * n), "$V^{\perp}$", color=GRAY, fontsize=13)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)
    ax.set_axis_off()
    ax.view_init(elev=20, azim=-58)
    ax.set_title("Every $b$ splits into $p \in V$ plus $e \perp V$", fontsize=12)
    ax.text2D(0.5, 0.02, "dim $V$ + dim $V^{\perp}$ = dim $\mathbb{R}^3$",
              transform=ax.transAxes, ha="center", fontsize=11.5, color=MUTED)

    ax2 = fig.add_subplot(1, 2, 2)
    O = np.array([0.0, 0.0])
    P = np.array([1.5, 0.0])
    B = np.array([1.5, 1.05])
    ax2.add_patch(Polygon([O, P, B], closed=True, facecolor=BLUE,
                          alpha=0.10, edgecolor="none"))
    ax2.annotate("", xy=P, xytext=O, arrowprops=dict(arrowstyle="-|>", color=BLUE,
                                                     lw=2.6, mutation_scale=17))
    ax2.annotate("", xy=B, xytext=P, arrowprops=dict(arrowstyle="-|>", color=ORANGE,
                                                     lw=2.6, mutation_scale=17))
    ax2.annotate("", xy=B, xytext=O, arrowprops=dict(arrowstyle="-|>", color=GREEN,
                                                     lw=2.6, mutation_scale=17))
    ax2.plot([1.5, 1.36, 1.36], [0, 0, 0.14], color=INK, lw=1.4)
    ax2.text(0.72, -0.17, "$p$", color=BLUE, fontsize=15, ha="center")
    ax2.text(1.62, 0.55, "$e$", color=ORANGE, fontsize=15, va="center")
    ax2.text(0.66, 0.62, "$b$", color=GREEN, fontsize=15, ha="center")
    ax2.text(-0.10, -0.16, "$O$", fontsize=13)
    ax2.text(0.78, 1.22, "$b=p+e,\quad p\perp e$", fontsize=14, ha="center")
    ax2.text(0.78, -0.48, "$|b|^2=|p|^2+|e|^2$", fontsize=16, ha="center")
    ax2.set_xlim(-0.30, 1.95)
    ax2.set_ylim(-0.65, 1.40)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("Pythagoras: $|b|^2 = |p|^2 + |e|^2$", fontsize=12)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L13_orthogonal_complement.png", dpi=200, bbox_inches="tight")
    plt.close(fig)



def fig_l14_ls():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.4, 5.2))
    t = np.array([1.0, 2.0, 3.0])
    y = np.array([1.0, 2.0, 2.0])
    C, D = 2 / 3, 0.5
    tt = np.linspace(0.55, 3.45, 100)

    ax.plot(tt, C + D * tt, color=BLUE, lw=2.6, label=r"$y=C+Dt$")
    ax.scatter(t, y, color=RED, s=70, zorder=5, label="data $(t_i,y_i)$")
    for i, (ti, yi) in enumerate(zip(t, y)):
        yf = C + D * ti
        ax.plot([ti, ti], [yi, yf], color=ORANGE, lw=2.0, ls=(0, (4, 3)), zorder=3)
        ax.scatter([ti], [yf], color=BLUE, s=28, zorder=4)
        off = 0.07 if yi > yf else -0.07
        ax.text(ti + 0.06, (yi + yf) / 2 + off, f"$e_{i+1}$", color=ORANGE, fontsize=13)
    ax.text(1.45, 0.72, r"$E=\sum_i (C+Dt_i-y_i)^2$", fontsize=13, color=INK)
    ax.set_xlabel("$t$")
    ax.set_ylabel("$y$")
    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0.45, 2.55)
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    ax.set_title("Least squares: slide the line to minimize vertical errors", fontsize=12)
    clean(ax)

    Cg = np.linspace(-0.2, 1.5, 240)
    Dg = np.linspace(-0.35, 1.35, 240)
    CC, DD = np.meshgrid(Cg, Dg)
    E = ((CC + DD - 1) ** 2 + (CC + 2 * DD - 2) ** 2 + (CC + 3 * DD - 2) ** 2)
    cs = ax2.contour(CC, DD, E, levels=np.array([0.2, 0.5, 1, 2, 4, 7, 12, 20]),
                     cmap="viridis", linewidths=1.6)
    ax2.clabel(cs, inline=True, fontsize=8, fmt="%g")
    ax2.scatter([C], [D], marker="*", s=320, color=RED, zorder=5,
                edgecolor="white", linewidth=1.2)
    ax2.annotate("solution\n$(C,D)=(2/3,\\,1/2)$", xy=(C, D), xytext=(-0.08, 0.95),
                 fontsize=11, ha="left",
                 bbox=dict(boxstyle="round,pad=0.25", fc=PAPER, ec="none", alpha=0.9),
                 arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.4))
    ax2.set_xlabel("$C$ (intercept)")
    ax2.set_ylabel("$D$ (slope)")
    ax2.set_title("Level sets of $E$: a bowl whose bottom is the solution", fontsize=12)
    clean(ax2)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L14_least_squares_fit.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_l20_pca():
    rng = np.random.default_rng(7)
    Q = np.array([[np.cos(np.deg2rad(30)), -np.sin(np.deg2rad(30))],
                  [np.sin(np.deg2rad(30)), np.cos(np.deg2rad(30))]])
    lam = np.array([5.0, 0.6])
    L = Q @ np.diag(np.sqrt(lam))
    X = rng.normal(size=(240, 2)) @ L.T
    X = X - X.mean(axis=0)

    Cinv = X.T @ X / (len(X) - 1)
    w, V = np.linalg.eigh(Cinv)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]

    fig, (ax, ax3) = plt.subplots(1, 2, figsize=(12.8, 5.4),
                                  gridspec_kw={"width_ratios": [1.15, 1]})
    ax.scatter(X[:, 0], X[:, 1], s=16, color=GRAY, alpha=0.55, edgecolor="none")
    for k, (col, name) in enumerate([(RED, "$u_1$"), (BLUE, "$u_2$")]):
        vec = V[:, k] * 2.15 * np.sqrt(w[k])
        ax.annotate("", xy=vec, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.8, mutation_scale=18))
        ax.text(*(vec * 1.10), name, color=col, fontsize=15, ha="center", va="center")
    ax.scatter([0], [0], marker="x", s=70, color=INK, zorder=5)
    ax.text(0.12, 0.42, "mean", fontsize=10, color=INK,
            bbox=dict(boxstyle="round,pad=0.2", fc=PAPER, ec="none", alpha=0.85))
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title("Data cloud and its principal axes\n(arrow length $\\propto\\sqrt{\\lambda}$)", fontsize=12)
    clean(ax)

    p1 = X @ V[:, 0]
    p2 = X @ V[:, 1]
    bins = np.linspace(-6.0, 6.0, 26)
    ax3.hist(p1, bins=bins, density=True, color=RED, alpha=0.55,
             label=f"along $u_1$:  var = {w[0]:.2f}")
    ax3.hist(p2, bins=bins, density=True, color=BLUE, alpha=0.55,
             label=f"along $u_2$:  var = {w[1]:.2f}")
    ax3.set_xlabel("projection coordinate")
    ax3.set_ylabel("density")
    ax3.legend(loc="upper left", fontsize=10, frameon=False)
    ax3.set_title("Spread along each axis = eigenvalue", fontsize=12)
    ax3.text(0.02, 0.62, "$C u = \\lambda u$", transform=ax3.transAxes,
             fontsize=14, color=INK)
    clean(ax3, equal=False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L20_pca_principal_axes.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_l16_det():
    fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.9))
    cases = [
        ("shear", np.array([[1, 1], [0, 1]]), "det = 1   (area unchanged)",
         "property 5: adding a multiple of one row\nto another keeps the area"),
        ("swap", np.array([[0, 1], [1, 0]]), "det = -1   (same area, flipped)",
         "property 4: swapping two rows flips\nthe sign of the orientation"),
        ("scale", np.array([[3, 0], [0, 1]]), "det = 3   (area tripled)",
         "property 3: multiplying one row by 3\nmultiplies the area by 3"),
    ]
    for ax, (name, A, res, note) in zip(axes, cases):
        sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
        ax.add_patch(Polygon(sq, closed=True, fill=False, edgecolor=GRAY,
                             lw=1.6, ls=(0, (5, 4)), zorder=4))
        img = sq @ A.T
        col = {"shear": BLUE, "swap": PURPLE, "scale": GREEN}[name]
        ax.add_patch(Polygon(img, closed=True, facecolor=col, alpha=0.20,
                             edgecolor=col, lw=2.2, zorder=2))
        ax.annotate("", xy=img[1], xytext=(0, 0), zorder=3,
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2, mutation_scale=15))
        ax.annotate("", xy=img[3], xytext=(0, 0), zorder=3,
                    arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2, mutation_scale=15))
        v1, v2 = img[1], img[3]
        n1 = np.array([v1[1], -v1[0]]) / np.linalg.norm(v1) * 0.30 + v1 / np.linalg.norm(v1) * 0.12
        n2 = np.array([v2[1], -v2[0]]) / np.linalg.norm(v2) * 0.30 + v2 / np.linalg.norm(v2) * 0.12
        ax.text(*(v1 + n1), "$A e_1$", color=RED, fontsize=12,
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.15", fc=PAPER, ec="none", alpha=0.85))
        ax.text(*(v2 + n2), "$A e_2$", color=BLUE, fontsize=12,
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.15", fc=PAPER, ec="none", alpha=0.85))
        ax.text(0.52, 0.46, "unit square", fontsize=9.5, color=GRAY, ha="center",
                bbox=dict(boxstyle="round,pad=0.15", fc=PAPER, ec="none", alpha=0.8))
        ax.scatter([0], [0], color=INK, s=24, zorder=6)
        ax.set_xlim(-0.55, 3.45)
        ax.set_ylim(-0.60, 1.55)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(res, fontsize=12, pad=10)
        ax.text(0.5, -0.17, note, transform=ax.transAxes, ha="center",
                va="top", fontsize=9.5, color=MUTED)
    fig.suptitle("Determinant = area scale factor, sign = orientation", fontsize=14)
    fig.tight_layout(rect=[0, 0.03, 1, 0.93])
    fig.savefig(f"{OUT}/L16_determinant_properties.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_l21():
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 6.2))
    A = np.array([[-1.0, 2.0], [1.0, -2.0]])
    S = np.array([[2.0, 1.0], [1.0, -1.0]])
    Sinv = np.linalg.inv(S)
    lam = np.array([0.0, -3.0])

    def flow(u0, ts):
        e = np.stack([np.exp(lam[0] * ts), np.exp(lam[1] * ts)], axis=0)
        return (S @ (e * (Sinv @ u0).reshape(2, 1))).T

    ax = axes[0]
    xs = np.linspace(-2.4, 2.4, 11)
    X, Y = np.meshgrid(xs, xs)
    U = A[0, 0] * X + A[0, 1] * Y
    V = A[1, 0] * X + A[1, 1] * Y
    ax.quiver(X, Y, U, V, color=GRAY, alpha=0.50, angles="xy",
              scale_units="xy", scale=5.0, width=0.004)
    ts = np.linspace(0.0, 7.0, 400)
    starts = [(1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, -1.0),
              (1.8, 1.4), (-1.8, -1.4), (2.0, -1.0), (-1.4, 1.8)]
    for u0 in starts:
        tr = flow(np.array(u0), ts)
        ax.plot(tr[:, 0], tr[:, 1], color=BLUE, lw=1.3, alpha=0.8)
        ax.scatter(*u0, color=BLUE, s=14, zorder=5)
    ax.plot([-2.4, 2.4], [-1.2, 1.2], color=RED, lw=2.0)
    ax.plot([-2.0, 2.0], [2.0, -2.0], color=GREEN, lw=1.8, ls="--")
    ax.scatter([1.0], [0.0], color=INK, s=34, zorder=6)
    ax.text(1.08, -0.18, "$u(0)=(1,0)$", fontsize=9.5, color=INK)
    ax.text(1.95, 1.15, "steady direction\n$(2,1)^T$", color=RED, fontsize=10,
            ha="right", va="bottom")
    ax.text(-1.85, 1.82, "fast decay\n$(1,-1)^T$", color=GREEN, fontsize=10,
            ha="left", va="bottom")
    ax.scatter([2 / 3], [1 / 3], color=RED, s=28, zorder=6)
    ax.text(0.38, 0.18, "$(2/3,1/3)$", color=RED, fontsize=9.5, ha="right")
    ax.set_xlim(-2.4, 2.4); ax.set_ylim(-2.4, 2.4)
    ax.set_xlabel("$u_1$"); ax.set_ylabel("$u_2$")
    ax.set_title("Phase portrait: flow collapses onto the $\\lambda=0$ line", fontsize=12)
    clean(ax)

    ax = axes[1]
    ax.axvspan(-4.2, 0.0, color=BLUE, alpha=0.10)
    ax.axvspan(0.0, 2.4, color=RED, alpha=0.05)
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor=GREEN,
                        lw=1.8, ls="--"))
    pts = [(-3.0 + 6.0j, RED), (0.0 + 0.0j, RED), (-3.0 + 0.0j, RED),
           (0.8 + 0.0j, GREEN), (-0.5 + 0.8j, GREEN)]
    for z, c in pts:
        ax.scatter([z.real], [z.imag], color=c, s=42, zorder=6)
    ax.text(-2.85, 6.28, "$\\lambda=-3+6i$: $|e^{\\lambda t}|=e^{-3t}$",
            fontsize=9.5, color=RED, va="top")
    ax.text(-0.12, -0.55, "$\\lambda=0$\nsteady state", fontsize=9.0,
            color=RED, ha="right", va="top")
    ax.text(-3.0, -0.55, "$\\lambda=-3$", fontsize=9.0, color=RED,
            ha="center", va="top")
    ax.text(0.92, 0.18, "discrete stable\neigenvalues", fontsize=9.0,
            color=GREEN, ha="left", va="bottom")
    ax.text(0.35, 0.90, "|$\\lambda$|=1", fontsize=9.0, color=GREEN,
            ha="left", va="bottom")
    ax.axhline(0, color=MUTED, lw=1.0)
    ax.axvline(0, color=MUTED, lw=1.0)
    ax.text(-4.0, 3.2, "Re $\\lambda<0$", color=BLUE, fontsize=11)
    ax.text(0.12, 3.2, "Re $\\lambda>0$", color=RED, fontsize=11)
    handles = [Patch(facecolor=BLUE, alpha=0.18, label="continuous: Re $\\lambda<0$"),
               Line2D([], [], color=GREEN, ls="--", lw=1.6, label="discrete: |$\\lambda$|<1")]
    ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=9)
    ax.set_xlim(-4.2, 2.4); ax.set_ylim(-3.4, 6.6)
    ax.set_xlabel("Re $\\lambda$"); ax.set_ylabel("Im $\\lambda$")
    ax.set_title("$e^{At}$ stable on the left; $A^k$ stable inside the circle", fontsize=12)
    clean(ax)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L21_stability_phase.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_l12_adj():
    fig = plt.figure(figsize=(14.6, 4.7))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.15, 1.0, 1.0], wspace=0.28)

    ax = fig.add_subplot(gs[0, 0])
    pos = {1: (0.0, 1.35), 3: (1.35, 1.35), 2: (0.0, 0.0), 4: (1.35, 0.0)}
    comp = {1: BLUE, 3: BLUE, 2: ORANGE, 4: ORANGE}
    for (a, b) in [(1, 3), (3, 1), (2, 4), (4, 2)]:
        rad = 0.22 if a < b else -0.22
        ax.add_patch(FancyArrowPatch(pos[a], pos[b], arrowstyle="-|>",
                                     mutation_scale=14, color=GRAY, lw=1.3,
                                     connectionstyle=f"arc3,rad={rad}"))
    for (a, b) in [(1, 2), (3, 4)]:
        ax.add_patch(FancyArrowPatch(pos[a], pos[b], arrowstyle="-|>",
                                     mutation_scale=14, color=PURPLE, lw=1.6))
    for n, p in pos.items():
        ax.add_patch(Circle(p, 0.20, facecolor=comp[n], edgecolor="white",
                            lw=1.4, alpha=0.85, zorder=4))
        ax.text(p[0], p[1], str(n), color="white", ha="center", va="center",
                fontsize=11, fontweight="bold", zorder=5)
    ax.text(-0.42, 1.72, "SCC A: {1,3}", color=BLUE, fontsize=10)
    ax.text(1.12, -0.40, "SCC B: {2,4}", color=ORANGE, fontsize=10)
    ax.set_xlim(-0.65, 1.95); ax.set_ylim(-0.65, 1.95)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Directed graph: two SCCs, one-way bridge", fontsize=12)

    A = np.array([[0, 1, 1, 0], [0, 0, 0, 1],
                  [1, 0, 0, 1], [0, 1, 0, 0]], dtype=float)
    P = np.eye(4)[:, [0, 2, 1, 3]]
    B = P.T @ A @ P

    for k, (M, title) in enumerate([(A, "Adjacency matrix $A$\n(original labels)"),
                                    (B, "$P^T AP$\n(SCC order)")]):
        ax = fig.add_subplot(gs[0, k + 1])
        ax.imshow(M, cmap=LinearSegmentedColormap.from_list("darkblue", [PANEL, BLUE]), vmin=0, vmax=1.0)
        for i in range(4):
            for j in range(4):
                ax.text(j, i, int(M[i, j]), ha="center", va="center",
                        fontsize=11, color=PAPER if M[i, j] > 0.5 else MUTED)
        ax.set_xticks(range(4)); ax.set_yticks(range(4))
        ax.set_xticklabels(["1", "3", "2", "4"] if k == 1 else ["1", "2", "3", "4"])
        ax.set_yticklabels(["1", "3", "2", "4"] if k == 1 else ["1", "2", "3", "4"])
        ax.set_xlabel("to node"); ax.set_ylabel("from node")
        ax.set_title(title, fontsize=12)
        if k == 1:
            ax.add_patch(Rectangle((-0.5, -0.5), 2, 2, fill=False, ec=RED, lw=2.2))
            ax.add_patch(Rectangle((1.5, 1.5), 2, 2, fill=False, ec=RED, lw=2.2))
            ax.add_patch(Rectangle((-0.5, 1.5), 2, 2, fill=False, ec=GRAY,
                                   lw=1.6, ls="--"))
            ax.text(0.5, 2.5, "zero block", ha="center", va="center",
                    fontsize=9.5, color=GRAY)

    fig.suptitle("Matrices are graphs: relabeling nodes = permutation similarity", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig(f"{OUT}/L12_adjacency_scc.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- Markov chain (topic)
def fig_markov_chain():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.6, 5.2),
                                  gridspec_kw={"width_ratios": [1.0, 1.15]})

    A = np.array([0.0, 0.0]); B = np.array([2.2, 0.0]); r = 0.30

    for c, name in [(A, "A"), (B, "B")]:
        ax.add_patch(Circle(c, r, facecolor=PANEL, edgecolor=INK,
                            lw=2.0, zorder=4))
        ax.text(c[0], c[1], name, ha="center", va="center", fontsize=16, zorder=5)

    # self loops (arc over each node)
    for c, lab in [(A, "0.6"), (B, "0.8")]:
        ax.annotate("", xy=(c[0] + 0.20, c[1] + 0.36), xytext=(c[0] - 0.20, c[1] + 0.36),
                    arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.8",
                                    color=BLUE, lw=2.2, mutation_scale=15), zorder=6)
        ax.text(c[0], c[1] + 0.88, lab, ha="center", va="center", fontsize=12,
                color=BLUE)

    # cross edges: A -> B (top), B -> A (bottom)
    ax.add_patch(FancyArrowPatch(A + (r, 0.05), B - (r, 0.05), arrowstyle="-|>",
                                 mutation_scale=16, connectionstyle="arc3,rad=0.30",
                                 color=ORANGE, lw=2.4, zorder=3))
    ax.add_patch(FancyArrowPatch(B - (r, -0.05), A + (r, -0.05), arrowstyle="-|>",
                                 mutation_scale=16, connectionstyle="arc3,rad=-0.30",
                                 color=GREEN, lw=2.4, zorder=3))
    ax.text(1.10, 0.40, "0.4", ha="center", fontsize=12, color=ORANGE)
    ax.text(1.10, -0.46, "0.2", ha="center", fontsize=12, color=GREEN)
    ax.text(1.10, -0.98, "P = [[0.6, 0.2], [0.4, 0.8]]", ha="center", fontsize=11, color=INK)
    ax.set_xlim(-1.0, 3.4); ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("A 2-state Markov chain:\neach column of $P$ sums to 1", fontsize=12)

    P = np.array([[0.6, 0.2], [0.4, 0.8]])
    piA = 1 / 3
    k = np.arange(0, 16)
    for u0, col, lab in [([1.0, 0.0], RED, "start in A"),
                         ([0.0, 1.0], ORANGE, "start in B")]:
        u = np.array(u0, dtype=float)
        tr = []
        for _ in k:
            tr.append(u[0]); u = P @ u
        ax2.plot(k, tr, marker="o", ms=4, lw=1.8, color=col, label=lab)
    ax2.axhline(piA, color=GRAY, ls="--", lw=1.6)
    ax2.text(12.6, piA + 0.05, r"$\pi_A=\frac{1}{3}$ (stationary)", color=GRAY,
             fontsize=11, ha="right")
    ax2.set_xlabel("step $k$"); ax2.set_ylabel(r"$P(X_k=A)$")
    ax2.set_ylim(-0.06, 1.10)
    ax2.set_title("$u_k=P^k u_0\\to\\pi$ forgets the start\n"
                  "(rate set by $|\\lambda_2|=0.4$)", fontsize=12)
    ax2.legend(frameon=False, loc="center right")
    clean(ax2, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/markov_chain_convergence.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- Linear programming (topic)
def fig_linear_programming():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.4))

    x = np.linspace(-1.5, 26, 300)
    wood = 20 - x / 2          # x + 2y <= 40
    labor = 30 - 1.5 * x       # 3x + 2y <= 60
    poly = np.array([[0, 0], [20, 0], [10, 15], [0, 20]])

    # left: feasible region, corners, optimal objective line
    ax.add_patch(Polygon(poly, closed=True, facecolor=GRAY, alpha=0.20,
                         edgecolor="none", zorder=0))
    ax.plot(x, wood, color=BLUE, lw=2.2, label=r"$x+2y\leq40$  (wood)")
    ax.plot(x, labor, color=GREEN, lw=2.2, label=r"$3x+2y\leq60$  (labor)")
    for (xi, yi), lab, col in [
            ((0, 0), "(0, 0)   z = 0", INK),
            ((20, 0), "(20, 0)   z = 800", INK),
            ((0, 20), "(0, 20)   z = 1200", INK),
            ((10, 15), "(10, 15)   z = 1300", RED)]:
        ax.scatter([xi], [yi], color=col, s=55, zorder=6)
        dy = 1.6 if yi > 12 else -1.8
        ax.text(xi, yi + dy, lab, ha="center", fontsize=10.5, color=col,
                bbox=dict(boxstyle="round,pad=0.2", fc=PAPER, ec="none", alpha=0.85))
    ax.scatter([10], [15], marker="*", s=340, color=RED, zorder=7,
               edgecolor="white", lw=1.0)
    obj = 1300 / 60 - (2 / 3) * x
    ax.plot(x, obj, color=RED, ls="--", lw=1.8, zorder=5)
    ax.text(3.4, 1300 / 60 - (2 / 3) * 3.4 + 1.3, r"$40x+60y=1300$",
            color=RED, fontsize=11, rotation=-33.7, va="bottom", ha="left")
    g = np.array([40.0, 60.0]); g = g / np.linalg.norm(g)
    ax.add_patch(FancyArrowPatch((5, 3), (5 + 3.2 * g[0], 3 + 3.2 * g[1]),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=RED, lw=2.6, zorder=6))
    ax.text(5 + 3.5 * g[0], 3 + 3.5 * g[1], "increase\nprofit", color=RED,
            fontsize=10, ha="left", va="center")
    ax.set_xlim(-2, 26); ax.set_ylim(-2, 26)
    ax.set_xlabel("chairs $x$"); ax.set_ylabel("tables $y$")
    ax.set_title("Feasible region: optimum at a vertex\n(10 chairs, 15 tables $\\to$ $\\$1300)",
                 fontsize=12)
    ax.legend(frameon=False, loc="upper right")
    clean(ax)

    # right: the simplex walk from corner to corner
    ax2.add_patch(Polygon(poly, closed=True, facecolor=GRAY, alpha=0.18,
                          edgecolor="none", zorder=0))
    ax2.plot(x, wood, color=BLUE, lw=1.6, alpha=0.85)
    ax2.plot(x, labor, color=GREEN, lw=1.6, alpha=0.85)
    path = np.array([[0, 0], [0, 20], [10, 15]])
    ax2.plot(path[:, 0], path[:, 1], color=PURPLE, lw=2.6, zorder=4, alpha=0.9)
    for a, b in zip(path[:-1], path[1:]):
        ax2.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=20,
                                      color=PURPLE, lw=2.6, zorder=5,
                                      shrinkA=6, shrinkB=6))
    for i, (xi, yi) in enumerate(path):
        ax2.scatter([xi], [yi], color=PURPLE, s=70, zorder=6)
        ax2.text(xi + 0.8, yi + 0.8, ["$(0,0)$", "$(0,20)$", "$(10,15)$"][i],
                 fontsize=10.5, color=PURPLE)
    ax2.text(4.2, 7.5, "simplex walk:\ncorner $\\to$ corner", color=PURPLE, fontsize=11)
    ax2.set_xlim(-2, 26); ax2.set_ylim(-2, 26)
    ax2.set_xlabel("chairs $x$"); ax2.set_ylabel("tables $y$")
    ax2.set_title("Simplex visits 3 of 4 corners,\nstill finds the global optimum",
                  fontsize=12)
    clean(ax2)

    fig.tight_layout()
    fig.savefig(f"{OUT}/linear_programming_simplex.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- shared helpers
BLUE_L, GREEN_L, ORANGE_L, RED_L, GRAY_L = (
    "#16324A", "#173A24", "#3A2A16", "#3A1E1E", "#242424")


def draw_grid(ax, M, x0, y0, cell=0.5, title="", face=None, highlight=None,
              fontsize=11, show_zero=True):
    """Draw a small matrix as a labelled grid on a normal 2D axes."""
    M = np.asarray(M)
    n, m = M.shape
    for i in range(n):
        for j in range(m):
            y = y0 + (n - 1 - i) * cell
            fc = PANEL if face is None else face[i][j]
            ax.add_patch(Rectangle((x0 + j * cell, y), cell, cell,
                                   facecolor=fc, edgecolor="#4A4A5A", lw=1.0))
            v = M[i, j]
            if show_zero or v != 0:
                ax.text(x0 + (j + 0.5) * cell, y + cell / 2, f"{v:g}",
                        ha="center", va="center", fontsize=fontsize,
                        color=INK)
    if highlight:
        for (i, j, col) in highlight:
            ax.add_patch(Rectangle((x0 + j * cell, y0 + (n - 1 - i) * cell),
                                   cell, cell, fill=False, edgecolor=col,
                                   lw=2.2, zorder=5))
    if title:
        ax.text(x0 + m * cell / 2, y0 + n * cell + 0.12, title,
                ha="center", va="bottom", fontsize=11.5)


# ---------------------------------------------------------------- L2 elimination
def fig_l2():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.0),
                                  gridspec_kw={"width_ratios": [1.0, 1.2]})

    x = np.linspace(-0.6, 3.6, 200)
    ax.plot(x, (5 - x) / 2, color=BLUE, lw=2.2, label="row 1: $x+2y=5$")
    ax.plot(x, (11 - 3 * x) / 4, color=RED, lw=2.2, ls="--",
            label="row 2: $3x+4y=11$")
    ax.plot(x, 2 * np.ones_like(x), color=GREEN, lw=2.4, label="after: $y=2$")
    ax.scatter([1], [2], color=INK, s=65, zorder=6)
    ax.annotate("solution $(1,2)$\nunchanged", (1, 2), xytext=(1.55, 2.55),
                fontsize=11, arrowprops=dict(arrowstyle="-", color=GRAY, lw=1.0))
    ax.text(2.05, 1.80, "$E_{21}$: row2 $-\\ 3\\cdot$ row1",
            color=GREEN, fontsize=10.5)
    ax.set_xlim(-0.4, 3.7); ax.set_ylim(-0.6, 3.9)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Row picture: rewrite row 2,\nkeep the intersection",
                 fontsize=12.5)
    ax.legend(frameon=False, loc="upper right", fontsize=9.5)
    clean(ax)

    E = np.array([[1, 0], [-3, 1]])
    A = np.array([[1, 2], [3, 4]])
    U = np.array([[1, 2], [0, -2]])
    cell = 0.56
    fa = [[BLUE_L, BLUE_L], [BLUE_L, BLUE_L]]
    fe = [[GRAY_L, GRAY_L], [ORANGE_L, GRAY_L]]
    fu = [[BLUE_L, BLUE_L], [GRAY_L, BLUE_L]]
    draw_grid(ax2, E, 0.00, 0.55, cell, "$E_{21}$", fe,
              highlight=[(1, 0, ORANGE)])
    draw_grid(ax2, A, 1.50, 0.55, cell, "$A$", fa,
              highlight=[(0, 0, BLUE)])
    draw_grid(ax2, U, 3.00, 0.55, cell, "$U$", fu,
              highlight=[(0, 0, BLUE)])
    ax2.text(1.31, 0.55 + cell, "$\\times$", fontsize=18, ha="center",
             va="center")
    ax2.text(2.81, 0.55 + cell, "$=$", fontsize=18, ha="center", va="center")
    ax2.text(0.0, 0.02,
             "the multiplier $3$ is recorded for $L$ "
             "(sign flips: L = [[1, 0], [3, 1]])",
             fontsize=10.5)
    ax2.set_xlim(-0.15, 4.35); ax2.set_ylim(-0.1, 2.15)
    ax2.set_aspect("equal"); ax2.axis("off")
    ax2.set_title("Matrix view: left multiply = row operation",
                  fontsize=12.5, pad=14)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L2_elimination.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L3 multiplication
def fig_l3():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.0))

    col = np.array([[2], [3], [4]])
    row = np.array([[1, 6]])
    out = col @ row
    cell = 0.46
    draw_grid(ax, col, 0.00, 0.65, cell, "column",
              [[RED_L], [RED_L], [RED_L]], fontsize=12)
    draw_grid(ax, row, 0.80, 1.10, cell, "row",
              [[BLUE_L, BLUE_L]], fontsize=12)
    draw_grid(ax, out, 2.06, 0.65, cell, "rank-1 result",
              [[GREEN_L, GREEN_L], [GREEN_L, GREEN_L], [GREEN_L, GREEN_L]],
              fontsize=12)
    ax.text(0.63, 1.40, "$\\times$", fontsize=18, ha="center", va="center")
    ax.text(1.89, 1.40, "$=$", fontsize=18, ha="center", va="center")
    ax.text(0.0, 0.20,
            "$c_{ij}=u_i v_j$: every row is a multiple of the row vector",
            fontsize=10.5)
    ax.set_xlim(-0.10, 3.10); ax.set_ylim(0.0, 2.60)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Column times row = rank-1 matrix", fontsize=12.5)

    ax2.plot([-1.2, 4.2], [-2.4, 8.4], color=GRAY, lw=1.1, ls=":")
    c1 = np.array([1.0, 2.0]); c2 = np.array([3.0, 6.0])
    ax2.add_patch(FancyArrowPatch((0, 0), c1, arrowstyle="-|>",
                                 mutation_scale=16, color=BLUE, lw=2.4))
    ax2.add_patch(FancyArrowPatch((0, 0), c2, arrowstyle="-|>",
                                 mutation_scale=16, color=GREEN, lw=2.4))
    ax2.add_patch(FancyArrowPatch((0, 0), (3, -1), arrowstyle="-|>",
                                 mutation_scale=16, color=PURPLE, lw=2.2))
    ax2.text(0.75, 2.15, "$c_1=(1,2)$", color=BLUE, fontsize=11)
    ax2.text(3.05, 6.05, "$c_2=3\\,c_1$", color=GREEN, fontsize=11)
    ax2.text(3.05, -0.75, "$x=(3,-1)$", color=PURPLE, fontsize=11)
    ax2.text(-1.15, 4.7, "$C(A)$ is one line,\nnot $\\mathbb{R}^2$",
             fontsize=11)
    ax2.text(1.05, -1.85, "$A x=0$: a nonzero vector\nis crushed to the origin",
             color=PURPLE, fontsize=10.5)
    ax2.scatter([0], [0], color=INK, s=28, zorder=6)
    ax2.set_xlim(-1.4, 4.5); ax2.set_ylim(-2.4, 8.4)
    ax2.set_xlabel("x"); ax2.set_ylabel("y")
    ax2.set_title("Collinear columns: the plane collapses to a line",
                  fontsize=12.5)
    clean(ax2)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L3_multiplication_and_singular.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L4 LU
def fig_l4():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13.4, 4.9),
                                  gridspec_kw={"width_ratios": [1.55, 1.0]})

    A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
    L = np.array([[1, 0, 0], [3, 1, 0], [0, 2, 1]])
    U = np.array([[1, 2, 1], [0, 2, -2], [0, 0, 5]])
    cell = 0.5
    fa = [[BLUE_L] * 3 for _ in range(3)]
    fl = [[GRAY_L, GRAY_L, GRAY_L],
          [ORANGE_L, BLUE_L, GRAY_L],
          [GRAY_L, ORANGE_L, BLUE_L]]
    fu = [[BLUE_L, BLUE_L, BLUE_L],
          [GRAY_L, BLUE_L, BLUE_L],
          [GRAY_L, GRAY_L, BLUE_L]]
    draw_grid(ax, A, 0.00, 0.55, cell, "$A$", fa)
    draw_grid(ax, L, 1.85, 0.55, cell, "$L$: multipliers", fl,
              highlight=[(1, 0, ORANGE), (2, 1, ORANGE)])
    draw_grid(ax, U, 3.70, 0.55, cell, "$U$: pivots", fu,
              highlight=[(0, 0, BLUE), (1, 1, BLUE), (2, 2, BLUE)])
    ax.text(1.66, 0.55 + 0.75, "$=$", fontsize=18, ha="center", va="center")
    ax.text(3.51, 0.55 + 0.75, "$\\times$", fontsize=18, ha="center",
            va="center")
    ax.text(0.0, 0.02,
            "$LU=A$: multipliers $3,2$ go into $L$; pivots $1,2,5$ stay on $U$'s diagonal",
            fontsize=10.5)
    ax.set_xlim(-0.15, 5.25); ax.set_ylim(0.0, 2.20)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("The elimination ledger: $A=LU$", fontsize=12.5, pad=26)

    n = 200
    m = np.arange(1, 41)
    direct = m * n ** 3 / 3
    lu = n ** 3 / 3 + m * n ** 2
    ax2.plot(m, direct / 1e6, color=RED, lw=2.2,
             label="solve each $b$ from scratch")
    ax2.plot(m, lu / 1e6, color=BLUE, lw=2.2, label="factor $LU$ once")
    ax2.annotate("$m=40$: 25x fewer flops", xy=(40, lu[-1] / 1e6),
                 xytext=(22, 28), fontsize=10.5,
                 arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.2))
    ax2.set_xlabel("number of right-hand sides $m$")
    ax2.set_ylabel("floating-point operations (millions)")
    ax2.set_ylim(0, 118)
    ax2.set_title("$n=200$: factor once, solve many", fontsize=12.5)
    ax2.legend(frameon=False, loc="upper left", fontsize=9.5)
    clean(ax2, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L4_lu_structure.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L5 subspaces
def fig_l5():
    fig = plt.figure(figsize=(15.2, 4.9))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.0, 1.1], wspace=0.25)

    # (a) transpose
    ax = fig.add_subplot(gs[0, 0])
    A = np.array([[1, 2], [3, 4], [5, 6]])
    cell = 0.44
    draw_grid(ax, A, 0.00, 0.35, cell, "$A$",
              [[BLUE_L, BLUE_L], [BLUE_L, BLUE_L], [BLUE_L, BLUE_L]])
    draw_grid(ax, A.T, 1.28, 0.35, cell, "$A^{T}$",
              [[GREEN_L, GREEN_L, GREEN_L], [GREEN_L, GREEN_L, GREEN_L]])
    ax.add_patch(Rectangle((0.0 + cell, 0.35 + 2 * cell), cell, cell,
                           fill=False, ec=RED, lw=2.2, zorder=5))
    ax.add_patch(Rectangle((1.28, 0.35), cell, cell,
                           fill=False, ec=RED, lw=2.2, zorder=5))
    ax.annotate("", xy=(1.18, 1.05), xytext=(1.02, 1.05),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4))
    ax.text(0.0, 0.10, "$a_{ij}\\to a_{ji}$: rows become columns",
            fontsize=10.5)
    ax.set_xlim(-0.10, 2.75); ax.set_ylim(0.0, 2.05)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Transpose: flip across the diagonal", fontsize=12.5)

    # (b) subspaces of R^2
    ax = fig.add_subplot(gs[0, 1])
    ax.add_patch(Rectangle((-3, -3), 6, 6, facecolor=BLUE_L, alpha=0.55,
                           edgecolor="none", zorder=0))
    xx = np.linspace(-3, 3, 2)
    ax.plot(xx, 0 * xx, color=GRAY, lw=2.0)
    ax.plot(xx, xx, color=GREEN, lw=2.0)
    ax.plot(xx, -0.6 * xx, color=ORANGE, lw=2.0)
    ax.plot(xx, xx + 1.8, color=RED, lw=2.0, ls="--")
    ax.scatter([0], [0], color=INK, s=32, zorder=6)
    ax.text(-2.75, 2.35, "all of $\\mathbb{R}^2$", fontsize=10.5,
            color=BLUE)
    ax.text(1.65, -2.25, "lines\nthrough 0", fontsize=10.5, color=GREEN)
    ax.text(0.12, -2.65, "$\\{0\\}$", fontsize=10.5)
    ax.text(-2.85, -2.55, "offset line:\nnot a subspace", fontsize=10.5,
            color=RED)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("$\\mathbb{R}^2$: three kinds of subspaces", fontsize=12.5)
    clean(ax)

    # (c) column space in R^3
    ax = fig.add_subplot(gs[0, 2], projection="3d")
    dark3d(ax)
    c1 = np.array([1.0, 2.0, 4.0]); c2 = np.array([3.0, 3.0, 1.0])
    s, t = np.meshgrid(np.linspace(-0.70, 0.80, 2),
                       np.linspace(-0.70, 0.80, 2))
    X = s * c1[0] + t * c2[0]
    Y = s * c1[1] + t * c2[1]
    Z = s * c1[2] + t * c2[2]
    ax.plot_surface(X, Y, Z, color=BLUE, alpha=0.38, linewidth=0)
    for vec, col, lab in [(c1, BLUE, "$c_1$"), (c2, GREEN, "$c_2$")]:
        ax.quiver(0, 0, 0, *vec, color=col, lw=2.4, arrow_length_ratio=0.10)
    b = 0.35 * c1 + 0.45 * c2
    n = np.cross(c1, c2); n = n / np.linalg.norm(n)
    bout = b + 1.25 * n
    ax.quiver(0, 0, 0, *b, color=RED, lw=2.4, arrow_length_ratio=0.10)
    ax.quiver(0, 0, 0, *bout, color=PURPLE, lw=2.2, arrow_length_ratio=0.10)
    ax.plot([b[0], bout[0]], [b[1], bout[1]], [b[2], bout[2]],
            color=PURPLE, ls="--", lw=1.2, alpha=0.8)
    ax.text2D(0.03, 0.12, "$C(A)$: plane through 0", color=BLUE,
              fontsize=10, transform=ax.transAxes)
    ax.text2D(0.54, 0.70, "$b\\in C(A)$\n$Ax=b$ solvable", color=RED,
              fontsize=10, transform=ax.transAxes)
    ax.text2D(0.58, 0.40, "$b_{out}\\notin C(A)$\nno solution", color=PURPLE,
              fontsize=10, transform=ax.transAxes)
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5); ax.set_zlim(-1, 5)
    ax.view_init(elev=20, azim=-58)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.set_xlabel(""); ax.set_ylabel(""); ax.set_zlabel("")
    ax.grid(False)
    ax.set_title("Column space $C(A)\\subset\\mathbb{R}^3$", fontsize=12.5)

    fig.savefig(f"{OUT}/L5_subspaces.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L5 transpose geometry
def fig_l5_transpose():
    A = np.array([[1.0, 1.0], [0.0, 1.0]])
    x = np.array([0.0, 2.0])
    v = np.array([1.0, 1.0])
    Ax, Av = A @ x, A @ v

    fig = plt.figure(figsize=(13.0, 10.4))
    gs = fig.add_gridspec(2, 2, wspace=0.22, hspace=0.30)

    def arrows(ax, pairs):
        for vec, col, ls, lab, off in pairs:
            ax.add_patch(FancyArrowPatch(
                (0, 0), vec, arrowstyle="-|>", mutation_scale=16,
                color=col, lw=2.4, linestyle=ls, alpha=0.95))
            ax.text(vec[0] + off[0], vec[1] + off[1], lab, color=col,
                    fontsize=11)

    # (a) shear changes the dot product
    ax = fig.add_subplot(gs[0, 0])
    arrows(ax, [(x, BLUE, "-", "$x$", (-0.34, 0.06)),
                (v, GREEN, "-", "$v$", (0.08, 0.06)),
                (Ax, BLUE, "--", "$Ax$", (0.08, -0.28)),
                (Av, GREEN, "--", "$Av$", (0.08, 0.10))])
    ax.plot([x[0], v[0]], [x[1], v[1]], color=GRAY, ls=":", lw=1.1)
    ax.plot([Ax[0], Av[0]], [Ax[1], Av[1]], color=GRAY, ls=":", lw=1.1)
    ax.text(0.05, 2.62, "$x\\cdot v = 2$", color=INK, fontsize=12)
    ax.text(1.45, 2.55, "$(Ax)\\cdot(Av) = 6$", color=RED, fontsize=12)
    ax.text(0.02, -0.62, "a shear changes lengths and angles",
            color=GRAY, fontsize=10.5)
    ax.set_xlim(-0.55, 3.05); ax.set_ylim(-0.85, 2.95)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("(a) Shear: dot product is not preserved", fontsize=12.5)
    clean(ax)

    # (b) A^T pairs the output vector back with the input
    ax = fig.add_subplot(gs[0, 1])
    vbar = np.array([1.0, 0.0])
    v_back = A.T @ vbar
    arrows(ax, [(x, BLUE, "-", "$x$", (-0.34, 0.06)),
                (v_back, GREEN, "-", "$v=A^{T}\\bar v$", (0.10, 0.06)),
                (Ax, BLUE, "--", "$Ax$", (0.08, -0.28)),
                (vbar, ORANGE, "--", "$\\bar v$", (0.08, 0.08))])
    ax.text(0.05, 2.62, "input: $x\\cdot v = 2$", color=INK,
            fontsize=11.5)
    ax.text(1.35, 2.62, "output: $Ax\\cdot\\bar v = 2$", color=RED,
            fontsize=11.5)
    ax.text(0.02, -0.62, "$v=A^{T}\\bar v$ moves $\\bar v$ back to the input side",
            color=GRAY, fontsize=10.0)
    ax.set_xlim(-0.55, 3.05); ax.set_ylim(-0.85, 2.95)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("(b) $A^{T}$ restores the same dot product", fontsize=12.5)
    clean(ax)

    # (c) orthogonal matrix preserves the dot product
    ax = fig.add_subplot(gs[1, 0])
    Q = np.array([[0.0, -1.0], [1.0, 0.0]])
    x2 = np.array([1.0, 2.0]); v2 = np.array([3.0, -1.0])
    Qx, Qv = Q @ x2, Q @ v2
    arrows(ax, [(x2, BLUE, "-", "$x$", (0.08, 0.10)),
                (v2, GREEN, "-", "$v$", (0.08, -0.26)),
                (Qx, BLUE, "--", "$Qx$", (-0.52, 0.04)),
                (Qv, GREEN, "--", "$Qv$", (0.08, 0.10))])
    ax.text(-3.55, 2.95, "$x\\cdot v = Qx\\cdot Qv = 1$", fontsize=11.5)
    ax.text(-3.55, 2.55, "$Q^{T}Q=I$, so $Q^{T}=Q^{-1}$", color=PURPLE,
            fontsize=11)
    ax.text(-3.55, -3.15, "rotations and reflections keep lengths and angles",
            color=GRAY, fontsize=10.2)
    ax.set_xlim(-3.8, 3.6); ax.set_ylim(-3.4, 3.3)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("(c) Orthogonal $Q$: dot product is preserved", fontsize=12.5)
    clean(ax)

    # (d) SVD view: transpose reverses both rotations
    ax = fig.add_subplot(gs[1, 1])
    th = np.linspace(0, 2 * np.pi, 400)
    circ = np.vstack([np.cos(th), np.sin(th)])
    ell = A @ circ
    ax.plot(circ[0], circ[1], color=GRAY, lw=1.6, ls="--")
    ax.plot(ell[0], ell[1], color=BLUE, lw=2.6)
    ax.text(-1.62, -1.35, "unit circle", color=GRAY, fontsize=9.5)
    ax.text(0.55, -1.28, "$A$ applied", color=BLUE, fontsize=9.5)
    U, S, Vt = np.linalg.svd(A)
    V = Vt.T
    for col, lab, off in [
            (V[:, 0], "$v_1$", (0.08, 0.08)),
            (V[:, 1], "$v_2$", (-0.55, 0.05))]:
        ax.add_patch(FancyArrowPatch(
            (0, 0), col, arrowstyle="-|>", mutation_scale=12,
            color=GREEN, lw=1.4, ls="--", alpha=0.75))
        ax.text(col[0] + off[0], col[1] + off[1], lab, color=GREEN,
                fontsize=10)
    for i, col in enumerate((RED, ORANGE)):
        vec = U[:, i] * S[i]
        ax.add_patch(FancyArrowPatch(
            (0, 0), vec, arrowstyle="-|>", mutation_scale=14,
            color=col, lw=2.4))
    ax.text(0.02, 0.97, "$A=R_1\\Sigma R_2^{T}$\n$A^{T}=R_2\\Sigma R_1^{T}$",
            transform=ax.transAxes, va="top", fontsize=11.5)
    ax.text(0.02, 0.03, "transpose: reverse both rotations, keep $\\Sigma$",
            transform=ax.transAxes, fontsize=9.5, color=GRAY)
    ax.set_xlim(-1.9, 2.1); ax.set_ylim(-1.9, 1.9)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("(d) SVD: $A^{T}$ reverses the rotations", fontsize=12.5)
    clean(ax)

    fig.savefig(f"{OUT}/L5_transpose_dot_product.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L22 Markov
def fig_l22_markov():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.2),
                                  gridspec_kw={"width_ratios": [1.0, 1.12]})
    A = np.array([0.0, 0.0]); B = np.array([2.5, 0.0]); r = 0.38
    for c, name in [(A, "CA"), (B, "MA")]:
        ax.add_patch(Circle(c, r, facecolor=PANEL, edgecolor=INK,
                            lw=2.0, zorder=4))
        ax.text(c[0], c[1], name, ha="center", va="center", fontsize=14,
                zorder=5)
    for c, lab in [(A, "0.9"), (B, "0.8")]:
        ax.annotate("", xy=(c[0] + 0.22, c[1] + 0.44),
                    xytext=(c[0] - 0.22, c[1] + 0.44),
                    arrowprops=dict(arrowstyle="-|>",
                                    connectionstyle="arc3,rad=0.8",
                                    color=BLUE, lw=2.2, mutation_scale=15),
                    zorder=6)
        ax.text(c[0], c[1] + 0.98, lab, ha="center", fontsize=12, color=BLUE)
    ax.add_patch(FancyArrowPatch(A + (r, 0.05), B - (r, 0.05),
                                 arrowstyle="-|>", mutation_scale=16,
                                 connectionstyle="arc3,rad=0.30",
                                 color=ORANGE, lw=2.4, zorder=3))
    ax.add_patch(FancyArrowPatch(B - (r, -0.05), A + (r, -0.05),
                                 arrowstyle="-|>", mutation_scale=16,
                                 connectionstyle="arc3,rad=-0.30",
                                 color=GREEN, lw=2.4, zorder=3))
    ax.text(1.25, 0.42, "0.1", ha="center", fontsize=12, color=ORANGE)
    ax.text(1.25, -0.50, "0.2", ha="center", fontsize=12, color=GREEN)
    ax.text(1.25, -1.18, "A = [[0.9, 0.2], [0.1, 0.8]]",
            ha="center", fontsize=11)
    ax.set_xlim(-1.0, 3.7); ax.set_ylim(-1.65, 1.55)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("California $\\leftrightarrow$ Massachusetts:\ncolumns sum to 1",
                 fontsize=12.5)

    k = np.arange(0, 31)
    ca = 2000 / 3 - 2000 / 3 * 0.7 ** k
    ma = 1000 / 3 + 2000 / 3 * 0.7 ** k
    ax2.plot(k, ca, color=BLUE, lw=2.2, label="California")
    ax2.plot(k, ma, color=ORANGE, lw=2.2, label="Massachusetts")
    ax2.axhline(2000 / 3, color=BLUE, ls="--", lw=1.2, alpha=0.7)
    ax2.axhline(1000 / 3, color=ORANGE, ls="--", lw=1.2, alpha=0.7)
    ax2.text(23.5, 2000 / 3 + 28, "$2000/3$", color=BLUE, fontsize=10.5)
    ax2.text(23.5, 1000 / 3 - 62, "$1000/3$", color=ORANGE, fontsize=10.5)
    ax2.set_xlabel("year $k$"); ax2.set_ylabel("people (start: 1000 in MA)")
    ax2.set_ylim(-30, 1080)
    ax2.set_title("$u_k\\to\\pi$ at rate $|\\lambda_2|=0.7$", fontsize=12.5)
    ax2.legend(frameon=False, loc="center right")
    clean(ax2, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L22_markov_stationary.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L22 Fourier
def fig_l22_fourier():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.0),
                                  gridspec_kw={"width_ratios": [1.25, 1.0]})

    x = np.linspace(-np.pi, np.pi, 1200)
    sq = np.sign(np.sin(x))
    ax.plot(x, sq, color=GRAY, lw=2.0, ls="--", label="square wave")
    for N, col, lab in [(1, RED, "$N=1$ term"),
                        (3, BLUE, "$N=3$ terms"),
                        (9, GREEN, "$N=9$ terms")]:
        s = np.zeros_like(x)
        for k in range(1, N + 1, 2):
            s += (4 / (np.pi * k)) * np.sin(k * x)
        ax.plot(x, s, color=col, lw=1.9, label=lab)
    ax.set_xlim(-np.pi, np.pi); ax.set_ylim(-1.65, 1.65)
    ax.set_xticks([-np.pi, 0, np.pi])
    ax.set_xticklabels(["$-\\pi$", "0", "$\\pi$"])
    ax.set_xlabel("x"); ax.set_ylabel("$f(x)$")
    ax.set_title("Odd sine harmonics build a square wave", fontsize=12.5)
    ax.legend(frameon=False, loc="lower right", fontsize=9, ncol=2)
    clean(ax, equal=False)

    n = np.arange(1, 20, 2)
    b = 4 / (np.pi * n)
    ax2.vlines(n, 0, b, color=BLUE, lw=1.8)
    ax2.scatter(n, b, color=BLUE, s=28, zorder=4)
    ax2.plot(n, b, color=GRAY, ls=":", lw=1.2)
    ax2.set_xlabel("harmonic $n$ (odd)")
    ax2.set_ylabel("coefficient $b_n$")
    ax2.set_xticks(n)
    ax2.set_title("Coefficients decay like $1/n$", fontsize=12.5)
    ax2.text(8.5, 0.78, "slow decay at a jump\n$\\Rightarrow$ Gibbs ripple",
             fontsize=10.5)
    ax2.set_ylim(0, 1.45)
    clean(ax2, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L22_fourier.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L23 spectral
def fig_l23():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.2))

    t = np.linspace(0, 2 * np.pi, 400)
    circle = np.vstack([np.cos(t), np.sin(t)])
    A = np.array([[3.0, 1.0], [1.0, 3.0]])
    ellipse = A @ circle
    ax.plot(circle[0], circle[1], color=GRAY, ls="--", lw=1.5,
            label="unit circle")
    ax.plot(ellipse[0], ellipse[1], color=BLUE, lw=2.4, label="image under $A$")
    q1 = np.array([1.0, 1.0]) / np.sqrt(2)
    q2 = np.array([-1.0, 1.0]) / np.sqrt(2)
    for vec, lam, col in [(q1, 4.0, RED), (q2, 2.0, GREEN)]:
        ax.add_patch(FancyArrowPatch((0, 0), lam * vec, arrowstyle="-|>",
                                     mutation_scale=17, color=col, lw=2.4))
        p = lam * vec * 1.06
        ax.text(p[0], p[1], f"$\\lambda={lam:g}$", color=col, fontsize=11,
                ha="left" if p[0] > 0 else "right",
                va="bottom" if p[1] > 0 else "top")
    ax.scatter([0], [0], color=INK, s=25, zorder=6)
    ax.set_xlim(-4.7, 4.7); ax.set_ylim(-4.7, 4.7)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Symmetric $A$: orthogonal axes,\nreal stretches",
                 fontsize=12.5)
    ax.legend(frameon=False, loc="lower right", fontsize=9.5)
    clean(ax)

    x = np.array([1.6, 0.3])
    p1 = (x @ q1) * q1
    p2 = (x @ q2) * q2
    Ax = 4 * p1 + 2 * p2
    for vec, col, lw, lab, off in [
            (x, INK, 2.4, "$x$", (0.10, 0.10)),
            (p1, RED, 1.6, "$p_1$", (-0.34, 0.08)),
            (p2, GREEN, 1.6, "$p_2$", (0.08, -0.30)),
            (4 * p1, RED, 2.6, "$4p_1$", (0.12, 0.10)),
            (2 * p2, GREEN, 2.6, "$2p_2$", (0.10, -0.30)),
            (Ax, PURPLE, 2.8, "$Ax$", (0.10, 0.12))]:
        ax2.add_patch(FancyArrowPatch((0, 0), vec, arrowstyle="-|>",
                                      mutation_scale=16, color=col, lw=lw))
        ax2.text(vec[0] + off[0], vec[1] + off[1], lab, color=col,
                 fontsize=11)
    ax2.plot([4 * p1[0], Ax[0]], [4 * p1[1], Ax[1]], color=GRAY, ls="--",
             lw=1.1)
    ax2.plot([2 * p2[0], Ax[0]], [2 * p2[1], Ax[1]], color=GRAY, ls="--",
             lw=1.1)
    ax2.scatter([0], [0], color=INK, s=25, zorder=6)
    ax2.set_xlim(-1.0, 6.2); ax2.set_ylim(-2.6, 5.2)
    ax2.set_xlabel("x1"); ax2.set_ylabel("x2")
    ax2.set_title("Project on orthogonal axes,\nstretch by $\\lambda_i$, add",
                  fontsize=12.5)
    clean(ax2)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L23_spectral_axes.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L24 roots / FFT
def fig_l24():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.2))

    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=GRAY, ls="--", lw=1.4)
    n = 8
    for k in range(n):
        th = 2 * np.pi * k / n
        x, y = np.cos(th), np.sin(th)
        col = RED if k % 2 == 0 else BLUE
        ax.plot([0, x], [0, y], color=col, lw=1.1, alpha=0.55)
        ax.scatter([x], [y], color=col, s=55, zorder=5)
        ax.text(1.15 * x, 1.15 * y, f"$W^{k}$", color=col,
                fontsize=11, ha="center", va="center")
    ax.text(0, 0, "$W=e^{2\\pi i/n}$", fontsize=10.5, ha="center",
            va="center",
            bbox=dict(facecolor=PANEL, edgecolor="none", pad=1.5))
    ax.set_xlim(-1.38, 1.38); ax.set_ylim(-1.38, 1.38)
    ax.set_xlabel("Re"); ax.set_ylabel("Im")
    ax.set_title("Eighth roots of unity: columns of $F_8$",
                 fontsize=12.5)
    clean(ax)

    ns = np.array([16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
    ax2.loglog(ns, ns ** 2, color=RED, lw=2.2, label="$n^2$")
    ax2.loglog(ns, 0.5 * ns * np.log2(ns), color=BLUE, lw=2.2,
               label="$(n/2)\\log_2 n$")
    ax2.scatter([1024], [1024 ** 2], color=RED, s=35, zorder=5)
    ax2.scatter([1024], [0.5 * 1024 * 10], color=BLUE, s=35, zorder=5)
    ax2.annotate("n=1024: 1,048,576", (1024, 1024 ** 2),
                 xytext=(45, 1.4e6), fontsize=9.5, color=RED)
    ax2.annotate("n=1024: 5,120", (1024, 5120),
                 xytext=(1220, 2200), fontsize=9.5, color=BLUE,
                 arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8,
                                 alpha=0.6))
    ax2.set_xlabel("n"); ax2.set_ylabel("multiplications")
    ax2.set_title("FFT: divide and conquer wins", fontsize=12.5)
    ax2.legend(frameon=False, loc="upper left")
    clean(ax2, equal=False)

    fig.tight_layout()
    fig.savefig(f"{OUT}/L24_roots_fft.png", dpi=200, bbox_inches="tight")
    plt.close(fig)



def cell_grid(ax, M, x0, y0, cell=0.55, face=None, fs=12, fmt="{:.0f}"):
    M = np.asarray(M)
    n, m = M.shape
    for i in range(n):
        for j in range(m):
            y = y0 + (n - 1 - i) * cell
            fc = PANEL if face is None else face[i][j]
            ax.add_patch(Rectangle((x0 + j * cell, y), cell, cell,
                                   facecolor=fc, edgecolor="#4A4A5A", lw=1.1))
            lab = fmt(M[i, j]) if callable(fmt) else fmt.format(M[i, j])
            ax.text(x0 + (j + 0.5) * cell, y + cell / 2, lab,
                    ha="center", va="center", color=INK, fontsize=fs)


# ---------------------------------------------------------------- L7
def fig_l7():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.8),
                                  gridspec_kw={"width_ratios": [1.45, 1]})
    U = np.array([[1, 2, 0, -2], [0, 0, 1, 2], [0, 0, 0, 0]])
    face = [[PANEL] * 4 for _ in range(3)]
    for i, j in [(0, 0), (1, 2)]:
        face[i][j] = BLUE_L
    for i in range(3):
        for j in (1, 3):
            if face[i][j] == PANEL:
                face[i][j] = ORANGE_L
    ax.set_xlim(0, 5.1); ax.set_ylim(0, 4.4); ax.axis("off")
    cell_grid(ax, U, 0.55, 0.85, cell=0.72, face=face, fs=15)
    for j in range(4):
        ax.text(0.55 + (j + 0.5) * 0.72, 3.45, f"$x_{j+1}$",
                ha="center", va="center", fontsize=13)
    ax.text(0.30, 1.21, "$U$", ha="right", va="center", fontsize=15)
    ax.text(2.25, 3.82, "pivot columns 1, 3:  $r=2$", color=BLUE, ha="center", fontsize=12)
    ax.text(2.25, 0.30, "free columns 2, 4:  $n-r=2$", color=ORANGE, ha="center", fontsize=12)
    ax.text(0.55, 4.12, "Elimination keeps $N(A)$ unchanged", fontsize=12)

    s = np.array([[-2, 2], [1, 0], [0, -2], [0, 1]])
    face2 = [[PANEL] * 2 for _ in range(4)]
    ax2.set_xlim(0, 3.1); ax2.set_ylim(0, 4.4); ax2.axis("off")
    cell_grid(ax2, s, 0.55, 0.85, cell=0.62, face=face2, fs=13)
    ax2.text(0.55 + 0.31, 3.35, "$s_1$", ha="center", fontsize=13, color=BLUE)
    ax2.text(0.55 + 0.93, 3.35, "$s_2$", ha="center", fontsize=13, color=BLUE)
    ax2.text(1.55, 0.35, "$N(A)=\\mathrm{span}\\{s_1,s_2\\}$,  $\\dim N=n-r=2$",
             ha="center", fontsize=12)
    ax2.text(1.55, 3.88, "free variables set to 1 in turn", ha="center",
             fontsize=10.5, color=MUTED)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L7_pivots_nullspace.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L8
def fig_l8():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.9),
                                  gridspec_kw={"width_ratios": [1.1, 1]})
    t = np.linspace(-2.2, 2.8, 200)
    ax.plot(t, t, color=BLUE, lw=2.2, label="$N(A)$: through the origin")
    ax.plot(t, t + 1.4, color=ORANGE, lw=2.2, ls="--",
            label="$x_p+N(A)$: the solution set")
    ax.scatter([0], [0], color=BLUE, s=55, zorder=5)
    ax.scatter([0.4], [1.8], color=ORANGE, s=70, zorder=5)
    ax.annotate("$x_p$", (0.4, 1.8), xytext=(0.55, 2.35), fontsize=13,
                color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.0))
    ax.annotate("$0$", (0, 0), xytext=(-0.28, -0.28), fontsize=12, color=BLUE)
    ax.annotate("", xy=(1.65, 3.05), xytext=(0.4, 1.8),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.2))
    ax.text(1.75, 3.12, "$+\\,x_n$", color=GREEN, fontsize=13)
    ax.set_xlim(-2.2, 3.0); ax.set_ylim(-1.8, 3.6)
    ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$")
    ax.set_title("Solutions are $x_p$ plus the nullspace:\na parallel copy of $N(A)$",
                 fontsize=12.5)
    ax.legend(frameon=False, loc="lower right", fontsize=10)
    clean(ax)

    xp = np.array([[-2], [0], [1.5], [0]])
    s = np.array([[-2, 2], [1, 0], [0, -2], [0, 1]])
    M = np.hstack([xp, s])
    face = [[ORANGE_L, BLUE_L, BLUE_L] for _ in range(4)]
    ax2.set_xlim(0, 3.4); ax2.set_ylim(0, 4.4); ax2.axis("off")
    cell_grid(ax2, M, 0.45, 0.85, cell=0.62, face=face, fs=12,
              fmt=lambda v: f"{v:g}")
    ax2.text(0.45 + 0.31, 3.35, "$x_p$", ha="center", fontsize=13, color=ORANGE)
    ax2.text(0.45 + 0.93, 3.35, "$s_1$", ha="center", fontsize=13, color=BLUE)
    ax2.text(0.45 + 1.55, 3.35, "$s_2$", ha="center", fontsize=13, color=BLUE)
    ax2.text(1.55, 0.35, "$x=x_p+c_1s_1+c_2s_2$", ha="center", fontsize=13)
    ax2.text(0.45, 4.08, "Read $x_p$ and $N(A)$ off one RREF", fontsize=12)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L8_affine_solution_set.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L9
def fig_l9():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.9))
    u = np.array([1.4, 1.0]); v = np.array([1.0, -1.2])

    def arrow(ax, p, color, label, off=(0.08, 0.08), ls="-"):
        ax.add_patch(FancyArrowPatch((0, 0), p, arrowstyle="-|>", mutation_scale=18,
                                     color=color, lw=2.4, linestyle=ls))
        ax.text(p[0] + off[0], p[1] + off[1], label, color=color, fontsize=12)

    # (a) two independent directions fill the plane
    for c in np.linspace(-3, 3, 13):
        p0 = c * u
        ax.plot([p0[0] - 3 * v[0], p0[0] + 3 * v[0]],
                [p0[1] - 3 * v[1], p0[1] + 3 * v[1]],
                color=BLUE, alpha=0.16, lw=0.8, zorder=1)
        p1 = c * v
        ax.plot([p1[0] - 3 * u[0], p1[0] + 3 * u[0]],
                [p1[1] - 3 * u[1], p1[1] + 3 * u[1]],
                color=BLUE, alpha=0.16, lw=0.8, zorder=1)
    arrow(ax, u, BLUE, "$u$")
    arrow(ax, v, GREEN, "$v$")
    ax.set_title("Independent: $u,v$ reach every point of the plane", fontsize=12)
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6)
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$"); clean(ax)

    # (b) dependent: c = a + b
    a = np.array([1.4, 1.0]); b = np.array([1.0, -1.2]); c = a + b
    arrow(ax2, a, BLUE, "$a$")
    arrow(ax2, b, GREEN, "$b$")
    arrow(ax2, c, ORANGE, "$c=a+b$", off=(0.06, 0.12), ls="--")
    ax2.plot([a[0], c[0]], [a[1], c[1]], ls=":", color=GRAY, lw=1.2)
    ax2.plot([b[0], c[0]], [b[1], c[1]], ls=":", color=GRAY, lw=1.2)
    ax2.set_title("Dependent: the third vector adds no direction", fontsize=12)
    ax2.set_xlim(-0.6, 3.0); ax2.set_ylim(-1.8, 2.4)
    ax2.set_xlabel("$x$"); ax2.set_ylabel("$y$"); clean(ax2)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L9_span_basis.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L11
def fig_l11():
    fig, ax = plt.subplots(figsize=(13.0, 4.6))
    u = np.array([[1], [2], [3]])
    v = np.array([[1, 4, 5]])
    A = u @ v
    ax.set_xlim(0, 8.0); ax.set_ylim(0, 3.5); ax.axis("off")
    cell_grid(ax, u, 0.35, 0.75, cell=0.6, face=[[BLUE_L]] * 3, fs=14)
    cell_grid(ax, v, 1.9, 1.35, cell=0.6, face=[[BLUE_L] * 3], fs=14)
    cell_grid(ax, A, 4.5, 0.75, cell=0.6,
              face=[[BLUE_L] * 3 for _ in range(3)], fs=13)
    ax.text(0.95, 2.95, "$u$", ha="center", fontsize=15, color=BLUE)
    ax.text(2.8, 2.95, "$v^{\\mathrm{T}}$", ha="center", fontsize=15, color=BLUE)
    ax.text(5.4, 2.95, "$A=uv^{\\mathrm{T}}$  (rank 1)",
            ha="center", fontsize=14, color=BLUE)
    ax.text(1.5, 1.62, "$\\times$", ha="center", va="center", fontsize=26, color=MUTED)
    ax.text(4.15, 1.62, "$=$", ha="center", va="center", fontsize=26, color=MUTED)
    ax.text(5.4, 0.35, "each column of $A$ is a multiple of $u$",
            ha="center", fontsize=11.5, color=MUTED)
    ax.text(5.4, 3.30, "Every rank-$r$ matrix is a sum of $r$ rank-1 pieces",
            ha="center", fontsize=12.5, color=INK)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L11_rank_one_outer_product.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- L17
def fig_l17():
    fig, ax = plt.subplots(figsize=(11.8, 4.6))
    ax.axis("off")
    V = np.array([["$a_{11}$", "$a_{12}$", "$a_{13}$", "$a_{11}$", "$a_{12}$"],
                  ["$a_{21}$", "$a_{22}$", "$a_{23}$", "$a_{21}$", "$a_{22}$"],
                  ["$a_{31}$", "$a_{32}$", "$a_{33}$", "$a_{31}$", "$a_{32}$"]],
                 dtype=object)
    cell = 0.9
    for i in range(3):
        for j in range(5):
            fc = PANEL if j < 3 else "#1A1A1A"
            ax.add_patch(Rectangle((j * cell, (2 - i) * cell), cell, cell,
                                   facecolor=fc, edgecolor="#4A4A5A", lw=1.1))
            ax.text((j + 0.5) * cell, (2 - i) * cell + cell / 2, V[i, j],
                    ha="center", va="center", fontsize=13)
    pos = [(0, 0, 1, 1, 2, 2), (0, 1, 1, 2, 2, 3), (0, 2, 1, 3, 2, 4)]
    neg = [(0, 2, 1, 1, 2, 0), (0, 3, 1, 2, 2, 1), (0, 4, 1, 3, 2, 2)]
    for (r0, c0, r1, c1, r2, c2) in pos:
        ax.plot([(c0 + .5) * cell, (c1 + .5) * cell, (c2 + .5) * cell],
                [(2 - r0 + .5) * cell, (2 - r1 + .5) * cell, (2 - r2 + .5) * cell],
                color=BLUE, lw=2.4, alpha=0.85)
    for (r0, c0, r1, c1, r2, c2) in neg:
        ax.plot([(c0 + .5) * cell, (c1 + .5) * cell, (c2 + .5) * cell],
                [(2 - r0 + .5) * cell, (2 - r1 + .5) * cell, (2 - r2 + .5) * cell],
                color=RED, lw=2.4, ls="--", alpha=0.85)
    ax.set_xlim(-0.3, 5.4); ax.set_ylim(-0.9, 3.3)
    ax.text(2.25, 3.10, "Sarrus: 3 forward diagonals (blue) minus 3 backward (red)",
            ha="center", fontsize=12.5, color=INK)
    ax.text(2.25, -0.55, "$+\;a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}"
            "\;-\;(a_{13}a_{22}a_{31}+a_{11}a_{23}a_{32}+a_{12}a_{21}a_{33})$",
            ha="center", fontsize=11.5, color=INK)
    ax.text(5.15, 1.35, "6 terms", fontsize=12, color=MUTED, ha="left")
    fig.tight_layout()
    fig.savefig(f"{OUT}/L17_sarrus_rule.png", dpi=200, bbox_inches="tight")
    plt.close(fig)



DARK_CMAP = LinearSegmentedColormap.from_list(
    "darkpurple", ["#3A3568", "#6D5BD0", "#C4B5FD"])
DIV_CMAP = LinearSegmentedColormap.from_list("darkdiv", [BLUE, PANEL, RED])


def fig_l25_pd_vs_saddle():
    fig = plt.figure(figsize=(12.8, 5.6))
    X, Y = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-2, 2, 60))
    cases = [((2, 6, 20), "Positive definite: upward bowl (minimum at origin)"),
             ((2, 6, 7), "Indefinite: saddle point (saddle at origin)")]
    for k, ((a, b, c), title) in enumerate(cases):
        ax = fig.add_subplot(1, 2, k + 1, projection="3d")
        dark3d(ax)
        Z = a * X ** 2 + 2 * b * X * Y + c * Y ** 2
        ax.plot_surface(X, Y, Z, cmap=DARK_CMAP, linewidth=0,
                        antialiased=True, rstride=1, cstride=1, shade=False)
        ax.contour(X, Y, Z, zdir="z", offset=Z.min() - 0.18 * (Z.max() - Z.min()),
                   levels=8, colors=[BLUE, GREEN, ORANGE, PURPLE, RED,
                                     MUTED, BLUE, GREEN], linewidths=1.0)
        ax.scatter([0], [0], [0], color=ORANGE, s=35, depthshade=False)
        ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("f(x, y)")
        ax.set_title(title, fontsize=12)
        ax.view_init(elev=26, azim=-60)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L25_positive_definite_vs_saddle.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_l25_energy():
    fig, ax = plt.subplots(figsize=(9.8, 5.3))
    t = np.linspace(-1.6, 1.6, 400)
    ax.axhline(0, color=MUTED, lw=0.9)
    ax.plot(t, (7 - 18) * t ** 2, color=RED, lw=2.6,
            label="c = 7  (indefinite)")
    ax.plot(t, np.zeros_like(t), color=ORANGE, lw=2.8, ls="--",
            label="c = 18  (positive semidefinite)")
    ax.plot(t, (20 - 18) * t ** 2, color=GREEN, lw=2.6,
            label="c = 20  (positive definite)")
    ax.set_xlabel("t along d = (3, -1)")
    ax.set_ylabel("$d^{\\mathrm{T}}Ad\\cdot t^2$")
    ax.set_title("Energy along the critical direction", fontsize=13)
    ax.set_ylim(-30, 6)
    ax.legend(frameon=False, loc="lower center")
    clean(ax, equal=False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L25_energy_along_critical_direction.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_l25_levels():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.3))
    gl = np.linspace(-5.5, 5.5, 800)
    GLX, GLY = np.meshgrid(gl, gl)
    g = np.linspace(-2.6, 2.6, 500)
    GX, GY = np.meshgrid(g, g)

    ax = axes[0]
    A = np.array([[2.0, 6.0], [6.0, 20.0]])
    Z = A[0, 0] * GLX ** 2 + 2 * A[0, 1] * GLX * GLY + A[1, 1] * GLY ** 2
    lv = [0.4, 0.8, 1.5, 2.5, 4.5]
    ax.contour(GLX, GLY, Z, levels=lv,
               colors=[BLUE, GREEN, ORANGE, PURPLE, RED],
               linewidths=1.6)
    w, V = np.linalg.eigh(A)
    for lam, vec, col, lab in zip(w, V.T, [RED, BLUE],
                                  ["v1 (small eigenvalue)", "v2 (large eigenvalue)"]):
        L = 1 / np.sqrt(lam)
        ax.annotate("", xy=vec * L, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.4))
        ax.plot([], [], color=col, lw=2.4, label=lab)
    ax.scatter([0], [0], color=INK, s=28, zorder=5)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Positive definite: level sets are ellipses", fontsize=12.5)
    ax.legend(frameon=False, loc="lower right")
    ax.set_xlim(-5.5, 5.5); ax.set_ylim(-5.5, 5.5)
    clean(ax)

    ax = axes[1]
    A = np.array([[2.0, 6.0], [6.0, 7.0]])
    Z = A[0, 0] * GX ** 2 + 2 * A[0, 1] * GX * GY + A[1, 1] * GY ** 2
    ax.contour(GX, GY, Z, levels=[-16, -9, -4, -1, 1, 4, 9, 16],
               cmap=DIV_CMAP, linewidths=1.6)
    ax.contour(GX, GY, Z, levels=[0], colors=[MUTED], linestyles="--",
               linewidths=1.3)
    w, V = np.linalg.eigh(A)
    for lam, vec in zip(w, V.T):
        ax.plot([-2.4 * vec[0], 2.4 * vec[0]],
                [-2.4 * vec[1], 2.4 * vec[1]],
                color=GRAY, ls=":", lw=1.3)
    ax.scatter([0], [0], color=RED, s=45, zorder=5)
    ax.text(0.10, 0.10, "saddle", color=RED, fontsize=11)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Indefinite: level sets are hyperbolas", fontsize=12.5)
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6)
    clean(ax)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L25_level_sets_and_principal_axes.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


def fig_l14_probability():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.4))

    w0, w1 = 0.75, 0.485
    x = np.linspace(0.5, 3.5, 200)
    ax.plot(x, w0 + w1 * x, color=BLUE, lw=2.4, label="$y = w^{\\mathrm{T}}x$")
    xo = np.array([1.0, 2.0, 3.0])
    yo = w0 + w1 * xo + np.array([0.12, -0.35, 0.28])
    ax.scatter(xo, yo, color=RED, s=70, zorder=5, label="observations")
    for xi, yi in zip(xo, yo):
        ax.plot([xi, xi], [w0 + w1 * xi, yi], color=ORANGE, ls="--", lw=1.6)
    ax.set_xlim(0.5, 3.5); ax.set_ylim(0.5, 2.6)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Noise model: $\\varepsilon\\sim\\mathcal{N}(0,\\sigma^2)$",
                 fontsize=12.5)
    ax.legend(frameon=False, loc="upper left")
    clean(ax, equal=False)

    ins = ax.inset_axes([0.58, 0.09, 0.37, 0.30])
    e = np.linspace(-3.5, 3.5, 200)
    p = np.exp(-e ** 2 / 2)
    ins.plot(e, p, color=PURPLE, lw=1.8)
    ins.fill_between(e, p, color=PURPLE, alpha=0.25)
    ins.axvline(0.8, color=ORANGE, ls="--", lw=1.2)
    ins.set_title("$p(e)\\propto e^{-e^2/2\\sigma^2}$", fontsize=9.5)
    ins.set_xticks([-3, 0, 3]); ins.set_yticks([])
    ins.set_facecolor(PAPER)
    for sp in ("top", "right"):
        ins.spines[sp].set_visible(False)
    ins.tick_params(labelsize=8, colors=MUTED)

    Q = np.array([[0.22, 0.08], [0.08, 0.30]])
    c = np.array([2.5, 1.6])
    gx = np.linspace(-2.4, 3.2, 500); gy = np.linspace(-2.1, 2.4, 500)
    GX, GY = np.meshgrid(gx, gy)
    D = np.stack([GX - c[0], GY - c[1]], axis=-1)
    R = np.einsum("...i,ij,...j->...", D, Q, D)
    lv = [0.3, 0.7, 1.2, 2.0, 3.0, 4.5]
    ax2.contour(GX, GY, R, levels=lv, colors=[GRID] * len(lv), linewidths=1.1)

    th = np.linspace(0, 2 * np.pi, 400)
    ax2.plot(np.cos(th), np.sin(th), color=BLUE, lw=2.2, label="$L_2$: $||w||=1$")
    dia = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]])
    ax2.plot(dia[:, 0], dia[:, 1], color=ORANGE, lw=2.2,
             label="$L_1$: $|w_1|+|w_2|=1$")

    verts = np.array([[1.0, 0.0], [0.0, 1.0], [-1.0, 0.0], [0.0, -1.0]])
    Rv = np.einsum("...i,ij,...j->...", verts - c, Q, verts - c)
    wl1 = verts[np.argmin(Rv)]
    lev1 = Rv.min()

    circ = np.stack([np.cos(th), np.sin(th)], axis=1)
    Rc = np.einsum("...i,ij,...j->...", circ - c, Q, circ - c)
    wl2 = circ[np.argmin(Rc)]
    lev2 = Rc.min()

    ax2.contour(GX, GY, R, levels=[lev1], colors=[INK], linewidths=1.8)
    ax2.contour(GX, GY, R, levels=[lev2], colors=[INK], linewidths=1.8,
                linestyles="--")

    ax2.scatter(*c, marker="*", s=190, color=GREEN, zorder=6)
    ax2.text(c[0] + 0.10, c[1] + 0.08, "OLS", color=GREEN, fontsize=11)
    ax2.scatter(*wl1, color=ORANGE, s=70, zorder=6)
    ax2.text(wl1[0] + 0.12, wl1[1] - 0.18, "$w_{L1}$", color=ORANGE, fontsize=11)
    ax2.scatter(*wl2, color=BLUE, s=70, zorder=6)
    ax2.text(wl2[0] + 0.10, wl2[1] + 0.14, "$w_{L2}$", color=BLUE, fontsize=11)
    ax2.set_xlim(-2.4, 3.2); ax2.set_ylim(-2.1, 2.4)
    ax2.set_xlabel("$w_1$"); ax2.set_ylabel("$w_2$")
    ax2.set_title("Regularization geometry:\nequal RSS contours, different constraints",
                  fontsize=12)
    ax2.legend(frameon=False, loc="upper right")
    ax2.text(-2.3, -2.0, "L1 prefers a vertex: one weight becomes 0\n"
             "L2 shrinks both weights, none exactly 0",
             fontsize=10, color=MUTED, va="bottom")
    clean(ax2)
    fig.tight_layout()
    fig.savefig(f"{OUT}/L14_probability_regularization.png", dpi=200,
                bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_l1, fig_l10, fig_l14, fig_l15, fig_l18, fig_l19, fig_l20,
               fig_l12, fig_l13, fig_l14_ls, fig_l20_pca, fig_l16_det,
               fig_l21, fig_l12_adj, fig_markov_chain, fig_linear_programming,
               fig_l2, fig_l3, fig_l4, fig_l5, fig_l5_transpose,
               fig_l22_markov, fig_l22_fourier, fig_l23, fig_l24,
               fig_l7, fig_l8, fig_l9, fig_l11, fig_l17,
               fig_l25_pd_vs_saddle, fig_l25_energy, fig_l25_levels,
               fig_l14_probability):
        fn()
        print("ok", fn.__name__)
