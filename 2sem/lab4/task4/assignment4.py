import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QColorDialog


class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)
        self.smileyColor = QtGui.QColor("yellow")
        self.scale = 1.0

    def setColor(self, color):
        self.smileyColor = color
        self.update()

    def setScale(self, scale_value):
        self.scale = scale_value / 100.0
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        w = self.width()
        h = self.height()
        cx, cy = w // 2, h // 2
        radius = 50 * self.scale
        painter.setBrush(self.smileyColor)
        painter.setPen(QtCore.Qt.black)
        painter.drawEllipse(QtCore.QPointF(cx, cy), radius, radius)
        eye_offset = radius / 2
        eye_radius = 5 * self.scale
        painter.setBrush(QtCore.Qt.black)
        painter.drawEllipse(QtCore.QPointF(cx - eye_offset, cy - eye_offset), eye_radius, eye_radius)
        painter.drawEllipse(QtCore.QPointF(cx + eye_offset, cy - eye_offset), eye_radius, eye_radius)
        rect = QtCore.QRectF(cx - radius / 1.5, cy, radius * 1.3, radius / 1.2)
        painter.drawArc(rect, 0, 180 * 16)
        painter.end()


class MainWindow4(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow4, self).__init__()
        uic.loadUi("assignment4.ui", self)
        self.canvasWidget = Canvas(self.canvas)
        layout = self.canvas.parentWidget().layout()
        layout.addWidget(self.canvasWidget)
        self.chooseColorButton.clicked.connect(self.chooseColor)
        self.scaleSlider.valueChanged.connect(self.canvasWidget.setScale)

    def chooseColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvasWidget.setColor(color)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow4()
    window.show()
    sys.exit(app.exec_())
