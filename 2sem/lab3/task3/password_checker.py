from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


KEYBOARD_SEQUENCES = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю",
    "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM",
    "ЙЦУКЕНГШЩЗХЪ", "ФЫВАПРОЛДЖЭ", "ЯЧСМИТЬБЮ"
]


def check_password(password):
    if len(password) < 9:
        raise LengthError("Пароль должен быть не короче 9 символов")

    if not any(c.isdigit() for c in password):
        raise DigitError("Пароль должен содержать хотя бы одну цифру")

    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        raise LetterError("Пароль должен содержать хотя бы одну строчную и одну заглавную букву")

    lower_password = password.lower()
    for seq in KEYBOARD_SEQUENCES:
        seq = seq.lower()
        for i in range(len(seq) - 2):
            if seq[i:i + 3] in lower_password:
                raise SequenceError("Пароль не должен содержать три подряд идущие буквы с клавиатуры")

    return "ok"


class PasswordCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("password_checker.ui", self)
        self.pushButton.clicked.connect(self.validate_password)

    def validate_password(self):
        password = self.lineEdit.text()
        try:
            result = check_password(password)
            self.label.setText(result)
        except PasswordError as e:
            self.label.setText(f"error: {str(e)}")


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordCheckerApp()
    window.show()
    app.exec()
