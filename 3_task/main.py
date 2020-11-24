import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.nn)
        self.show()
        self.t = False

    def nn(self):
        self.pushButton.setText = "Yes"
        self.t = True

    def paintEvent(self, event):
        if self.t:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            self.t = False
            qp.end()

    def draw(self, qp):
        x = randrange(0, 8)
        qp.setBrush(QColor(255, 255, 0))
        er = randrange(0, 40)
        for i in range(x):
            qp.drawRect(70, 70 + 30 * i, 120, 30)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())