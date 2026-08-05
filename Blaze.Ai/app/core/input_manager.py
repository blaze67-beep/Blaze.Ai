from PySide6.QtGui import QCursor


class InputManager:

    MOUSE = "mouse"
    HAND = "hand"

    def __init__(self, vision):
        self.mode = self.MOUSE
        self.vision = vision

    def toggle(self):
        self.mode = self.HAND if self.mode == self.MOUSE else self.MOUSE

    def position(self, window):

        if self.mode == self.MOUSE:

            pos = QCursor.pos()

            return (
                pos.x() - window.frameGeometry().x(),
                pos.y() - window.frameGeometry().y()
            )

        hand = self.vision.get_hand()

        return hand