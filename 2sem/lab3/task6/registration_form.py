from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from password_checker import check_password
from phone_validator import validate_phone_number


class RegistrationForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("registration_form.ui", self)
        self.register_button.clicked.connect(self.register)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        phone_number = self.phone_input.text()

        try:
            check_password(password)
        except Exception as e:
            self.result_label.setText(f"Ошибка пароля: {str(e)}")
            return

        # Проверка номера телефона
        phone_validation_result = validate_phone_number(phone_number)
        if phone_validation_result.startswith('не'):
            self.result_label.setText(f"Ошибка телефона: {phone_validation_result}")
            return

        self.result_label.setText("Регистрация успешна!")


if __name__ == "__main__":
    app = QApplication([])
    window = RegistrationForm()
    window.show()
    app.exec()
