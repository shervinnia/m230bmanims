from manim import *

class StructFactor(MovingCameraScene):
    def construct(self):
        color1 = "#3498DB"
        color2 = "#9834DB"
        self.camera.frame.save_state()
        f1 = Arrow(ORIGIN, [ 2, 0, 0], buff=0, stroke_width = 5)
        f2 = Arrow(f1.get_end(), [ 2, 2, 0], buff=0, stroke_width = 5)
        f3 = Arrow(f2.get_end(), [ 0, 2, 0], buff=0, stroke_width = 5)
        f4 = Arrow(f3.get_end(), f3.get_end()+[2*0.7071,2*0.7071,0], buff=0, stroke_width = 5)
        F = Arrow(ORIGIN,f4.get_end(),buff=0,color=color2)
        Fline = Line(start=ORIGIN,end=F.get_end())
        Fdot = Dot(point=F.get_end(),color=color2)

        zeroline = Line(start=ORIGIN,end=[1,0,0])
        phiangle = Angle(zeroline,Fline)
        Fcircle=Circle(radius=F.get_length(),color=color2).rotate(phiangle.get_value())
        tip_text = MathTex(r'\vec{F}',color=color2).next_to([0.5,1.5,0], RIGHT*1.2)
        tex = MathTex(r"\phi").next_to(phiangle,RIGHT*0.3 + UP*0.1)
        Fmagtex=Text('|F|',color=color2).next_to(Fdot,LEFT*0.5+DOWN*0.1)
        self.play(Write(Axes(
                            x_range=(-14.222,14.222,1),
                            y_range=(-8,8,1),
                            x_length=14.222,
                            y_length=8,
                            axis_config={
                                "color":color1
                            }
                            )))
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
        self.play(Create(F))
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
        self.play(DrawBorderThenFill(Fcircle))
        self.play(Write(Fmagtex))
        self.wait(5)
