from manim import *

class Rphi(Scene):
    def construct(self):
        tex = MathTex(
            r"\bold{R}_{x}(\phi)=\begin{bmatrix}1 & 0 & 0 \\0 & \cos(\phi) & -\sin(\phi) \\0 & \sin(\phi) & \cos(\phi)\end{bmatrix}", font_size=80)
        tex2 = MathTex(
            r"\bold{R}_{y}(\phi)=\begin{bmatrix}\cos(\phi) & 0 & \sin(\phi) \\0 & 1 & 0 \\ -\sin(\phi) & 0 & \cos(\phi)\end{bmatrix}", font_size=40)
        tex3 = MathTex(
            r"\bold{R}_{z}(\phi)=\begin{bmatrix}\cos(\phi) & -\sin(\phi) & 0 \\sin(\phi) & \cos(\phi) & 0 \\0 & 0 & 1\end{bmatrix}", font_size=40)
        self.play(Write(tex))
        self.wait()
        self.play(ScaleInPlace(tex,0.5))
        self.play(tex.animate.shift(3*UP))
        self.play(Write(tex3))
        self.play(tex3.animate.shift(3*DOWN))
        self.play(Write(tex2))
        self.wait()
