# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_lesson_task.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lesson_task(object):
    def setupUi(self, Lesson_task):
        Lesson_task.setObjectName("Lesson_task")
        Lesson_task.resize(236, 199)
        self.create = QtWidgets.QPushButton(Lesson_task)
        self.create.setGeometry(QtCore.QRect(140, 160, 88, 34))
        self.create.setObjectName("create")
        self.task = QtWidgets.QLineEdit(Lesson_task)
        self.task.setGeometry(QtCore.QRect(0, 50, 151, 32))
        self.task.setObjectName("task")
        self.label = QtWidgets.QLabel(Lesson_task)
        self.label.setGeometry(QtCore.QRect(0, 110, 58, 18))
        self.label.setObjectName("label")
        self.week_day = QtWidgets.QLineEdit(Lesson_task)
        self.week_day.setGeometry(QtCore.QRect(0, 80, 111, 32))
        self.week_day.setObjectName("week_day")
        self.subject = QtWidgets.QLineEdit(Lesson_task)
        self.subject.setGeometry(QtCore.QRect(0, 20, 113, 32))
        self.subject.setObjectName("subject")
        self.time = QtWidgets.QLineEdit(Lesson_task)
        self.time.setGeometry(QtCore.QRect(0, 130, 113, 32))
        self.time.setObjectName("time")

        self.retranslateUi(Lesson_task)
        QtCore.QMetaObject.connectSlotsByName(Lesson_task)

    def retranslateUi(self, Lesson_task):
        _translate = QtCore.QCoreApplication.translate
        Lesson_task.setWindowTitle(_translate("Lesson_task", "Lesson_task"))
        self.create.setText(_translate("Lesson_task", "Create"))
        self.task.setText(_translate("Lesson_task", "Task"))
        self.label.setText(_translate("Lesson_task", "Time"))
        self.week_day.setText(_translate("Lesson_task", "Week day"))
        self.subject.setText(_translate("Lesson_task", "Subject"))
        self.time.setText(_translate("Lesson_task", "00:00"))
