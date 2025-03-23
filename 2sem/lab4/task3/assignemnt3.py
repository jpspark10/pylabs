import sys, random
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor


class MainWindow3(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow3, self).__init__()
        uic.loadUi("assignment3.ui", self)
        self.generateFlag()

    def generateFlag(self):
        num, ok = QInputDialog.getInt(self, "Количество цветов", "Введите число цветов:",
                                      min=2, max=10, value=3)
        if not ok:
            return
        width = 300
        height = 200
        stripe_width = width // num
        image = QImage(width, height, QImage.Format_RGB32)
        painter = QPainter(image)
        for i in range(num):
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.fillRect(i * stripe_width, 0, stripe_width, height, color)
        painter.end()
        pixmap = QPixmap.fromImage(image)
        self.flagLabel.setPixmap(pixmap.scaled(self.flagLabel.size(),
                                               QtCore.Qt.KeepAspectRatio,
                                               QtCore.Qt.SmoothTransformation))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow3()
    window.show()
    sys.exit(app.exec_())
