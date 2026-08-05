from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget

from app.core.input_manager import InputManager
from app.vision.vision_engine import VisionEngine
from app.hud.renderer import HUDRenderer


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(640, 480)
        self.setWindowTitle("Blaze.AI")

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.vision = VisionEngine()
        self.input = InputManager(self.vision)
        self.renderer = HUDRenderer()

        self.angle = 0

        self.hud_x = 320.0
        self.hud_y = 240.0

        self.target_hud_x = self.hud_x
        self.target_hud_y = self.hud_y

        self.mouse_dragging = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(16)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_dragging = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_dragging = False

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_H:
            self.input.toggle()
            print("Mode:", self.input.mode)

    def update_frame(self):

        self.angle += 6

        if self.input.mode == self.input.MOUSE:

            if self.mouse_dragging:

                position = self.input.position(self)

                if position is not None:
                    self.target_hud_x, self.target_hud_y = position

        else:

            position = self.input.position(self)

            if position is not None:
                self.target_hud_x, self.target_hud_y = position

        self.hud_x += (self.target_hud_x - self.hud_x) * 0.15
        self.hud_y += (self.target_hud_y - self.hud_y) * 0.20

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        self.renderer.draw(
            painter,
            int(self.hud_x),
            int(self.hud_y),
            self.angle
        )