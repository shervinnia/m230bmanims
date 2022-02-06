from manim import *

class ewaldspheres(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        sphere1 = Sphere(
            center=(3, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        self.play(Create(ax))
        self.wait()
        self.play(Create(sphere1))
        self.wait()
    #    self.play(Transform(sphere1,np.cos(3.14)))

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
