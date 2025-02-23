import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6 import uic


class NotebookApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('notebook.ui', self)
        self.addButton.clicked.connect(self.add_contact)
        self.setFixedSize(400, 300)

    def add_contact(self):
        try:
            contact_name = self.nameLineEdit.text().strip()
            contact_number = self.numberLineEdit.text().strip()
            if not contact_name or not contact_number:
                return
            contact_item = f"{contact_name}: {contact_number}"
            self.contactListWidget.addItem(contact_item)
            self.nameLineEdit.clear()
            self.numberLineEdit.clear()
            QMessageBox.information(self, "Контакт добавлен", f"Добавлен: {contact_item}")
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotebookApp()
    window.show()
    sys.exit(app.exec())
