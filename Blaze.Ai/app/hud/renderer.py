from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt

from app.hud.components import glow
from app.hud.components import rings
from app.hud.components import center
from app.hud.components import crosshair
from app.hud.components import radar

from app.hud.depth import DepthProjector
from app.hud.particle_engine import ParticleEngine


class HUDRenderer:

    def __init__(self):

        self.projector = DepthProjector()
        self.particles = ParticleEngine()

    def draw(self, painter: QPainter, x: int, y: int, angle: float):

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.NoBrush)

        # Update particle animation
        self.particles.update()

        # ==========================
        # BACK LAYER
        # ==========================

        glow.draw(painter, x, y)

        # ==========================
        # RADAR
        # ==========================

        radar.draw(painter, x, y, angle)

        # ==========================
        # PARTICLES
        # ==========================

        self.particles.draw(painter, x, y)

        # ==========================
        # MAIN RINGS
        # ==========================

        rings.draw(painter, x, y, angle)

        # ==========================
        # CROSSHAIR
        # ==========================

        crosshair.draw(painter, x, y)

        # ==========================
        # REACTOR
        # ==========================

        center.draw(painter, x, y, angle)