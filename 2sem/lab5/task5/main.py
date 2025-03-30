import sys
import os
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

MOVE_STEP = 20


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class UFOWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = resource_path("ufo.ui")
        uic.loadUi(ui_file, self)
        self.setWindowTitle("Управление НЛО")
        self.setFocusPolicy(Qt.StrongFocus)

    def keyPressEvent(self, event):
        dx, dy = 0, 0
        key = event.key()
        if key == Qt.Key_Left:
            dx = -MOVE_STEP
        elif key == Qt.Key_Right:
            dx = MOVE_STEP
        elif key == Qt.Key_Up:
            dy = -MOVE_STEP
        elif key == Qt.Key_Down:
            dy = MOVE_STEP
        else:
            super().keyPressEvent(event)
            return

        current_pos = self.ufoLabel.pos()
        new_x = current_pos.x() + dx
        new_y = current_pos.y() + dy

        cw = self.centralwidget
        cw_width = cw.width()
        cw_height = cw.height()
        label_width = self.ufoLabel.width()
        label_height = self.ufoLabel.height()

        if new_x > cw_width:
            new_x = -label_width
        elif new_x + label_width < 0:
            new_x = cw_width
        if new_y > cw_height:
            new_y = -label_height
        elif new_y + label_height < 0:
            new_y = cw_height

        self.ufoLabel.move(new_x, new_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UFOWindow()
    window.show()
    sys.exit(app.exec_())
