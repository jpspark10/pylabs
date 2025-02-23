import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6 import uic
import random


class AliasGame(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('alias_game.ui', self)
        self.startButton.clicked.connect(self.start_game)
        self.takeButton.clicked.connect(self.player_turn)
        self.setFixedSize(400, 300)
        self.total_stones = 0

    def start_game(self):
        try:
            self.total_stones = int(self.stonesInput.text())
            if self.total_stones <= 0:
                raise ValueError
            self.statusLabel.setText(f"Камней на столе: {self.total_stones}")
            self.takeButton.setEnabled(True)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректное количество камней.")

    def player_turn(self):
        try:
            stones_taken = int(self.takeInput.text())
            if stones_taken < 1 or stones_taken > 3 or stones_taken > self.total_stones:
                raise ValueError
            self.total_stones -= stones_taken
            self.statusLabel.setText(f"Камней на столе: {self.total_stones}")
            if self.total_stones == 0:
                QMessageBox.information(self, "Игра окончена", "Вы выиграли!")
                self.takeButton.setEnabled(False)
                return
            self.computer_turn()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите число от 1 до 3, не превышающее количество камней.")

    def computer_turn(self):
        optimal_take = (self.total_stones - 1) % 4
        stones_taken = optimal_take if optimal_take != 0 else random.randint(1, min(3, self.total_stones))
        self.total_stones -= stones_taken
        self.statusLabel.setText(f"Камней на столе: {self.total_stones}")
        if self.total_stones == 0:
            QMessageBox.information(self, "Игра окончена", "Компьютер выиграл!")
            self.takeButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AliasGame()
    window.show()
    sys.exit(app.exec())
