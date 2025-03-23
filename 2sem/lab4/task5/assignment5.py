import sys, math
from PyQt5 import QtWidgets, uic, QtCore
import pyqtgraph as pg
import numpy as np


class MainWindow5(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow5, self).__init__()
        uic.loadUi("assignment5.ui", self)

        self.plotContainer = self.findChild(QtWidgets.QWidget, "plotContainer")
        self.plotWidget = pg.PlotWidget()
        layout = QtWidgets.QVBoxLayout(self.plotContainer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.plotWidget)

        self.plotButton.clicked.connect(self.plotFunction)

    def plotFunction(self):
        func_text = self.functionLineEdit.text().strip()
        try:
            a = float(self.minSpinBox.value())
            b = float(self.maxSpinBox.value())
            if a >= b:
                raise ValueError("Неверный диапазон")
            x = np.linspace(a, b, 1000)
            safe_dict = {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                         "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi, "abs": np.abs}
            y = eval(func_text, {"__builtins__": None}, safe_dict)
            self.plotWidget.clear()
            self.plotWidget.plot(x, y, pen=pg.mkPen('b', width=2))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка вычисления функции:\n{e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow5()
    window.show()
    sys.exit(app.exec_())
