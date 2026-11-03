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

OUT = "/mnt/c/X/STD/STD/Math/Linear Algebra/STDY/assets"
RED, BLUE, GREEN, ORANGE, PURPLE, GRAY = (
    "#d62728", "#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", "#7f7f7f")


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
    ax.scatter([1], [2], color="black", s=60, zorder=5)
    ax.annotate("solution (1, 2)", (1, 2), textcoords="offset points",
                xytext=(12, 20), fontsize=11)
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
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
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
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
    s, t = np.meshgrid(np.linspace(-1.3, 1.3, 2), np.linspace(-1.3, 1.3, 2))
    ax.plot_surface(s, t, 0 * s, color="#9ecae1", alpha=0.45, linewidth=0)
    ax.plot([0, 0], [0, 0], [-1.5, 1.5], color=RED, lw=3)
    d = 0.25
    ax.plot([0, d, d, 0], [0, 0, 0, 0], [d, d, 0, 0], color="black", lw=1.2)
    ax.scatter([0], [0], [0], color="black", s=25)
    ax.text2D(0.58, 0.78, "row space = span(v)\ndim 1", color=RED, fontsize=10,
              transform=ax.transAxes)
    ax.text2D(0.04, 0.38, "null space = plane v.x = 0\ndim 2", color="#08519c",
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
            [d * u1[1], d * (u1[1] + u2[1]), d * u2[1]], color="black", lw=1.2)
    ax.text(1.45, 2.1, "column space\n(Ax), dim 1", color=GREEN, fontsize=10)
    ax.text(-3.45, -2.1, "left null space\n(A^T y = 0), dim 1", color=PURPLE,
            fontsize=10)
    ax.scatter([0], [0], color="black", s=25, zorder=5)
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

    a1 = np.array([1.0, 0.0, 0.35]); a2 = np.array([0.0, 1.0, 0.55])
    b = np.array([1.2, 1.2, -0.6])
    n = np.cross(a1, a2)
    p = b - (b @ n) / (n @ n) * n
    s, t = np.meshgrid(np.linspace(-1.15, 1.15, 2), np.linspace(-1.15, 1.15, 2))
    X = s * a1[0] + t * a2[0]; Y = s * a1[1] + t * a2[1]; Z = s * a1[2] + t * a2[2]
    ax.plot_surface(X, Y, Z, color="#9ecae1", alpha=0.4, linewidth=0)
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
            color="black", lw=1.2)
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
    ax.scatter([proj[0]], [proj[1]], color="black", s=25, zorder=5)
    ax.add_patch(FancyArrowPatch(proj, a2, arrowstyle="-|>", mutation_scale=16,
                                 color=GREEN, lw=2.2))
    ax.text(0.95, 1.35, "$e = a_2 - \\mathrm{proj}$", color=GREEN, fontsize=11)
    ax.text(proj[0] + 0.1, proj[1] - 0.25, "proj", color="black", fontsize=10)
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
            [d * q1[1], d * (q1[1] + q2[1]), d * q2[1]], color="black", lw=1.2)
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
    ax.add_patch(Polygon(sq, closed=True, facecolor="#d9d9d9", edgecolor=GRAY,
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
    ax.add_patch(Polygon(sq, closed=True, facecolor="#d9d9d9", edgecolor=GRAY,
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
        ax.add_patch(plt.Circle((x, y), 0.17, facecolor="white",
                                edgecolor="#333333", lw=1.8, zorder=4))
        ax.text(x, y, str(n), fontsize=13, ha="center", va="center", zorder=5)
    ax.set_xlim(-0.6, 2.5)
    ax.set_ylim(-0.9, 1.65)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Graph: spanning tree (blue, solid) + extra edges (orange, dashed)",
                 fontsize=11.5)

    A = np.array([[-1, 1, 0, 0], [0, -1, 1, 0], [-1, 0, 1, 0],
                  [-1, 0, 0, 1], [0, 0, -1, 1]])
    cmap = {-1: "#f7c6c2", 1: "#c8e6c9", 0: "#ffffff"}
    for i in range(5):
        for j in range(4):
            v = int(A[i, j])
            ax2.add_patch(plt.Rectangle((j, 4 - i), 1, 1, facecolor=cmap[v],
                                        edgecolor="#999999", lw=1.2))
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
             ha="center", color="#444444")
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
    ax.scatter(0, 0, 0, color="#333333", s=25, zorder=5)

    a = 0.16
    ph = p / np.linalg.norm(p)
    eh = e / np.linalg.norm(e)
    c1 = p - a * ph
    c2 = p - a * ph - a * eh
    c3 = p - a * eh
    ax.plot([c1[0], c2[0], c3[0]], [c1[1], c2[1], c3[1]],
            [c1[2], c2[2], c3[2]], color="#333333", lw=1.3)

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
              transform=ax.transAxes, ha="center", fontsize=11.5, color="#444444")

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
    ax2.plot([1.5, 1.36, 1.36], [0, 0, 0.14], color="#333333", lw=1.4)
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
    ax.text(1.45, 0.72, r"$E=\sum_i (C+Dt_i-y_i)^2$", fontsize=13, color="#333333")
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
                 bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9),
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
    ax.scatter([0], [0], marker="x", s=70, color="#333333", zorder=5)
    ax.text(0.12, 0.42, "mean", fontsize=10, color="#333333",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
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
             fontsize=14, color="#333333")
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
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))
        ax.text(*(v2 + n2), "$A e_2$", color=BLUE, fontsize=12,
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))
        ax.text(0.52, 0.46, "unit square", fontsize=9.5, color=GRAY, ha="center",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8))
        ax.scatter([0], [0], color="#333333", s=24, zorder=6)
        ax.set_xlim(-0.55, 3.45)
        ax.set_ylim(-0.60, 1.55)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(res, fontsize=12, pad=10)
        ax.text(0.5, -0.17, note, transform=ax.transAxes, ha="center",
                va="top", fontsize=9.5, color="#444444")
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
    ax.scatter([1.0], [0.0], color="#222222", s=34, zorder=6)
    ax.text(1.08, -0.18, "$u(0)=(1,0)$", fontsize=9.5, color="#222222")
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
    ax.axhline(0, color="#444444", lw=1.0)
    ax.axvline(0, color="#444444", lw=1.0)
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
        ax.imshow(M, cmap="Blues", vmin=0, vmax=1.0)
        for i in range(4):
            for j in range(4):
                ax.text(j, i, int(M[i, j]), ha="center", va="center",
                        fontsize=11, color="white" if M[i, j] > 0.5 else "#333333")
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
        ax.add_patch(Circle(c, r, facecolor="white", edgecolor="#333333",
                            lw=2.0, zorder=4))
        ax.text(c[0], c[1], name, ha="center", va="center", fontsize=16, zorder=5)

    # self loops (arc over each node)
    for c, lab in [(A, "0.6"), (B, "0.8")]:
        ax.annotate("", xy=(c[0] + 0.16, c[1] + 0.12), xytext=(c[0] - 0.16, c[1] + 0.12),
                    arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.7",
                                    color=BLUE, lw=2.2, mutation_scale=15), zorder=3)
        ax.text(c[0], c[1] + 0.66, lab, ha="center", va="center", fontsize=12,
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
    ax.text(1.10, -0.98, "P = [[0.6, 0.2], [0.4, 0.8]]", ha="center", fontsize=11, color="#333333")
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
    ax2.set_title(r"$u_k=P^k u_0\to\pi$ forgets the start\n(rate set by $|\lambda_2|=0.4$)",
                  fontsize=12)
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
            ((0, 0), "(0, 0)   z = 0", "#333333"),
            ((20, 0), "(20, 0)   z = 800", "#333333"),
            ((0, 20), "(0, 20)   z = 1200", "#333333"),
            ((10, 15), "(10, 15)   z = 1300", RED)]:
        ax.scatter([xi], [yi], color=col, s=55, zorder=6)
        dy = 1.6 if yi > 12 else -1.8
        ax.text(xi, yi + dy, lab, ha="center", fontsize=10.5, color=col,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
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


for fn in (fig_l1, fig_l10, fig_l14, fig_l15, fig_l18, fig_l19, fig_l20,
           fig_l12, fig_l13, fig_l14_ls, fig_l20_pca, fig_l16_det,
           fig_l21, fig_l12_adj, fig_markov_chain, fig_linear_programming):
    fn()
    print("ok", fn.__name__)
