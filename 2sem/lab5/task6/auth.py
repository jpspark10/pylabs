import sys
from PyQt5 import QtWidgets, uic
from utils import hash_password, is_valid_password
import database

class AuthWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/auth.ui", self)
        # Предполагается, что в auth.ui есть:
        # QLineEdit: loginLineEdit, passwordLineEdit
        # QPushButton: loginButton, registerButton
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)

    def login(self):
        login = self.loginLineEdit.text()
        password = self.passwordLineEdit.text()
        password_hash = hash_password(password)
        if database.verify_user(login, password_hash):
            self.accept()  # авторизация успешна
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")

    def register(self):
        login = self.loginLineEdit.text()
        password = self.passwordLineEdit.text()
        if not is_valid_password(password):
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пароль не соответствует требованиям!")
            return
        password_hash = hash_password(password)
        if database.register_user(login, password_hash):
            QtWidgets.QMessageBox.information(self, "Успех", "Пользователь успешно зарегистрирован!")
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Логин уже существует!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    database.init_db()
    auth_window = AuthWindow()
    if auth_window.exec_() == QtWidgets.QDialog.Accepted:
        # Если авторизация успешна, запускаем главное окно
        from mainwindow import MainWindow
        main_win = MainWindow()
        main_win.show()
        sys.exit(app.exec_())
