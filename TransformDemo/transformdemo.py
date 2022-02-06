from manim import *
import numpy as np
import imageio

class dots(Scene):
    def construct(self):
        circle1 = Circle(radius=0.5, color = WHITE, fill_opacity=1)
        circle2 = circle1.copy()
        circle3 = circle1.copy()
        self.play(DrawBorderThenFill(circle1))
        self.add(circle2, circle3)
        self.play(circle2.animate.shift(LEFT*3))
        self.play(circle3.animate.shift(RIGHT*3))

class transform(Scene):
    def construct(self):
        filename = '/home/shervin/Documents/manimprojects/TransformDemo/media/videos/transformdemo/1080p60/dots.mp4'
        vid = imageio.get_reader(filename, 'ffmpeg')
        #image = ImageMobject(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(vid.get_data(100)))))
        #image = ImageMobject(np.fft.fftshift(np.fft.fft2(vid.get_data(100))))
        self.add(image)
        #image.add_updater(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(vid.get_data(frame.all())))))
        for frame in vid:
            self.add(ImageMobject(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(vid.get_data(frame.all()))))))
