from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.input_field = QLineEdit(self)
        self.result_field = QLineEdit(self)
        self.result_field.setReadOnly(True)

        self.button = QPushButton("Вычислить", self)
        self.button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        layout.addWidget(self.result_field)

        self.setLayout(layout)
        self.setWindowTitle("Калькулятор выражений")

    def calculate(self):
        try:
            result = eval(self.input_field.text())
            self.result_field.setText(str(result))
        except Exception:
            self.result_field.setText("Ошибка")


if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()