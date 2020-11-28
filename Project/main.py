import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QCheckBox, QLabel, QPushButton, QTableWidgetItem, QFileDialog, QPlainTextEdit
from PyQt5 import uic, QtWidgets
from PIL.ImageQt import ImageQt
from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from planner import Ui_Planner
import datetime as dt
from save_task import Ui_Task
from save_event import Ui_Event
from save_lesson_task import Ui_Lesson_task
from save_big_task import Ui_Big_task
from save_lesson_event import Ui_Lesson_event
from save_lesson import Ui_Lesson
import sqlite3


WEEK_DAY = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def mistake(): # создание диалогового окна с выводом об ошибке
    mis = QDialog()
    wrong = QLabel("You made a mistake", mis)
    wrong.move(50, 50)
    mis.setWindowTitle("Mistake")
    mis.setWindowModality(Qt.ApplicationModal)
    mis.exec()


class Example(QMainWindow, Ui_Planner):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("/home/stasya/Desktop/Industrial programming/Project/Database/planner_db")
        desktop = QtWidgets.QApplication.desktop()
        try:
            self.view_shedule()
            self.view_task(self.task_day)
            self.view_lesson_task("school", self.school_task)
            self.view_lesson_task("additional", self.additional)
            self.view_my_event()
            self.view_big_tasks()
            self.view_week_event()
            self.view_lesson_events()
            self.change_shedule.clicked.connect(self.change_shedules)
            self.create_task.clicked.connect(self.add_for_day)
            self.create_task_2.clicked.connect(self.add_a_lesson)
            self.create_task_3.clicked.connect(self.add_a_lesson)
            self.create_school_event.clicked.connect(self.add_a_lesson_event)
            self.create_my_event.clicked.connect(self.add_a_event)
            self.create_task_week.clicked.connect(self.add_a_big_task)
            self.create_event_week.clicked.connect(self.add_a_event)
            self.open_img.clicked.connect(self.op_img)
            self.open_txt.clicked.connect(self.op_txt)
            self.show()
        except Exception:
            mistake()
    
    def rewrite(self): # обновить данные, считываетмые из таблицы
        try:
            self.view_shedule()
            self.view_my_event()
            self.view_task(self.task_day)
            self.view_big_tasks()
            self.view_lesson_events()
            self.view_lesson_task("school", self.school_task)
            self.view_lesson_task("additional", self.additional)
        except Exception:
            mistake()

    # блок функций для  взаимодействия с простыми задачами

    def add_for_day(self):
        self.task = Tasks()
        self.task.show()

    def view_task(self, widget):
        for i in reversed(range(widget.count())): 
            widget.itemAt(i).widget().setParent(None)
        cn = self.connection
        cur = cn.cursor()
        res = cur.execute("""SELECT * FROM dayly_tasks WHERE date='""" + str(dt.date.today()) + """' ORDER BY deadline, important;""")
        cn.commit()
        for i in res:
            self.tsk = QCheckBox(i[4] + "-" + i[1] + "\t" + str(i[2]), self)
            self.tsk.clicked.connect(self.did)
            widget.addWidget(self.tsk)

    # блок функций для  взаимодействия с lesson-задачами

    def add_a_lesson(self):
        self.lesson = Lesson_task()
        self.lesson.show()

    def view_lesson_task(self, clas, widget):
        global WEEK_DAY
        for i in reversed(range(widget.count())): 
            widget.itemAt(i).widget().setParent(None)
        cn = self.connection
        cur = cn.cursor()
        res = cur.execute("""SELECT * FROM view_lesson_tasks WHERE clas='""" + clas
                            + """' AND week_day='""" + WEEK_DAY[dt.date.today().weekday()] + """' ORDER BY deadline;""")
        cn.commit()
        for i in res:
            self.tsk = QCheckBox(i[1] + "-" + i[2] + "\t" + str(i[3]), self)
            self.tsk.clicked.connect(self.did)
            widget.addWidget(self.tsk)

    # блок функций для  взаимодействия с событиями

    def add_a_event(self):
        self.new_event = My_event()
        self.new_event.show()

    def view_my_event(self):
        for i in reversed(range(self.event.count())): 
            self.event.itemAt(i).widget().setParent(None)
        cn = self.connection
        cur = cn.cursor()
        res = cur.execute("""SELECT event, time FROM my_event WHERE date='""" + str(dt.date.today()) + """';""")
        cn.commit()
        for i in res:
            event = QLabel(i[1] + "-" + i[0], self)
            self.event.addWidget(event)

    # взаимодействие с событиями

    def view_week_event(self):
        cn = self.connection
        cur = cn.cursor()
        res = cur.execute("""SELECT event, date, time FROM my_event 
                            WHERE date>='""" + str(dt.date.today()) + """'ORDER BY date, time;""").fetchall()
        self.table_events.setColumnCount(3)
        self.table_events.setRowCount(0)
        for i, row in enumerate(res):
            self.table_events.setRowCount(
                self.table_events.rowCount() + 1)
            for j, el in enumerate(row):
                self.table_events.setItem(
                    i, j, QTableWidgetItem(str(el)))
        self.table_events.resizeColumnsToContents()

    # блок функций для  взаимодействия с big-задачами

    def add_a_big_task(self):
        self.wek = Big_task()
        self.wek.show()

    def view_big_tasks(self):
        for i in reversed(range(self.task_week.count())): 
            self.task_week.itemAt(i).widget().setParent(None)
        cn = self.connection
        cur = cn.cursor()
        res = cur.execute("""SELECT * FROM big_tasks ORDER BY clas, deadline, important;""")
        cn.commit()
        for i in res:
            self.tsk = QCheckBox(i[4] + "-" + i[3] + "\t" + i[1] + "\t" + str(i[2]), self)
            self.tsk.clicked.connect(self.did)
            self.task_week.addWidget(self.tsk)

    # взаимодействие с расписанием

    def change_shedules(self):
        self.change = Save_lesson()
        self.change.show()

    def view_shedule(self):
        for i in reversed(range(self.shedule.count())): 
            self.shedule.itemAt(i).widget().setParent(None)
        cn = self.connection
        cur = cn.cursor()
        res = cur.execute("""SELECT DISTINCT * FROM view_shedule WHERE week_day='""" + WEEK_DAY[dt.date.today().weekday()] + """' ORDER BY time;""")
        cn.commit()
        for i in res:
            print(i)
            task = QLabel(self)
            task.setText(i[1] + "-" + i[2])
            self.shedule.addWidget(task)

    # добавление школьного события

    def add_a_lesson_event(self):
        self.lesson_event = Lesson_event()
        self.lesson_event.show()

    def view_lesson_events(self):
        cn = self.connection
        cur = cn.cursor()
        res = cur.execute("""SELECT date, event, subject FROM view_lesson_events;""")
        cn.commit()
        self.event_school.setColumnCount(3)
        self.event_school.setRowCount(0)
        for i, row in enumerate(res):
            self.event_school.setRowCount(
                self.event_school.rowCount() + 1)
            for j, el in enumerate(row):
                self.event_school.setItem(
                    i, j, QTableWidgetItem(str(el)))
        self.table_events.resizeColumnsToContents()

    # показ изображения/текстового документа

    def op_img(self):
        for i in reversed(range(self.l_view.count())): 
            self.l_view.itemAt(i).widget().setParent(None)
        img = QPixmap(QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0])
        im = QLabel(self)
        im.setPixmap(img)
        self.l_view.addWidget(im)

    def op_txt(self):
        for i in reversed(range(self.l_view.count())): 
            self.l_view.itemAt(i).widget().setParent(None)
        txt = QFileDialog.getOpenFileName(self, 'Выбрать документ', '')[0]
        tx = open(txt)
        wid = QPlainTextEdit(self)
        wid.setPlainText(tx.read())
        tx.close()
        self.l_view.addWidget(wid)


    def did(self): # Удаление элемента
        s = self.sender().text().split("-")[1]
        s = s.split()[1]
        cn = self.connection
        cur = cn.cursor()
        ers = cur.execute("""SELECT task FROM lesson_tasks;""")
        t = True
        for i in ers:
            if s == i[0]:
                res = cur.execute("""DELETE FROM lesson_tasks WHERE task = '""" + s +"""';""")
                t = False
        ers = cur.execute("""SELECT task FROM big_tasks;""")
        for i in ers:
            if s == i[0]:
                res = cur.execute("""DELETE FROM big_tasks WHERE task = '""" + s +"""';""")
                t = False
        if t:    
            res = cur.execute("""DELETE FROM dayly_tasks WHERE task = '""" + s +"""';""")
        cn.commit()
        self.sender().deleteLater()



