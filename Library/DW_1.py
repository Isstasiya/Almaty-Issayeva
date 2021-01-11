import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QPushButton, QListWidgetItem, QApplication
from untitled import Ui_Frame
from genre import Ui_MainWindow
import datetime as dt
from PyQt5 import uic, QtWidgets
from PIL.ImageQt import ImageQt
from PIL import Image
from PyQt5.QtGui import QPixmap, QBitmap


class Example(QMainWindow, Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.t = False
        self.comboBox.addItems(["название", "автор", "серия"])
        self.connection = sqlite3.connect("database")
        self.pushButton.clicked.connect(self.nk)
        self.show()
    
    def nk(self):
            self.listWidget.clear()
            w = self.lineEdit.text()
            if self.comboBox.currentText() == "название":
                res = self.connection.cursor().execute(f"""SELECT book_id, name FROM books WHERE name LIKE '%{w}%'""").fetchall()
            elif self.comboBox.currentText() == "автор":
                res = self.connection.cursor().execute(f"""SELECT book_id, name FROM books WHERE author_id IN
                                                           (SELECT author_id FROM authors WHERE name LIKE '%{w}%')""").fetchall()
            else:
                res = self.connection.cursor().execute(f"""SELECT book_id, name FROM books WHERE series_id IN
                                                           (SELECT series_id FROM series WHERE name LIKE '%{w}%')""").fetchall()
            qw = [QPushButton(str(i[0]) + "." + i[1], self) for i in res]
            for btn in qw:
                btn.clicked.connect(self.ng)
            ty = [QListWidgetItem() for _ in qw]
            for i in range(len(ty)):
                self.listWidget.addItem(ty[i])
                ty[i].setSizeHint(qw[i].sizeHint())
                self.listWidget.setItemWidget(ty[i], qw[i])

    def ng(self):
        self.qw = Add(self.sender().text().split(".")[0])
        self.qw.show()


class Add(QMainWindow, Ui_MainWindow):
    def __init__(self, qw):
            super().__init__()
            self.setupUi(self)
            self.connection = sqlite3.connect("database")
            res = self.connection.cursor().execute(f"""SELECT * FROM books WHERE book_id = {qw}""").fetchall()
            aut = self.connection.cursor().execute(f"""SELECT name FROM authors WHERE author_id = {res[0][3]}""").fetchall()
            gen = self.connection.cursor().execute(f"""SELECT name FROM genre WHERE genre_id = {res[0][5]}""").fetchall()
            ser = self.connection.cursor().execute(f"""SELECT name FROM series WHERE series_id = {res[0][2]}""").fetchall()
            print(res[0][1], aut, gen, ser, res[0][4])
            self.lineEdit.setText(res[0][1])
            self.lineEdit_2.setText(aut[0][0])
            self.lineEdit_5.setText(gen[0][0])
            self.lineEdit_3.setText(ser[0][0])
            self.lineEdit_4.setText(str(res[0][4]))
            if res[0][6] != "-":
                self.label.setPixmap(QPixmap(str(res[0][6])))
            else:
                self.label.setPixmap(QPixmap("resy.jpg"))
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())