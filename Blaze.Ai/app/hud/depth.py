import math


class DepthProjector:

    def __init__(self):

        self.focal_length = 700
        self.camera_distance = 600

    def project(self, x, y, z):

        scale = self.focal_length / (self.camera_distance - z)

        return (
            x * scale,
            y * scale,
            scale
        )