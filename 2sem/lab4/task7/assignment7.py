import sys
import math
import logging
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class LSystem:
    def __init__(self, name, divisions, axiom, rules):
        logging.debug("Инициализация L-системы: name=%s, divisions=%s, axiom=%s", name, divisions, axiom)
        self.name = name
        try:
            self.divisions = int(divisions)
        except Exception as e:
            logging.error("Ошибка преобразования divisions: %s", e)
            self.divisions = 1
        self.axiom = axiom.strip()
        self.rules = {}
        for rule in rules:
            if "->" in rule:
                try:
                    key, value = rule.split("->")
                    self.rules[key.strip()] = value.strip()
                    logging.debug("Добавлено правило: %s -> %s", key.strip(), value.strip())
                except Exception as e:
                    logging.error("Ошибка при разборе правила '%s': %s", rule, e)

    def evolve(self, iterations):
        logging.debug("Эволюция L-системы на %s итераций", iterations)
        current = self.axiom
        for i in range(iterations):
            next_seq = "".join(self.rules.get(ch, ch) for ch in current)
            current = next_seq
            logging.debug("Итерация %s: %s", i + 1, current)
        return current


class DrawArea(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DrawArea, self).__init__(parent)
        self.lsystem = None
        self.iteration = 0

    def setLSystem(self, lsystem):
        self.lsystem = lsystem
        logging.debug("Установлена новая L-система: %s", lsystem.name)
        self.update()

    def setIteration(self, iteration):
        self.iteration = iteration
        logging.debug("Установлено значение итераций: %s", iteration)
        self.update()

    def paintEvent(self, event):
        if not self.lsystem:
            return
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        try:
            commands = self.lsystem.evolve(self.iteration)
        except Exception as e:
            logging.error("Ошибка в эволюции L-системы: %s", e)
            return

        try:
            angle = 360 / self.lsystem.divisions
        except Exception as e:
            logging.error("Ошибка вычисления угла: %s", e)
            angle = 90

        pos = QtCore.QPointF(self.width() / 2, self.height())
        current_angle = -90  # направлено вверх
        stack = []

        logging.debug("Начало отрисовки. Команды: %s", commands)
        try:
            painter.translate(pos)
            for ch in commands:
                if ch == "F":
                    length = 10  # длина шага
                    rad = math.radians(current_angle)
                    new_pos = QtCore.QPointF(length * math.cos(rad), length * math.sin(rad))
                    start_point = QtCore.QPointF(0, 0)
                    painter.drawLine(start_point, new_pos)
                    painter.translate(new_pos)
                elif ch == "+":
                    current_angle += angle
                elif ch == "-":
                    current_angle -= angle
                elif ch == "[":
                    stack.append((painter.transform(), current_angle))
                elif ch == "]" and stack:
                    tr, current_angle = stack.pop()
                    painter.setTransform(tr)
        except Exception as e:
            logging.error("Ошибка при отрисовке: %s", e)
        finally:
            painter.end()


class MainWindow7(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow7, self).__init__()
        try:
            uic.loadUi("assignment7.ui", self)
            logging.debug("UI файл успешно загружен.")
        except Exception as e:
            logging.critical("Ошибка загрузки UI файла: %s", e)
            sys.exit(1)

        self.drawAreaWidget = DrawArea()
        layout = QtWidgets.QVBoxLayout(self.drawArea)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.drawAreaWidget)

        self.loadFileButton.clicked.connect(self.loadLSystemFile)
        self.iterationSlider.valueChanged.connect(self.drawAreaWidget.setIteration)

    def loadLSystemFile(self):
        logging.debug("Нажата кнопка загрузки L-системы.")
        fname, _ = QFileDialog.getOpenFileName(self, "Открыть файл L-системы", "", "Text Files (*.txt)")
        if not fname:
            logging.info("Файл не выбран пользователем.")
            return
        logging.debug("Выбран файл: %s", fname)
        try:
            with open(fname, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
            logging.debug("Прочитано строк: %s", len(lines))
        except Exception as e:
            logging.error("Ошибка чтения файла: %s", e)
            QMessageBox.critical(self, "Ошибка", f"Ошибка чтения файла: {e}")
            return

        if len(lines) < 4:
            logging.error("Неверная структура файла L-системы! Строк: %s", len(lines))
            QMessageBox.warning(self, "Ошибка", "Неверная структура файла L-системы!")
            return

        try:
            name = lines[0]
            divisions = lines[1]
            axiom = lines[2]
            rules = lines[3:]
            lsystem = LSystem(name, divisions, axiom, rules)
            self.drawAreaWidget.setLSystem(lsystem)
            self.iterationSlider.setValue(0)  # Сброс слайдера
            logging.debug("L-система успешно загружена: %s", name)
        except Exception as e:
            logging.error("Ошибка при обработке файла L-системы: %s", e)
            QMessageBox.critical(self, "Ошибка", f"Ошибка при обработке файла L-системы: {e}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow7()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
