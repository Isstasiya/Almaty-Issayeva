import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5 import uic, QtWidgets
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.k = ['car_1.jpg', 'car_2.jpg', 'car_3.jpg']
        self.d = self.k[0]
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.nm = QPixmap(self.d)
        self.qw = QLabel(self)
        self.qw.setPixmap(self.nm)
        self.setMouseTracking(True)
        self.show()

    def mouseMoveEvent(self, event):
        if event.x() in range(0, 540) and event.y() in range(0, 540):
            self.qw.move(event.x(), event.y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            w = random.choice(self.k)
            while w == self.d:
                w = random.choice(self.k)
            self.d = w
            self.nm.load(self.d)
            self.qw.setPixmap(self.nm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())