import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt
from random import randint

class ZarAtmaSimulatoru(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zar Atma Simulatoru")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 30)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Zar At", self)
        self.button.setGeometry(100, 100, 100, 30)
        self.button.clicked.connect(self.zar_at)

    def zar_at(self):
        zar = randint(1, 6)
        self.label.setText(f"Atılan zar: {zar}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    zar_simulatoru = ZarAtmaSimulatoru()
    zar_simulatoru.show()
    sys.exit(app.exec_())
