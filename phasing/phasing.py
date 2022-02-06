from manim import *

class StructFactor(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        f1 = Arrow(ORIGIN, [ 2, 0, 0], buff=0, stroke_width = 5)
        f2 = Arrow(f1.get_end(), [ 2, 2, 0], buff=0, stroke_width = 5)
        f3 = Arrow(f2.get_end(), [ 0, 2, 0], buff=0, stroke_width = 5)
        f4 = Arrow(f3.get_end(), f3.get_end()+[2*0.7071,2*0.7071,0], buff=0, stroke_width = 5)
        F = Arrow(ORIGIN,f4.get_end(),buff=0,color='#3498DB')
        Fline = Line(start=ORIGIN,end=F.get_end())
        zeroline = Line(start=ORIGIN,end=[1,0,0])
        phiangle = Angle(zeroline,Fline)

        tip_text = Text('F',color='#3498DB').next_to([0.5,1.5,0], RIGHT*1.2)
        tex = MathTex(r"\phi").next_to(phiangle,RIGHT*0.3 + UP*0.1)
        self.play(Write(Axes(
                            x_range=(-14.222,14.222,1),
                            y_range=(-8,8,1),
                            x_length=14.222,
                            y_length=8,
                            axis_config={
                                "color":'#F08763'
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
        self.play(DrawBorderThenFill(F))
        self.wait(2)
        self.play(Write(tip_text))
        self.play(Write(phiangle),Write(tex))
        self.wait(10)
