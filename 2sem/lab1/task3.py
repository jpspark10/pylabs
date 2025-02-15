from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel


class WidgetToggler(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.widgets = [QLabel(f"Виджет {i + 1}", self) for i in range(3)]
        self.checkboxes = []

        for widget in self.widgets:
            checkbox = QCheckBox("Показать", self)
            checkbox.setChecked(True)
            checkbox.toggled.connect(lambda checked, w=widget: w.setVisible(checked))
            self.checkboxes.append(checkbox)

            self.layout.addWidget(checkbox)
            self.layout.addWidget(widget)

        self.setLayout(self.layout)
        self.setWindowTitle("Переключение виджетов")


if __name__ == "__main__":
    app = QApplication([])
    window = WidgetToggler()
    window.show()
    app.exec()
