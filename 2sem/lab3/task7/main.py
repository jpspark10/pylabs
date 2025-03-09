from PyQt6.QtWidgets import QApplication
from ui_mainwindow import PasswordCheckerApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordCheckerApp()
    window.show()
    sys.exit(app.exec())
