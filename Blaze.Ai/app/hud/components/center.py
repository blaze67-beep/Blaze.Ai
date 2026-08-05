import math

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen

from app.config.theme import PRIMARY, SECONDARY, ACCENT


def draw(painter, x, y, angle):

    painter.save()

    painter.translate(x, y)
    painter.rotate(angle * 2)

    # ==========================
    # OUTER REACTOR RING
    # ==========================

    pen = QPen(PRIMARY)
    pen.setWidth(3)
    painter.setPen(pen)
    painter.setBrush(Qt.NoBrush)

    painter.drawEllipse(-28, -28, 56, 56)

    # ==========================
    # INNER RING
    # ==========================

    pen = QPen(SECONDARY)
    pen.setWidth(2)
    painter.setPen(pen)

    painter.drawEllipse(-18, -18, 36, 36)

    # ==========================
    # ENERGY SPIKES
    # ==========================

    pen = QPen(PRIMARY)
    pen.setWidth(2)
    painter.setPen(pen)

    for i in range(8):

        a = math.radians(i * 45)

        x1 = math.cos(a) * 20
        y1 = math.sin(a) * 20

        x2 = math.cos(a) * 30
        y2 = math.sin(a) * 30

        painter.drawLine(
            int(x1),
            int(y1),
            int(x2),
            int(y2)
        )

    painter.restore()

    # ==========================
    # PULSING CORE
    # ==========================

    pulse = 10 + math.sin(math.radians(angle * 8)) * 3

    painter.setPen(Qt.NoPen)
    painter.setBrush(SECONDARY)

    painter.drawEllipse(
        int(x - pulse),
        int(y - pulse),
        int(pulse * 2),
        int(pulse * 2)
    )

    # Bright center

    painter.setBrush(ACCENT)

    painter.drawEllipse(
        x - 3,
        y - 3,
        6,
        6
    )