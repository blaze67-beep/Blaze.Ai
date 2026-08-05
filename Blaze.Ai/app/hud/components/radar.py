import math

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPen, QPolygon

from app.config.theme import PRIMARY, SECONDARY

from PySide6.QtCore import QPoint


def draw(painter, x, y, angle):

    radius = 150

    # =====================================
    # Scan Cone
    # =====================================

    for i in range(18):

        sweep = angle - i * 2

        a1 = math.radians(sweep - 1.8)
        a2 = math.radians(sweep + 1.8)

        alpha = max(0, 140 - i * 8)

        painter.setPen(Qt.NoPen)

        painter.setBrush(
            QColor(
                PRIMARY.red(),
                PRIMARY.green(),
                PRIMARY.blue(),
                alpha
            )
        )

        polygon = QPolygon([
            QPoint(x, y),
            QPoint(
                int(x + math.cos(a1) * radius),
                int(y + math.sin(a1) * radius)
            ),
            QPoint(
                int(x + math.cos(a2) * radius),
                int(y + math.sin(a2) * radius)
            )
        ])

        painter.drawPolygon(polygon)

    # =====================================
    # Bright Sweep Edge
    # =====================================

    a = math.radians(angle)

    pen = QPen(SECONDARY)
    pen.setWidth(3)
    pen.setCapStyle(Qt.RoundCap)

    painter.setPen(pen)

    painter.drawLine(
        x,
        y,
        int(x + math.cos(a) * radius),
        int(y + math.sin(a) * radius)
    )

    # =====================================
    # Energy Pulse
    # =====================================

    pulse_radius = 8 + math.sin(math.radians(angle * 6)) * 2

    painter.setBrush(SECONDARY)
    painter.setPen(Qt.NoPen)

    painter.drawEllipse(
        int(x - pulse_radius),
        int(y - pulse_radius),
        int(pulse_radius * 2),
        int(pulse_radius * 2)
    )