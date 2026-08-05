from PySide6.QtCore import Qt
from PySide6.QtGui import QPen

from app.config.theme import PRIMARY, GLOW


def draw(painter, x, y):

    painter.setBrush(Qt.NoBrush)

    # Outer glow
    for i in range(12):

        pen = QPen(GLOW)
        pen.setWidth(max(1, 22 - i))

        painter.setPen(pen)

        r = 150 + i * 3

        painter.drawEllipse(
            x - r,
            y - r,
            r * 2,
            r * 2
        )

    # Bright edge
    pen = QPen(PRIMARY)
    pen.setWidth(4)

    painter.setPen(pen)

    painter.drawEllipse(
        x - 150,
        y - 150,
        300,
        300
    )