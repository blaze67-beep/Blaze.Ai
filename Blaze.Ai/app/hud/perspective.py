import math


class Perspective:

    def __init__(self):

        self.tilt = 0.75

    def ellipse(self, radius):

        width = radius
        height = radius * self.tilt

        return width, height