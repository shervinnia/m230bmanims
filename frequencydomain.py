from manim import *
import numpy as np

class frequencydomain(Scene):
    def construct(self):
        self.show_axes()

    def show_axes(self):
        x_start = np.array([1,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([2,-2,0])
        y_end = np.array([2,2,0])

        x_axisfreq = Line(x_start, x_end)
        y_axisfreq = Line(y_start, y_end)

        x_axistime = Line(x_start-np.array([7,0,0]), x_end-np.array([7,0,0]))
        y_axistime = Line(y_start-np.array([5.5,0,0]), y_end-np.array([5.5,0,0]))

        self.add(x_axisfreq, x_axistime, y_axisfreq, y_axistime)
