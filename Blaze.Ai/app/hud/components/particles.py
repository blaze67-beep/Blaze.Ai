import math

from PySide6.QtGui import QColor


def draw(painter, x, y, angle):

    for i in range(8):

        a = angle + i * 45

        px = x + math.cos(math.radians(a)) * 150
        py = y + math.sin(math.radians(a)) * 150

        painter.setBrush(QColor(0, 255, 255))

        painter.drawEllipse(
            int(px) - 3,
            int(py) - 3,
            6,
            6
        )