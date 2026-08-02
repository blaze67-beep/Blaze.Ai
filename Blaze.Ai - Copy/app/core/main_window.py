import math

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget

from app.hud.effects import get_hand_position


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Blaze.AI")
        self.resize(500, 500)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.hand_x = None
        self.hand_y = None

        self.angle = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):
        self.angle += 2

        hand = get_hand_position()

        if hand:
            self.hand_x, self.hand_y = hand

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.hand_x is not None and self.hand_y is not None:
            cx = self.hand_x
            cy = self.hand_y
        else:
            cx = self.width() // 2
            cy = self.height() // 2

        # Main ring
        pen = QPen(QColor(0, 170, 255))
        pen.setWidth(5)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        painter.drawEllipse(cx - 150, cy - 150, 300, 300)

        # Orbiting dot
        x = cx + math.cos(math.radians(self.angle)) * 150
        y = cy + math.sin(math.radians(self.angle)) * 150

        painter.setBrush(QColor(0, 255, 255))
        painter.drawEllipse(int(x) - 8, int(y) - 8, 16, 16)