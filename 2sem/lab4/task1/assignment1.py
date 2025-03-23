import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
from PIL import Image


class MainWindow1(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow1, self).__init__()
        uic.loadUi("assignment1.ui", self)
        self.original_image = None
        self.processed_image = None

        self.channelComboBox.currentIndexChanged.connect(self.updateImage)
        self.rotateLeftButton.clicked.connect(lambda: self.rotateImage(-90))
        self.rotateRightButton.clicked.connect(lambda: self.rotateImage(90))

        self.openImage()

    def openImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Выберите квадратное изображение", "",
                                               "Images (*.png *.jpg *.bmp)")
        if not fname:
            return

        self.original_image = Image.open(fname).convert("RGB")
        if self.original_image.width != self.original_image.height:
            QMessageBox.warning(self, "Ошибка", "Изображение должно быть квадратным!")
            return

        self.processed_image = self.original_image.copy()
        self.showImage()

    def updateImage(self):
        if self.original_image is None:
            return

        channel = self.channelComboBox.currentText()
        img = self.original_image.copy()
        data = np.array(img)

        if channel in ['Red', 'Green', 'Blue']:
            channels = {'Red': 0, 'Green': 1, 'Blue': 2}
            keep = channels[channel]
            for c in range(3):
                if c != keep:
                    data[..., c] = 0

        self.processed_image = Image.fromarray(data)
        self.showImage()

    def rotateImage(self, angle):
        if self.processed_image:
            self.processed_image = self.processed_image.rotate(angle, expand=True)
            self.showImage()

    def showImage(self):
        if self.processed_image is None:
            return

        image = self.processed_image.convert("RGB")
        data = image.tobytes("raw", "RGB")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size(),
                                                 QtCore.Qt.KeepAspectRatio,
                                                 QtCore.Qt.SmoothTransformation))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow1()
    window.show()
    sys.exit(app.exec_())
