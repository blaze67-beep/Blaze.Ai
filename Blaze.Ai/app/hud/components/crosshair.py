from PySide6.QtGui import QColor, QPen


def draw(painter, x, y):

    pen = QPen(QColor(0, 255, 255))
    pen.setWidth(2)

    painter.setPen(pen)

    painter.drawLine(x - 25, y, x - 8, y)
    painter.drawLine(x + 8, y, x + 25, y)

    painter.drawLine(x, y - 25, x, y - 8)
    painter.drawLine(x, y + 8, x, y + 25)