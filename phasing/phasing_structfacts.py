from manim import *
#from gtts import gTTS


#intro = "Every structure factor in a Fourier Transform has a representation in the complex plane. Recall that each structure factor represents one wave in the Fourier synthsis of the electron density function of our molecule of interest. All three features of any sinusoidal wave are encoded in the Fourier transform, just not in the way we may be able to intuitively see at first. The frequency of the wave is represented by the location of the structure factor in reciprocal space; the Miller index of the structure factor directly corresponds to the frequency of the wave in all three real-space dimensions. The aplitude of the wave is represented by the amplitude of the structure factor in the complex plane. Finally, the phase of the wave is represented by the angle phi of the structure factor."
#intro_tts = gTTS(text=intro, lang='en')
#intro_tts.save("phasing_structfacts_intro.mp3")


class ShowStructFacts(Scene):
    def construct(self):
        color1 = "#FBE7C6"
        color2 = "#B4F8C8"
        color3 = "#a0e7e5"
        color4 = "#ffaebc"
        mob = ImageMobject("./FT_inv.jpg")
        mob.scale(2.5)
        mob.move_to(LEFT*3.2)
        dot1 = Dot(point=[-0.5,-0.05,0], radius=0)
        dot2 = Dot(point=[-2.17,1.57,0], radius = 0)
        dot3 = Dot(point=[-3.85,-1.93,0], radius = 0)
        square = SurroundingRectangle(dot1, corner_radius=0.1)
        plane = ComplexPlane(
                            x_range=(-3,3,1),
                            y_range=(-3,3,1),
                            background_line_style={"stroke_width": 0}
                            ).add_coordinates().move_to(RIGHT*3.8)
        GridSquare = SurroundingRectangle(plane, corner_radius = 0.2)
        structCircle1 = Circle(radius=1, color=color1).move_to(plane.get_origin())
        structCircle2 = Circle(radius=0.5, color=color2).move_to(plane.get_origin())
        radius3 = 2
        structCircle3 = Circle(radius=radius3, color=color3).move_to(plane.get_origin())
        Fmagtex1=MathTex(r"|\vec{F}|_1",color=color1,font_size=20).move_to(structCircle1.point_at_angle(45*DEGREES) + UR*0.3)
        Fmagtex2=MathTex(r"|\vec{F}|_2",color=color2,font_size=20).move_to(structCircle2.point_at_angle(45*DEGREES) + UR*0.3)
        Fmagtex3=MathTex(r"|\vec{F}|_3",color=color3,font_size=20).move_to(structCircle3.point_at_angle(45*DEGREES) + UR*0.3)
        #self.add(mob, dot1, dot2, dot3, square, plane, structCircle1, GridSquare, Fmagtex1)
        self.add(dot1, dot2, dot3)
        self.wait(2)
        self.play(
            FadeIn(mob),
            Create(plane)
            )
        self.wait(1)
        self.play(
            Create(square),
            Create(structCircle1),
            Create(GridSquare),
            Write(Fmagtex1))
        self.wait(10)
        self.play(
            square.animate.move_to(dot2.get_center()),
            #ScaleInPlace(structCircle1,2),
            #Fmagtex1.animate.move_to(structCircle2.point_at_angle(45*DEGREES) + UR*0.3)
            Uncreate(structCircle1),
            Unwrite(Fmagtex1),
            Create(structCircle2),
            Write(Fmagtex2),
            )
        self.wait(5)
        self.play(
            square.animate.move_to(dot3.get_center()),
            #ScaleInPlace(structCircle1,0.25),
            #Fmagtex1.animate.move_to(structCircle3.point_at_angle(45*DEGREES) + UR*0.3)
            Uncreate(structCircle2),
            Unwrite(Fmagtex2),
            Create(structCircle3),
            Write(Fmagtex3)
            )
        self.wait(5)
        self.play(FadeOut(mob),
                  Uncreate(square))
        self.wait(1)
        movefinal = LEFT*6.8
        self.play(
            plane.animate.shift(movefinal),
            GridSquare.animate.shift(movefinal),
            structCircle3.animate.shift(movefinal),
            Fmagtex3.animate.shift(movefinal))

        realspaceaxes = NumberPlane(
            x_range=[-2,8,1],
            y_range=[-1.5,1.5,1],
            x_length=5,
            axis_config={"color":WHITE},
            background_line_style={"stroke_width": 0},
            tips = False).add_coordinates().move_to(RIGHT*3.8)
        axes_labels = realspaceaxes.get_axis_labels()

        phase = ValueTracker(0)

        sine_function = lambda x: radius3 * np.sin(x+np.deg2rad(phase.get_value()))
        sine_graph = always_redraw(lambda: realspaceaxes.plot(
            sine_function,
            color=BLUE
        ))

        #movingvector = always_redraw(Arrow(plane.get_origin(), structCircle3.point_at_angle(phase.get_value()), buff=0, stroke_width = 5))

        movingvector = Arrow(plane.get_origin(), structCircle3.point_at_angle(phase.get_value()), buff=0)

        self.wait(3)
        self.play(
            Create(realspaceaxes),
            Write(sine_graph),
            Write(movingvector))
        #self.add(realspaceaxes, sine_graph, movingvector)

        #movingvector.add_updater(
        #    lambda x: x.become(movingvector.copy()).rotate(
        #        angle=25, about_point = plane.get_origin()))

        movingvector.add_updater(
            lambda x: x.become(Arrow(plane.get_origin(), structCircle3.point_at_angle(np.deg2rad(phase.get_value())), buff=0)))

        # Animate the sine wave from y=sin(0.1*x) to y=sin(10*x) over the course of 6 seconds.
        self.play(phase.animate(run_time=10).set_value(phase.get_value()+360)),

        #self.play(
        #    Create(realspaceaxes),
        #    Create(sinwave))
        #self.wait(1)
        #self.play(
        #    phase.animate.set_value(150))


