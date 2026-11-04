"""Animate A, A^{-1}, A^{-T}, A^{T} through their SVD stages.

Render:
  manim -qh four_svd_transforms.py FourSVDTransforms

The four panels share the same matrix A = [[1, 1], [0, 1]]:
  A      = R1  Sigma       R2^T
  A^-1   = R2  Sigma^-1    R1^T
  A^-T   = R1  Sigma^-1    R2^T
  A^T    = R2  Sigma       R1^T
Each stage is applied to a marked unit circle; rotations keep the circle,
the middle scaling turns it into an ellipse, and the final rotation orients it.
"""
import numpy as np
from manim import (
    Scene, VGroup, Circle, Line, Text, SurroundingRectangle,
    FadeIn, FadeOut, Write, Transform, ApplyMatrix, smooth, DOWN, UP,
    config,
)

config.frame_width = 16.0
config.frame_height = 9.0

# Same palette as the note figures (works on a white background).
RED = "#d62728"
BLUE = "#1f77b4"
GREEN = "#2ca02c"
ORANGE = "#ff7f0e"
PURPLE = "#9467bd"
GRAY = "#7f7f7f"
INK = "#222222"

A = np.array([[1.0, 1.0], [0.0, 1.0]])
U, S, Vt = np.linalg.svd(A)
R1 = U
R2 = Vt.T
SIGMA = np.diag(S)
SIGMA_INV = np.diag(1.0 / S)

CENTERS = [
    np.array([-3.5, 1.85, 0.0]),   # A
    np.array([3.5, 1.85, 0.0]),    # A^-1
    np.array([-3.5, -1.85, 0.0]),  # A^-T
    np.array([3.5, -1.85, 0.0]),   # A^T
]
PANEL_LABELS = [
    Text("A", font="DejaVu Sans", font_size=38, color=INK),
    Text("A⁻¹", font="DejaVu Sans", font_size=38, color=INK),
    Text("A⁻ᵀ", font="DejaVu Sans", font_size=38, color=INK),
    Text("Aᵀ", font="DejaVu Sans", font_size=38, color=INK),
]


SCALE = 0.88


def make_content(center):
    """Marked unit circle: gray boundary, red x-diameter, green y-diameter."""
    circle = Circle(radius=1.0, color=GRAY, stroke_width=2.4)
    red = Line([-1.0, 0.0, 0.0], [1.0, 0.0, 0.0], color=RED, stroke_width=3.2)
    green = Line([0.0, -1.0, 0.0], [0.0, 1.0, 0.0], color=GREEN, stroke_width=3.2)
    return VGroup(circle, red, green).scale(SCALE).move_to(center)


class FourSVDTransforms(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"

        title = Text(
            "A = [[1,1],[0,1]]: four paths",
            font="DejaVu Sans", font_size=30, color=INK,
        ).to_edge(UP, buff=0.30)
        self.play(Write(title), run_time=1.2)

        contents = [make_content(c) for c in CENTERS]
        labels = []
        for lab, c in zip(PANEL_LABELS, CENTERS):
            lab.move_to(c + np.array([-1.60, 1.45, 0.0]))
            labels.append(lab)

        self.play(
            *[FadeIn(c, scale=0.9) for c in contents],
            *[FadeIn(lab, shift=DOWN * 0.15) for lab in labels],
            run_time=1.0,
        )

        stage = Text("stage 1 of 3: rotate", font="DejaVu Sans",
                     font_size=30, color=BLUE)
        stage.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(stage, shift=UP * 0.2), run_time=0.6)

        # Stage 1: the first rotation (R2^T on the left, R1^T on the right).
        self.play(
            *[ApplyMatrix(M, obj, about_point=c)
              for M, obj, c in zip(
                  [R2.T, R1.T, R2.T, R1.T], contents, CENTERS)],
            run_time=1.7, rate_func=smooth,
        )

        # Stage 2: scale along the axes (Sigma on top, Sigma^-1 below).
        next_stage = Text("stage 2 of 3: scale", font="DejaVu Sans",
                          font_size=30, color=GREEN)
        next_stage.move_to(stage)
        self.play(Transform(stage, next_stage), run_time=0.4)
        self.play(
            *[ApplyMatrix(M, obj, about_point=c)
              for M, obj, c in zip(
                  [SIGMA, SIGMA_INV, SIGMA_INV, SIGMA], contents, CENTERS)],
            run_time=1.7, rate_func=smooth,
        )

        # Stage 3: the final rotation (R1 on the left, R2 on the right).
        next_stage = Text("stage 3 of 3: rotate", font="DejaVu Sans",
                          font_size=30, color=ORANGE)
        next_stage.move_to(stage)
        self.play(Transform(stage, next_stage), run_time=0.4)
        self.play(
            *[ApplyMatrix(M, obj, about_point=c)
              for M, obj, c in zip(
                  [R1, R2, R1, R2], contents, CENTERS)],
            run_time=1.7, rate_func=smooth,
        )

        self.wait(0.8)

        # Formula cards replace the labels; keep the ellipses faintly visible.
        formulas = [
            Text("A = R₁ Σ R₂ᵀ", font="DejaVu Sans",
                 font_size=32, color=INK),
            Text("A⁻¹ = R₂ Σ⁻¹ R₁ᵀ", font="DejaVu Sans",
                 font_size=32, color=INK),
            Text("A⁻ᵀ = R₁ Σ⁻¹ R₂ᵀ", font="DejaVu Sans",
                 font_size=32, color=INK),
            Text("Aᵀ = R₂ Σ R₁ᵀ", font="DejaVu Sans",
                 font_size=32, color=INK),
        ]
        for f, c in zip(formulas, CENTERS):
            f.move_to(c)
        boxes = [
            SurroundingRectangle(f, color=GRAY, buff=0.24, stroke_width=1.4)
            for f in formulas
        ]

        self.play(
            *[FadeOut(lab) for lab in labels],
            FadeOut(stage),
            *[obj.animate.set_opacity(0.12) for obj in contents],
            run_time=0.8,
        )
        self.play(
            *[FadeIn(f, shift=UP * 0.15) for f in formulas],
            *[FadeIn(b) for b in boxes],
            run_time=1.4,
        )

        insight = Text(
            "x · (A⁻ᵀ v̄) = (Ax) · v̄",
            font="DejaVu Sans", font_size=34, color=INK,
        )
        insight.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(1.8)
