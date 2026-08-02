import sys

from PySide6.QtWidgets import QApplication
from app.core.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

print("Blaze.AI started...")

sys.exit(app.exec())
