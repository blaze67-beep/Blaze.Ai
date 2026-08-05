import math

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen

from app.config.theme import PRIMARY, SECONDARY
from app.config.hud import (
    HUD_RADIUS,
    INNER_RING,
    ENERGY_RING,
    INNER_ROTATION,
    ENERGY_ROTATION,
)

from app.hud.perspective import Perspective


perspective = Perspective()


def draw(painter, x, y, angle):

    # ==========================
    # OUTER RING (Perspective)
    # ==========================

    outer_w, outer_h = perspective.ellipse(HUD_RADIUS)

    painter.save()

    painter.translate(x, y)
    painter.rotate(angle)

    pen = QPen(PRIMARY)
    pen.setWidth(4)
    pen.setCapStyle(Qt.RoundCap)

    painter.setPen(pen)

    for start in range(0, 360, 45):

        painter.drawArc(
            -int(outer_w),
            -int(outer_h),
            int(outer_w * 2),
            int(outer_h * 2),
            start * 16,
            22 * 16
        )

    painter.restore()

    # ==========================
    # INNER RING
    # ==========================

    inner_w, inner_h = perspective.ellipse(INNER_RING)

    painter.save()

    painter.translate(x, y)
    painter.rotate(-angle * INNER_ROTATION)

    pen = QPen(SECONDARY)
    pen.setWidth(3)
    pen.setCapStyle(Qt.RoundCap)

    painter.setPen(pen)

    for start in range(0, 360, 30):

        painter.drawArc(
            -int(inner_w),
            -int(inner_h),
            int(inner_w * 2),
            int(inner_h * 2),
            start * 16,
            10 * 16
        )

    painter.restore()

    # ==========================
    # ENERGY SPIKES
    # ==========================

    painter.save()

    painter.translate(x, y)
    painter.rotate(angle * ENERGY_ROTATION)

    pen = QPen(PRIMARY)
    pen.setWidth(2)

    painter.setPen(pen)

    for i in range(12):

        a = math.radians(i * 30)

        x1 = math.cos(a) * ENERGY_RING
        y1 = math.sin(a) * ENERGY_RING * perspective.tilt

        x2 = math.cos(a) * (ENERGY_RING + 10)
        y2 = math.sin(a) * (ENERGY_RING + 10) * perspective.tilt

        painter.drawLine(
            int(x1),
            int(y1),
            int(x2),
            int(y2)
        )

    painter.restore()