from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}


class MorseCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.input_field = QLineEdit(self)
        self.layout.addWidget(self.input_field)

        grid_layout = QGridLayout()
        row, col = 0, 0

        for letter, code in MORSE_CODE.items():
            button = QPushButton(letter, self)
            button.setFixedSize(40, 40)
            button.clicked.connect(lambda _, c=code: self.add_morse_code(c))
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 5:
                col = 0
                row += 1

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)
        self.setWindowTitle("Азбука Морзе")

    def add_morse_code(self, code):
        self.input_field.setText(self.input_field.text() + " " + code)


if __name__ == "__main__":
    app = QApplication([])
    window = MorseCodeApp()
    window.show()
    app.exec()
