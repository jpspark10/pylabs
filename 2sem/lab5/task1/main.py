import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QAbstractTableModel, Qt


class CSVTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        value = self._data.iloc[index.row(), index.column()]

        if role == Qt.DisplayRole:
            return str(value)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]
            else:
                return str(section + 1)
        return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)

        # Загружаем CSV
        self.df = pd.read_csv("rez.csv")
        self.df["school"] = self.df["login"].str.split("-").str[2]
        self.df["class"] = self.df["login"].str.split("-").str[3]

        self.model = CSVTableModel(self.df)
        self.tableView.setModel(self.model)

        self.comboBoxSchool.addItems(["Все"] + sorted(self.df["school"].unique()))
        self.comboBoxClass.addItems(["Все"] + sorted(self.df["class"].unique()))

        self.btnApplyFilter.clicked.connect(self.apply_filter)

    def apply_filter(self):
        school = self.comboBoxSchool.currentText()
        _class = self.comboBoxClass.currentText()

        filtered_df = self.df.copy()
        if school != "Все":
            filtered_df = filtered_df[filtered_df["school"] == school]
        if _class != "Все":
            filtered_df = filtered_df[filtered_df["class"] == _class]

        self.model = CSVTableModel(filtered_df)
        self.tableView.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