class Tasks(QMainWindow, Ui_Task): # Класс обыных задач
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.deadline.setDateTime(dt.datetime.today())
        self.create.clicked.connect(self.add_task)

    def add_task(self):
        try:
            cn = ex.connection
            cur = cn.cursor()
            res = cur.execute("""INSERT INTO dayly_tasks(task, important, date, deadline)
                                VALUES('""" + self.task.text() + """', """ + str(self.important.text())
                                            + """, '""" + str(self.deadline.date().year()) + "-" + str(self.deadline.date().month())
                                            + "-" + str(self.deadline.date().day()) + """', '"""
                                            + str(self.deadline.time().hour()) + ":" + str(self.deadline.time().minute()) + """');""")
            cn.commit()
            self.close()
            ex.rewrite()
        except Exception:
            mistake()
            self.close()


class Lesson_task(QMainWindow, Ui_Lesson_task): # Класс задач со школы и допов
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.create.clicked.connect(self.add_task)

    def add_task(self):
        try:
            global WEEK_DAY
            cn = ex.connection
            cur = cn.cursor()
            if self.week_day.text() not in WEEK_DAY:
                raise Exception
            sub_id = cur.execute("""SELECT subject_id FROM subject WHERE subject_name = '""" + self.subject.text() + """';""")
            for i in sub_id:
                s_id = i[0]
                break
            res = cur.execute("""INSERT INTO lesson_tasks(subject_id, deadline, week_day, task)
                                VALUES(""" + str(s_id) + """, '""" + self.time.text() + """', '""" + self.week_day.text() + """', '"""
                                            + self.task.text() + """');""")
            cn.commit()
            self.close()
            ex.rewrite()
        except Exception:
            mistake()
            self.close()


