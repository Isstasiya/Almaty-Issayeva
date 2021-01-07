import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5 import uic, QtWidgets
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.k = 'ufo.gif'
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.nm = QPixmap(self.k)
        self.qw = QLabel(self)
        self.qw.setPixmap(self.nm)
        self.qw.move(0, 0)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            if self.qw.y() - 10 < 0:
                self.qw.move(self.qw.x(), 540)
            else:
                self.qw.move(self.qw.x(), self.qw.y() - 10)
        elif event.key() == Qt.Key_Down:
            if self.qw.y() + 10 > 540:
                self.qw.move(self.qw.x(), 0)
            else:
                self.qw.move(self.qw.x(), self.qw.y() + 10)
        elif event.key() == Qt.Key_Right:
            if self.qw.x() + 10 > 540:
                self.qw.move(0, self.qw.y())
            else:
                self.qw.move(self.qw.x() + 10, self.qw.y())
        elif event.key() == Qt.Key_Left:
            if self.qw.x() - 10 < 0:
                self.qw.move(540, self.qw.y())
            else:
                self.qw.move(self.qw.x() - 10, self.qw.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())