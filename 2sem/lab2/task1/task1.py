import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic


class FlagApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('flag_app.ui', self)

        self.drawButton.clicked.connect(self.draw_flag)

        self.setFixedSize(300, 200)

    def draw_flag(self):
        colors = []
        if self.redCheckBox.isChecked():
            colors.append("Красный")
        if self.greenCheckBox.isChecked():
            colors.append("Зелёный")
        if self.blueCheckBox.isChecked():
            colors.append("Синий")
        if self.whiteCheckBox.isChecked():
            colors.append("Белый")
        if self.yellowCheckBox.isChecked():
            colors.append("Жёлтый")

        if colors:
            self.resultLabel.setText(', '.join(colors))
        else:
            self.resultLabel.setText("Выберите хотя бы один цвет!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlagApp()
    window.show()
    sys.exit(app.exec())
