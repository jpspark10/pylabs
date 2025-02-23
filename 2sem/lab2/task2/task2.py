import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtCore import QDateTime
from PyQt6 import uic


class SchedulerApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('scheduler.ui', self)
        self.addButton.clicked.connect(self.add_event)
        self.setFixedSize(400, 300)

    def add_event(self):
        try:
            event_name = self.eventNameLineEdit.text().strip()
            if not event_name:
                return
            selected_date = self.calendarWidget.selectedDate()
            selected_time = self.timeEdit.time()
            event_datetime = QDateTime(selected_date, selected_time)
            event_item = f"{event_datetime.toString('yyyy-MM-dd hh:mm')}: {event_name}"
            self.eventListWidget.addItem(event_item)
            self.sort_events()
            self.eventNameLineEdit.clear()
            QMessageBox.information(self, "Событие добавлено", f"Добавлено: {event_item}")
        except Exception as e:
            print(str(e))

    def sort_events(self):
        try:
            items = []
            for i in range(self.eventListWidget.count()):
                item_text = self.eventListWidget.item(i).text()
                date_part = item_text.split(": ", 1)[0]
                dt = QDateTime.fromString(date_part, "yyyy-MM-dd hh:mm")
                if dt.isValid():
                    items.append((dt, item_text))
            if not items:
                return
            items.sort(key=lambda x: x[0])
            self.eventListWidget.clear()
            for _, text in items:
                self.eventListWidget.addItem(text)
        except Exception as e:
            print("Ошибка при сортировке:", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SchedulerApp()
    window.show()
    sys.exit(app.exec())
