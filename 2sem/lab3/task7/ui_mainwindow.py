from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import uic
from logger import logger
from password_checker import check_password, PasswordError, LengthError, LetterError, DigitError, SequenceError, \
    WordError


class PasswordCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        logger.info("Загружается UI")
        try:
            uic.loadUi("password_checker.ui", self)
            logger.info("UI успешно загружен")
        except Exception as e:
            logger.error(f"Ошибка при загрузке UI: {str(e)}")
            raise e
        self.passwords = []
        self.dictionary = self.load_dictionary("dictionary.txt")

        self.pushButtonBrowseFile.clicked.connect(self.open_password_file)
        self.pushButtonCheckPassword.clicked.connect(self.check_passwords)

    def load_dictionary(self, file_name):
        try:
            logger.info(f"Загружается словарь из файла: {file_name}")
            with open(file_name, "r") as f:
                dictionary = set(f.read().splitlines())
            logger.info("Словарь успешно загружен")
            return dictionary
        except FileNotFoundError:
            logger.error(f"Файл словаря не найден: {file_name}")
            self.labelFileStatus.setText("Файл словаря не найден")
        except Exception as e:
            logger.error(f"Ошибка при загрузке словаря: {str(e)}")
            self.labelFileStatus.setText(f"Ошибка: {str(e)}")

    def open_password_file(self):
        try:
            logger.info("Открыт диалог для выбора файла с паролями")
            file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл с паролями", "",
                                                       "Text Files (*.txt);;All Files (*)")
            if file_name:
                self.labelFileName.setText(file_name)
                self.load_passwords(file_name)
        except Exception as e:
            logger.error(f"Ошибка при открытии файла с паролями: {str(e)}")
            self.labelFileStatus.setText(f"Ошибка: {str(e)}")

    def load_passwords(self, file_name):
        try:
            logger.info(f"Загружается файл с паролями: {file_name}")
            with open(file_name, "r") as f:
                self.passwords = f.read().splitlines()
            logger.info(f"Файл с паролями успешно загружен. Найдено {len(self.passwords)} паролей.")
        except Exception as e:
            logger.error(f"Ошибка при загрузке паролей: {str(e)}")

    def check_passwords(self):
        result_text = ""
        error_counts = {LengthError: 0, LetterError: 0, DigitError: 0, SequenceError: 0, WordError: 0}

        for password in self.passwords:
            logger.info(f"Проверяем пароль: {password}")
            try:
                result = check_password(password, self.dictionary)
                logger.info(f"Пароль '{password}' прошел проверку")
            except PasswordError as e:
                logger.error(f"Ошибка при проверке пароля '{password}': {str(e)}")
                error_counts[type(e)] += 1

        sorted_errors = sorted(error_counts.items(), key=lambda x: x[0].__name__)

        result_text += "\nСтатистика ошибок:\n"
        for error, count in sorted_errors:
            result_text += f"{error.__name__} - {count}\n"

        if hasattr(self, 'textEditResult'):
            self.textEditResult.setText(result_text)
        else:
            logger.error("textEditResult не найден, не удалось обновить результат на интерфейсе.")


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordCheckerApp()
    window.show()
    app.exec()
