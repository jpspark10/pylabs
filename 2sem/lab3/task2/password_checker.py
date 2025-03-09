from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

KEYBOARD_SEQUENCES = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю",
    "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM",
    "ЙЦУКЕНГШЩЗХЪ", "ФЫВАПРОЛДЖЭ", "ЯЧСМИТЬБЮ"
]


def check_length(password):
    return len(password) >= 9


def check_digit(password):
    return any(c.isdigit() for c in password)


def check_case(password):
    return any(c.islower() for c in password) and any(c.isupper() for c in password)


def check_keyboard_sequences(password):
    lower_password = password.lower()
    for seq in KEYBOARD_SEQUENCES:
        seq = seq.lower()
        for i in range(len(seq) - 2):
            if seq[i:i + 3] in lower_password:
                return False
    return True


def check_password(password):
    assert check_length(password), "Пароль должен быть не короче 9 символов"
    assert check_digit(password), "Пароль должен содержать хотя бы одну цифру"
    assert check_case(password), "Пароль должен содержать хотя бы одну строчную и одну заглавную букву"
    assert check_keyboard_sequences(password), "Пароль не должен содержать три подряд идущие буквы с клавиатуры"
    return True


class PasswordCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("password_checker.ui", self)
        self.checkButton.clicked.connect(self.validate_password)

    def validate_password(self):
        password = self.passwordInput.text()
        try:
            if check_password(password):
                self.resultLabel.setText("ok")
        except AssertionError as e:
            self.resultLabel.setText("error: " + str(e))


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordCheckerApp()
    window.show()
    app.exec()
