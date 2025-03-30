import sqlite3
import sys
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, \
    QMessageBox
from PyQt5.uic import loadUi

DB_PATH = 'films_db.db'


class FilmsTableModel(QAbstractTableModel):
    def __init__(self, data, columns):
        super().__init__()
        self._data = data  # переименовано чтобы не конфликтовать с методом data
        self.columns = columns

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        value = self._data[index.row()][index.column()]
        if role == Qt.DisplayRole:
            return str(value)
        return None

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]
        return None


class FilmDialog(QDialog):
    def __init__(self, parent=None, film_id=None):
        super(FilmDialog, self).__init__(parent)
        self.setWindowTitle("Add/Edit Film")
        self.film_id = film_id  # ID фильма, если редактируем

        self.db_connection = sqlite3.connect(DB_PATH)
        self.cursor = self.db_connection.cursor()

        # Элементы интерфейса
        self.titleLineEdit = QLineEdit(self)
        self.yearLineEdit = QLineEdit(self)
        self.genreComboBox = QComboBox(self)
        self.durationLineEdit = QLineEdit(self)

        self.titleLabel = QLabel("Title:", self)
        self.yearLabel = QLabel("Year:", self)
        self.genreLabel = QLabel("Genre:", self)
        self.durationLabel = QLabel("Duration:", self)

        self.saveButton = QPushButton("Save", self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.titleLineEdit)
        layout.addWidget(self.yearLabel)
        layout.addWidget(self.yearLineEdit)
        layout.addWidget(self.genreLabel)
        layout.addWidget(self.genreComboBox)
        layout.addWidget(self.durationLabel)
        layout.addWidget(self.durationLineEdit)
        layout.addWidget(self.saveButton)

        self.saveButton.clicked.connect(self.save_film)

        self.load_genres()

        if self.film_id:
            self.load_film_data()

    def load_genres(self):
        try:
            query = "SELECT id, title FROM genres"
            self.cursor.execute(query)
            genres = self.cursor.fetchall()
            for genre in genres:
                self.genreComboBox.addItem(genre[1], genre[0])  # Добавляем название жанра и его ID
        except Exception as e:
            self.show_message("Error", f"Failed to load genres: {str(e)}")
            print(f"Error loading genres: {str(e)}")  # Вывод ошибки в консоль

    def load_film_data(self):
        try:
            query = "SELECT title, year, genre, duration FROM films WHERE id = ?"
            self.cursor.execute(query, (self.film_id,))
            film = self.cursor.fetchone()
            if film:
                self.titleLineEdit.setText(film[0])
                self.yearLineEdit.setText(str(film[1]))
                self.genreComboBox.setCurrentIndex(self.genreComboBox.findData(film[2]))
                self.durationLineEdit.setText(str(film[3]))
        except Exception as e:
            self.show_message("Error", f"Failed to load film data: {str(e)}")
            print(f"Error loading film data: {str(e)}")  # Вывод ошибки в консоль

    def save_film(self):
        title = self.titleLineEdit.text()
        year = self.yearLineEdit.text()
        genre = self.genreComboBox.currentData()  # Получаем ID жанра
        duration = self.durationLineEdit.text()

        if not title or not year or not genre or not duration:
            self.show_message("Error", "All fields must be filled.")
            print("Error: All fields must be filled.")
            return

        try:
            year = int(year)
            duration = int(duration)
        except ValueError:
            self.show_message("Error", "Year and duration must be integers.")
            print("Error: Year and duration must be integers.")
            return

        try:
            if self.film_id:
                self.cursor.execute("UPDATE films SET title=?, year=?, genre=?, duration=? WHERE id=?",
                                    (title, year, genre, duration, self.film_id))
            else:
                self.cursor.execute("INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)",
                                    (title, year, genre, duration))
            self.db_connection.commit()
            self.accept()  # Закрываем окно после сохранения
        except Exception as e:
            self.show_message("Error", f"Failed to save film data: {str(e)}")
            print(f"Error saving film data: {str(e)}")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("film_ui.ui", self)
        self.db_connection = sqlite3.connect(DB_PATH)
        self.cursor = self.db_connection.cursor()

        self.load_data()

        self.addButton.clicked.connect(self.add_film)
        self.editButton.clicked.connect(self.edit_film)
        self.deleteButton.clicked.connect(self.delete_film)

    def load_data(self):
        try:
            self.cursor.execute(
                "SELECT films.id, films.title, films.year, genres.title, films.duration "
                "FROM films JOIN genres ON films.genre = genres.id"
            )
            rows = self.cursor.fetchall()
            columns = ["ID", "Title", "Year", "Genre", "Duration"]
            self.model = FilmsTableModel(rows, columns)
            self.tableView.setModel(self.model)
        except Exception as e:
            self.show_message("Error", f"Failed to load data: {str(e)}")
            print(f"Error loading data: {str(e)}")  # Вывод ошибки в консоль

    def add_film(self):
        try:
            dialog = FilmDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                self.load_data()
        except Exception as e:
            print(f"Error in add_film: {e}")
            self.show_message("Error", f"Failed to add film: {e}")

    def edit_film(self):
        try:
            selected_row = self.tableView.selectionModel().currentIndex().row()
            if selected_row == -1:
                self.show_message("Error", "No film selected for editing.")
                return
            film_id = self.model.data(self.model.index(selected_row, 0))
            dialog = FilmDialog(self, film_id)
            if dialog.exec_() == QDialog.Accepted:
                self.load_data()
        except Exception as e:
            print(f"Error in edit_film: {e}")
            self.show_message("Error", f"Failed to edit film: {e}")

    def delete_film(self):
        try:
            selected_row = self.tableView.selectionModel().currentIndex().row()
            if selected_row == -1:
                self.show_message("Error", "No film selected for deletion.")
                return
            film_id = self.model.data(self.model.index(selected_row, 0))
            # Получаем новый курсор для выполнения запроса
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM films WHERE id=?", (film_id,))
            self.db_connection.commit()
            self.load_data()
        except Exception as e:
            print(f"Error in delete_film: {e}")
            self.show_message("Error", f"Failed to delete film: {e}")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
