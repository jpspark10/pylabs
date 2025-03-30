import sys
from PyQt5 import QtWidgets, uic, QtGui
import database

DEFAULT_IMAGE_PATH = "default_book.png"


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)
        self.load_books()

        self.searchTitleButton.clicked.connect(self.search_by_title)
        self.searchAuthorButton.clicked.connect(self.search_by_author)
        self.addBookButton.clicked.connect(self.add_book)
        self.editBookButton.clicked.connect(self.edit_book)
        self.deleteBookButton.clicked.connect(self.delete_book)

    def load_books(self, books=None):
        if books is None:
            books = database.get_all_books()
        self.booksTableWidget.setRowCount(0)
        for row_number, book in enumerate(books):
            self.booksTableWidget.insertRow(row_number)
            # book: (id, title, author, year, genre, image_path)
            self.booksTableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(book[0])))
            self.booksTableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(book[1]))
            self.booksTableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(book[2]))
            self.booksTableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(book[3])))
            self.booksTableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(book[4]))
            image_path = book[5] if book[5] and book[5].strip() != "" else DEFAULT_IMAGE_PATH
            icon = QtGui.QIcon(image_path)
            item = QtWidgets.QTableWidgetItem()
            item.setIcon(icon)
            self.booksTableWidget.setItem(row_number, 5, item)

    def search_by_title(self):
        title = self.searchTitleLineEdit.text()
        books = database.search_books_by_title(title)
        self.load_books(books)

    def search_by_author(self):
        author = self.searchAuthorLineEdit.text()
        books = database.search_books_by_author(author)
        self.load_books(books)

    def add_book(self):
        dialog = BookDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            data = dialog.get_data()
            database.add_book(*data)
            self.load_books()

    def edit_book(self):
        # Редактирование выбранной книги
        current_row = self.booksTableWidget.currentRow()
        if current_row < 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите книгу для редактирования!")
            return
        book_id = int(self.booksTableWidget.item(current_row, 0).text())
        title = self.booksTableWidget.item(current_row, 1).text()
        author = self.booksTableWidget.item(current_row, 2).text()
        year = int(self.booksTableWidget.item(current_row, 3).text())
        genre = self.booksTableWidget.item(current_row, 4).text()
        image_path_item = self.booksTableWidget.item(current_row, 5)
        image_path = image_path_item.icon().name() if image_path_item.icon() else ""
        dialog = BookDialog(title, author, year, genre, image_path)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            data = dialog.get_data()
            database.update_book(book_id, *data)
            self.load_books()

    def delete_book(self):
        current_row = self.booksTableWidget.currentRow()
        if current_row < 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите книгу для удаления!")
            return
        book_id = int(self.booksTableWidget.item(current_row, 0).text())
        database.delete_book(book_id)
        self.load_books()


class BookDialog(QtWidgets.QDialog):
    def __init__(self, title="", author="", year=2020, genre="", image_path=""):
        super().__init__()
        self.setWindowTitle("Книга")
        layout = QtWidgets.QFormLayout(self)
        self.titleEdit = QtWidgets.QLineEdit(title)
        self.authorEdit = QtWidgets.QLineEdit(author)
        self.yearEdit = QtWidgets.QLineEdit(str(year))
        self.genreEdit = QtWidgets.QLineEdit(genre)
        self.imageEdit = QtWidgets.QLineEdit(image_path)
        self.browseButton = QtWidgets.QPushButton("Выбрать изображение")
        self.browseButton.clicked.connect(self.browse_image)
        layout.addRow("Название:", self.titleEdit)
        layout.addRow("Автор:", self.authorEdit)
        layout.addRow("Год издания:", self.yearEdit)
        layout.addRow("Жанр:", self.genreEdit)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.imageEdit)
        hlayout.addWidget(self.browseButton)
        layout.addRow("Изображение:", hlayout)
        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)

    def browse_image(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                            "Images (*.png *.jpg *.bmp)")
        if filename:
            self.imageEdit.setText(filename)

    def get_data(self):
        title = self.titleEdit.text()
        author = self.authorEdit.text()
        try:
            year = int(self.yearEdit.text())
        except ValueError:
            year = 0
        genre = self.genreEdit.text()
        image_path = self.imageEdit.text()
        return title, author, year, genre, image_path


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
