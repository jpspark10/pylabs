from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QSpinBox, QLabel, QPlainTextEdit, QPushButton

MENU = {
    "Пицца": 500,
    "Бургер": 300,
    "Суши": 700,
    "Паста": 450
}


class RestaurantOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.order_summary = QPlainTextEdit(self)
        self.order_summary.setReadOnly(True)
        self.items = {}

        for dish, price in MENU.items():
            checkbox = QCheckBox(f"{dish} ({price} руб.)", self)
            spinbox = QSpinBox(self)
            spinbox.setMinimum(1)
            spinbox.setMaximum(10)
            spinbox.setEnabled(False)
            checkbox.toggled.connect(lambda checked, sb=spinbox: sb.setEnabled(checked))

            self.items[checkbox] = (dish, price, spinbox)
            self.layout.addWidget(checkbox)
            self.layout.addWidget(spinbox)

        self.button = QPushButton("Оформить заказ", self)
        self.button.clicked.connect(self.calculate_order)

        self.layout.addWidget(self.button)
        self.layout.addWidget(QLabel("Чек:"))
        self.layout.addWidget(self.order_summary)

        self.setLayout(self.layout)
        self.setWindowTitle("Заказ в ресторане")

    def calculate_order(self):
        total = 0
        order_details = ""

        for checkbox, (dish, price, spinbox) in self.items.items():
            if checkbox.isChecked():
                quantity = spinbox.value()
                cost = price * quantity
                total += cost
                order_details += f"{dish} x{quantity} = {cost} руб.\n"

        order_details += f"\nИтого: {total} руб."
        self.order_summary.setPlainText(order_details)


if __name__ == "__main__":
    app = QApplication([])
    window = RestaurantOrder()
    window.show()
    app.exec()
