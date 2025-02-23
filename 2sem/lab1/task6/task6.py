from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import QTimer


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.display = QLineEdit(self)
        self.display.setValidator(QDoubleValidator())
        self.layout.addWidget(self.display)

        self.timer_label = QLabel("", self)  # Добавляем метку для таймера
        self.layout.addWidget(self.timer_label)

        grid_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)
        ]

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            grid_layout.addWidget(button, row, col)

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)
        self.setWindowTitle("Калькулятор")

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except ZeroDivisionError:
                self.display.setText(f"Ошибка: Деление на ноль")
                self.start_timer()
            except Exception:
                self.display.setText(f"Ошибка: Некорректное выражение")
                self.start_timer()
        elif text == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + text)

    def start_timer(self):
        self.remaining_time = 3
        self.timer_label.setText(f"Очистка через: {self.remaining_time}")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time > 0:
            self.timer_label.setText(f"Очистка через: {self.remaining_time}")
        else:
            self.display.clear()
            self.timer_label.clear()
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()
