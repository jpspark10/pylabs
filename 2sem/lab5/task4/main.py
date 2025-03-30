import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("button.ui", self)
        # Получаем кнопку по имени, заданному в UI-файле
        self.button = self.pushButton
        self.setMouseTracking(True)
        self.centralwidget.setMouseTracking(True)
        self.button.setFixedSize(100, 50)

    def showEvent(self, event):
        super().showEvent(event)
        self.move_button_randomly()

    def move_button_randomly(self):
        cw_width = self.centralwidget.width()
        cw_height = self.centralwidget.height()
        btn_width = self.button.width()
        btn_height = self.button.height()
        max_x = cw_width - btn_width
        max_y = cw_height - btn_height
        if max_x < 0 or max_y < 0:
            return
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.button.move(new_x, new_y)

    def mouseMoveEvent(self, event):
        cursor_pos = event.pos()
        # Получаем геометрию кнопки
        btn_geo = self.button.geometry()
        btn_center_x = btn_geo.x() + btn_geo.width() / 2
        btn_center_y = btn_geo.y() + btn_geo.height() / 2
        dx = cursor_pos.x() - btn_center_x
        dy = cursor_pos.y() - btn_center_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        threshold = 50  # пороговое расстояние в пикселях
        if distance < threshold:
            self.move_button_randomly()
        super().mouseMoveEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
