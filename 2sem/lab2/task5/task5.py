import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QDoubleSpinBox, QPushButton, QStatusBar, \
    QWidget, QDialog, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Антиплагиат')
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.thresholdSpinBox = QDoubleSpinBox(self)
        self.thresholdSpinBox.setMinimum(0.0)
        self.thresholdSpinBox.setMaximum(1.0)
        self.thresholdSpinBox.setSingleStep(0.01)
        self.thresholdSpinBox.setValue(0.6)
        self.thresholdSpinBox.setPrefix('Порог: ')
        layout.addWidget(self.thresholdSpinBox)

        self.textEdit1 = QTextEdit(self)
        self.textEdit2 = QTextEdit(self)
        layout.addWidget(self.textEdit1)
        layout.addWidget(self.textEdit2)

        self.calculateButton = QPushButton('Проверить', self)
        self.calculateButton.clicked.connect(self.check_plagiarism)
        layout.addWidget(self.calculateButton)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def check_plagiarism(self):
        text1 = self.textEdit1.toPlainText().splitlines()
        text2 = self.textEdit2.toPlainText().splitlines()

        threshold = self.thresholdSpinBox.value()

        matches = 0
        total_lines = max(len(text1), len(text2))

        for i in range(total_lines):
            line1 = text1[i] if i < len(text1) else ""
            line2 = text2[i] if i < len(text2) else ""
            if line1.strip().lower() == line2.strip().lower():
                matches += 1

        similarity = matches / total_lines if total_lines > 0 else 0

        self.show_result_window(matches, total_lines, similarity)

        self.update_status(similarity, threshold)

    def show_result_window(self, matches, total_lines, similarity):
        result_dialog = QDialog(self)
        result_dialog.setWindowTitle("Результат сравнения")

        layout = QVBoxLayout(result_dialog)
        result_label = QLabel(f"Совпадений: {matches}/{total_lines}\nСхожесть: {similarity * 100:.2f}%", result_dialog)
        layout.addWidget(result_label)

        result_dialog.setLayout(layout)
        result_dialog.exec()

    def update_status(self, similarity, threshold):
        if similarity >= threshold:
            self.statusBar.showMessage(f'Плагиат найден! ({similarity * 100:.2f}%)', Qt.AlignmentFlag.AlignLeft)
            self.statusBar.setStyleSheet('color: red;')
        else:
            self.statusBar.showMessage(f'Плагиат не найден. ({similarity * 100:.2f}%)', Qt.AlignmentFlag.AlignLeft)
            self.statusBar.setStyleSheet('color: green;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AntiPlagiarism()
    window.show()
    sys.exit(app.exec())
