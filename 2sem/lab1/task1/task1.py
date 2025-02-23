from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout


class WordSwitcher(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.input2.setReadOnly(True)

        self.button = QPushButton("→", self)
        self.button.clicked.connect(self.switch_text)

        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.button)
        layout.addWidget(self.input2)

        self.setLayout(layout)
        self.setWindowTitle("Перекидыватель слов")

    def switch_text(self):
        if self.button.text() == "→":
            self.input2.setText(self.input1.text())
            self.input1.clear()
            self.button.setText("←")
        else:
            self.input1.setText(self.input2.text())
            self.input2.clear()
            self.button.setText("→")


if __name__ == "__main__":
    app = QApplication([])
    window = WordSwitcher()
    window.show()
    app.exec()
