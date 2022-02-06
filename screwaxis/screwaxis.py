from manim import *

class GetZAxisLabelExample(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        point = Dot3D(point=ax.coords_to_point(0,0,1))
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        self.play(Create(ax))
        self.wait()
        self.play(Create(point))
        self.wait()
        self.play(Transform(point,np.cos(np.pi)))

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ]), color=RED, t_range = np.array([-3*TAU, 5*TAU, 0.01])
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.play(Create(axes))
        self.wait()
        self.play(Create(curve1))
        self.wait()
