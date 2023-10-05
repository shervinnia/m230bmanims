from manim import *
from concurrent.futures import ThreadPoolExecutor

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



count = 1
def create_lattice_point(x, y, z):
    global count
    print(f"adding sphere {count}")
    count = count+1
    return Sphere(radius=0.01, color=BLUE).shift(x * 0.25* RIGHT + y * 0.25* UP + z * 0.25* OUT)

class EwaldSphereRotation(ThreeDScene):
    def construct(self):
        # Initialize 3D view and axes
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes)

        # Initialize the reciprocal lattice
        lattice_points = []

        with ThreadPoolExecutor() as executor:
            future_to_point = {(x, y, z): executor.submit(create_lattice_point, x, y, z)
                               for x in range(-8, 12)
                               for y in range(-8, 12)
                               for z in range(-8, 12)}
            
            for future in future_to_point.values():
                lattice_points.append(future.result())

        self.add(*lattice_points)

        
        # Draw and label Ewald Sphere
        ewald_sphere = Sphere(radius=1).set_fill(color = WHITE, opacity=0.5).move_to([1,0,0])  
        #ewald_label = Text("Ewald Sphere").scale(0.2).next_to(ewald_sphere, direction=RIGHT, buff=0.5)
        self.add(ewald_sphere)
        
        # Animate rotation of Ewald Sphere
        self.play(Rotate(ewald_sphere, about_point=ORIGIN, angle=2*PI, run_time=30, rate_func=linear))

        # TODO: Detect intersections with lattice points and draw reflection vectors
        # You'll need custom logic to detect these intersections in real-time during the animation
        # Once an intersection is detected, you can use the following code to draw a reflection vector
        # intersection_point = ...  # Replace with actual coordinates
        # reflection_vector = Arrow(ORIGIN, intersection_point, color=RED)
        # reflection_label = Text("Reflection Vector").scale(0.2).next_to(reflection_vector, direction=RIGHT, buff=0.5)
        # self.add(reflection_vector, reflection_label)
        
        # Optional: Zoom in/out
        # self.play(self.camera.frame.animate.scale(0.5))