class My_event(QMainWindow, Ui_Event): # Класс событий
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.date_time.setDateTime(dt.datetime.today())
        self.create.clicked.connect(self.add_event)

    def add_event(self):
        try:
            cn = ex.connection
            cur = cn.cursor()
            res = cur.execute("""INSERT INTO my_event(event, date, time)
                                VALUES('""" + self.event.text() + """', '""" + str(self.date_time.date().year()) + "-" + str(self.date_time.date().month())
                                            + "-" + str(self.date_time.date().day()) + """', '"""
                                            + str(self.date_time.time().hour()) + ":" + str(self.date_time.time().minute()) + """');""")
            cn.commit()
            self.close()
            ex.rewrite()
        except Exception:
            mistake()
            self.close()


class Big_task(QMainWindow, Ui_Big_task): # Класс задач на неделю/спринт
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.deadline.setDateTime(dt.datetime.today())
        self.create.clicked.connect(self.add_task)

    def add_task(self):
        try:
            cn = ex.connection
            cur = cn.cursor()
            res = cur.execute("""INSERT INTO big_tasks(task, important, clas, deadline)
                                VALUES('""" + self.task.text() + """', """ + str(self.important.text())
                                            + """, '""" + self.clas.text() + """', '"""
                                            + str(self.deadline.time().hour()) + ":" + str(self.deadline.time().minute()) + """');""")
            cn.commit()
            self.close()
            ex.rewrite()
        except Exception:
            mistake()
            self.close()


class Lesson_event(QMainWindow, Ui_Lesson_event): # Класс расписания зумов и мероприятий, дедлайнов
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.date_time.setDateTime(dt.datetime.today())
        self.create.clicked.connect(self.add_event)

    def add_event(self):
        try:
            cn = ex.connection
            cur = cn.cursor()
            sub_id = cur.execute("""SELECT subject_id FROM subject WHERE subject_name = '""" + self.subject.text() + """';""")
            for i in sub_id:
                s_id = i[0]
                break
            res = cur.execute("""INSERT INTO lesson_event(event, subject_id, date, time)
                                VALUES('""" + self.event.text() + """', """ + str(s_id)
                                            + """, '""" + str(self.date_time.date().year()) + "-" + str(self.date_time.date().month())
                                            + "-" + str(self.date_time.date().day()) + """', '"""
                                            + str(self.date_time.time().hour()) + ":" + str(self.date_time.time().minute()) + """');""")
            cn.commit()
            self.close()
            ex.rewrite()
        except Exception:
            mistake()
            self.close()


class Save_lesson(QMainWindow, Ui_Lesson): # Класс расписания
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.create.clicked.connect(self.add_lesson)
        self.remove.clicked.connect(self.remove_lesson)

    def add_lesson(self):
            cn = ex.connection
            cur = cn.cursor()
            sub_id = cur.execute("""SELECT subject_id FROM subject WHERE subject_name = '""" + self.subject.text() + """';""")
            for i in sub_id:
                s_id = i[0]
                break
            res = cur.execute("""INSERT INTO shedule(subject_id, week_day, time)
                                VALUES(""" + str(s_id) + """, '""" + self.week_day.text() + """', '"""
                                            + self.time.text() + """');""")
            cn.commit()
            self.close()
            ex.rewrite()

    def remove_lesson(self):
            cn = ex.connection
            cur = cn.cursor()
            sub_id = cur.execute("""SELECT subject_id FROM subject WHERE subject_name = '""" + self.subject.text() + """';""")
            for i in sub_id:
                s_id = i[0]
                break
            res = cur.execute("""DELETE FROM shedule
                                 WHERE subject_id = '""" + str(s_id) + """' AND week_day='""" + self.week_day.text() + """';""")
            cn.commit()
            self.close()
            ex.rewrite()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())