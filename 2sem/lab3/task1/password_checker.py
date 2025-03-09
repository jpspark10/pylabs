from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

KEYBOARD_SEQUENCES = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю",
    "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM",
    "ЙЦУКЕНГШЩЗХЪ", "ФЫВАПРОЛДЖЭ", "ЯЧСМИТЬБЮ"
]


def check_password(password):
    if len(password) < 9:
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        return False

    lower_password = password.lower()
    for seq in KEYBOARD_SEQUENCES:
        seq = seq.lower()
        for i in range(len(seq) - 2):
            if seq[i:i + 3] in lower_password:
                return False

    return True


class PasswordCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("password_checker.ui", self)
        self.checkButton.clicked.connect(self.validate_password)

    def validate_password(self):
        password = self.passwordInput.text()
        if check_password(password):
            self.resultLabel.setText("ok")
        else:
            self.resultLabel.setText("error")


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordCheckerApp()
    window.show()
    app.exec()
