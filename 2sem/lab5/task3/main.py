import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor, QPolygonF
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Shape:
    def __init__(self, shape_type, pos, size, color):
        self.shape_type = shape_type
        self.pos = pos
        self.size = size
        self.color = color


class DrawingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shapes = []
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.StrongFocus)

    def mousePressEvent(self, event):
        pos = event.pos()
        size = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if event.button() == Qt.LeftButton:
            self.shapes.append(Shape("circle", pos, size, color))
        elif event.button() == Qt.RightButton:
            self.shapes.append(Shape("square", pos, size, color))
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            pos = self.mapFromGlobal(self.cursor().pos())
            size = random.randint(20, 100)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.shapes.append(Shape("triangle", pos, size, color))
            self.update()
        else:
            super().keyPressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for shape in self.shapes:
            painter.setBrush(shape.color)
            painter.setPen(shape.color)
            if shape.shape_type == "circle":
                r = shape.size / 2
                painter.drawEllipse(shape.pos.x() - r, shape.pos.y() - r, shape.size, shape.size)
            elif shape.shape_type == "square":
                r = shape.size / 2
                painter.drawRect(shape.pos.x() - r, shape.pos.y() - r, shape.size, shape.size)
            elif shape.shape_type == "triangle":
                r = shape.size / 2
                p1 = QPointF(shape.pos.x(), shape.pos.y() - r)
                p2 = QPointF(shape.pos.x() - r, shape.pos.y() + r)
                p3 = QPointF(shape.pos.x() + r, shape.pos.y() + r)
                triangle = QPolygonF([p1, p2, p3])
                painter.drawPolygon(triangle)
        painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("drawing.ui", self)
        self.drawingWidget = DrawingWidget(self)
        self.setCentralWidget(self.drawingWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