class StructFactor(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=3,
            zoomed_display_width=3,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
    )
    def construct(self):
        Title = MathTex(r'\textrm{The Phase Problem and Isomorphous Replacement}').move_to(ORIGIN+UP)
        subtitle = MathTex(r'\textrm{by Shervin Nia}').next_to(Title, DOWN)
        color1 = "#3498DB"
        color2 = "#9834DB"
        color3 = "#D4B638"
        color4 = "#F1F061"
        color5 = "#C15D86"
        self.camera.frame.save_state()
        f1 = Arrow(ORIGIN, [ 2, 0, 0], buff=0, stroke_width = 5)
        f2 = Arrow(f1.get_end(), [ 2, 2, 0], buff=0, stroke_width = 5)
        f3 = Arrow(f2.get_end(), [ 0, 2, 0], buff=0, stroke_width = 5)
        f4 = Arrow(f3.get_end(), f3.get_end()+[2*0.7071,2*0.7071,0], buff=0, stroke_width = 5)
        F = Arrow(ORIGIN,f4.get_end(),buff=0,color=color2)
        Fline = Line(start=ORIGIN,end=F.get_end())
        Fdot = Dot(point=F.get_end(),color=color2)

        Fcopy = F.copy()

        F2 = F.copy()
        F2.rotate_about_origin(15*PI/16)
        #Rotate(F2, angle=15*PI/16, about_point=ORIGIN)
        F2.shift(F.get_end())

        F3=F.copy()
        F3.rotate_about_origin(-1*15*PI/16)
        F3.shift(F.get_end())

        fh1 = Arrow(ORIGIN, F2.get_end(), buff=0, stroke_width = 5, color=color3)
        fh2 = Arrow(ORIGIN, F3.get_end(), buff=0, stroke_width = 5, color=color5)

        zeroline = Line(start=ORIGIN,end=[1,0,0])
        phiangle = Angle(zeroline,Fline)
        Fcircle=Circle(radius=F.get_length(),color=color2).rotate(phiangle.get_value())
        FH1circle = Fcircle.copy()
        FH2circle = Fcircle.copy()
        tip_text = MathTex(r'\vec{F}',color=color2).next_to([0.5,1.5,0], RIGHT*1.2)
        tex = MathTex(r"\phi").next_to(phiangle,RIGHT*0.3 + UP*0.1)
        #Fmagtex=MathTex(r'|\vec{F_P}|',color=color2).next_to(Fdot,LEFT*0.5+DOWN*0.1)
        Fmagtex=MathTex(r'|\vec{F_P}|',color=color2).move_to([6,3,0])
        FPH1tex=MathTex(r'|\vec{F}_{PH1}|', color=color4).next_to(Fmagtex, DOWN)
        FPH2tex=MathTex(r'|\vec{F}_{PH2}|', color=color5).next_to(FPH1tex, DOWN)

        axes = Axes(
                            x_range=(-14.222,14.222,1),
                            y_range=(-8,8,1),
                            x_length=14.222,
                            y_length=8,
                            axis_config={
                                "color":color1
                            }
                            )        
        
        #self.add_sound("phasing_structfacts_intro.mp3")'
        self.play(Write(Title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(Unwrite(Title), Unwrite(subtitle))
        self.play(Write(axes))
        self.play(self.camera.frame.animate.scale(0.6).move_to([1,1.5,0]))
        self.wait()
        self.play(GrowArrow(f1))
        #self.play(Write(Text('f1').next_to(f1,DOWN + LEFT)))
        self.wait()
        self.play(GrowArrow(f2))
        #self.play(Write(Text('f2').next_to(f2,DOWN+RIGHT)))
        self.wait()
        self.play(GrowArrow(f3))
        #self.play(Write(Text('f3').next_to(f3,DOWN+RIGHT)))
        self.wait()
        self.play(GrowArrow(f4))
        self.wait(3)
        self.play(GrowArrow(F))
        self.wait(2)
        self.play(Write(tip_text))
        self.play(Write(phiangle),Write(tex))
        self.wait(3)
        self.play(
            Create(Fdot),
            Uncreate(F),
            Uncreate(f1),
            Uncreate(f2),
            Uncreate(f3),
            Uncreate(f4),
            Unwrite(tip_text),
            Unwrite(phiangle),
            Unwrite(tex),
        )
        self.play(self.camera.frame.animate.scale(1/0.6).move_to([0,0,0]))
        self.wait()
        self.play(DrawBorderThenFill(Fcircle),
                  Uncreate(Fdot))
        self.play(Write(Fmagtex))
        self.wait(5)
        self.play(self.camera.frame.animate.scale(1.3))
        self.play(Create(FH1circle))
        #self.play(Create(F2))
        self.play(GrowArrow(fh1),FH1circle.animate.move_to(fh1.get_end()))
        self.play(GrowArrow(fh2),FH2circle.animate.move_to(fh2.get_end()))
        self.wait(0.5)
        self.play(FH1circle.animate.set_color(color4), FH2circle.animate.set_color(color5))
        self.play(Write(FPH1tex), Write(FPH2tex))

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame



        frame.move_to(Fdot)
        frame.set_color(color1)
        zoomed_display_frame.set_color(color1)
        zoomed_display.move_to([6,-2.5,0])

        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation())
        self.wait(2)

        self.play(DrawBorderThenFill(Fcopy))

        self.wait(5)

        self.play(
            Unwrite(Fmagtex),
            Unwrite(FPH1tex),
            Unwrite(FPH2tex),
            Uncreate(Fcopy))
        self.wait(0.2)
        self.play(Unwrite(axes))
        self.wait(0.5)
        self.play(Unwrite(fh1), Unwrite(fh2))
        self.play(
            Uncreate(Fcircle),
            Uncreate(FH1circle),
            Uncreate(FH2circle),
            Uncreate(zoomed_display_frame),
            FadeOut(frame))
        self.wait(0.5)



## COMBINED SCENE TO RUN EVERYTHING TOGETHER

def fade_out(scene: Scene):
    animations = []
    for mobject in scene.mobjects:
        animations.append(FadeOut(mobject))
    scene.play(*animations)


class CombinedScene(Scene):
    def construct(self):
        scenes = [ShowStructFacts, StructFactor] # TODO: Add scenes here
        for scene in scenes:
            scene.construct(self)
            fade_out(self)