import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image
import numpy as np


class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()
        uic.loadUi("assignment2.ui", self)
        self.original_image = None  # PIL Image (RGBA)
        self.processed_image = None
        self.alphaSlider.valueChanged.connect(self.updateAlpha)
        self.openImage()

    def openImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Открыть изображение", "",
                                               "Images (*.png *.jpg *.bmp)")
        if not fname:
            return
        self.original_image = Image.open(fname).convert("RGBA")
        self.processed_image = self.original_image.copy()
        self.showImage()

    def updateAlpha(self, value):
        if self.original_image is None:
            return
        img = self.original_image.copy()
        data = np.array(img)
        data[..., 3] = value
        self.processed_image = Image.fromarray(data, mode="RGBA")
        self.showImage()

    def showImage(self):
        if self.processed_image is None:
            return
        image = self.processed_image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)
        self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size(),
                                                QtCore.Qt.KeepAspectRatio,
                                                QtCore.Qt.SmoothTransformation))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow2()
    window.show()
    sys.exit(app.exec_())
