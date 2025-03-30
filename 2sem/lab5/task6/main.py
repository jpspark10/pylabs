import sys
from PyQt5 import QtWidgets
import database
from auth import AuthWindow


def main():
    database.init_db()
    app = QtWidgets.QApplication(sys.argv)
    auth_dialog = AuthWindow()
    if auth_dialog.exec_() == QtWidgets.QDialog.Accepted:
        from mainwindow import MainWindow
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
