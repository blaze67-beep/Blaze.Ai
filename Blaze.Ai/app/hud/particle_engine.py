import random

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class Particle:

    def __init__(self, cx, cy):
        self.respawn(cx, cy)

    def respawn(self, cx, cy):

        self.angle = random.uniform(0, 360)
        self.radius = random.uniform(120, 170)

        self.speed = random.uniform(0.2, 1.0)

        self.size = random.randint(2, 6)

        self.alpha = random.randint(120, 255)

    def update(self):

        self.angle += self.speed

    def draw(self, painter, cx, cy):

        import math

        x = cx + math.cos(math.radians(self.angle)) * self.radius
        y = cy + math.sin(math.radians(self.angle)) * self.radius

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 255, 255, self.alpha))
        painter.drawEllipse(int(x), int(y), self.size, self.size)


class ParticleEngine:

    def __init__(self):

        self.particles = []

        for _ in range(100):
            self.particles.append(Particle(250, 250))

    def update(self):

        for p in self.particles:
            p.update()

    def draw(self, painter, cx, cy):

        for p in self.particles:
            p.draw(painter, cx, cy)