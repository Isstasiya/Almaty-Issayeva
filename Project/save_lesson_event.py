# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_lesson_event.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lesson_event(object):
    def setupUi(self, Lesson_event):
        Lesson_event.setObjectName("Lesson_event")
        Lesson_event.resize(240, 189)
        self.create = QtWidgets.QPushButton(Lesson_event)
        self.create.setGeometry(QtCore.QRect(150, 150, 88, 34))
        self.create.setObjectName("create")
        self.date_time = QtWidgets.QDateTimeEdit(Lesson_event)
        self.date_time.setGeometry(QtCore.QRect(0, 100, 194, 32))
        self.date_time.setObjectName("date_time")
        self.event = QtWidgets.QLineEdit(Lesson_event)
        self.event.setGeometry(QtCore.QRect(0, 40, 113, 32))
        self.event.setObjectName("event")
        self.label = QtWidgets.QLabel(Lesson_event)
        self.label.setGeometry(QtCore.QRect(0, 80, 58, 18))
        self.label.setObjectName("label")
        self.subject = QtWidgets.QLineEdit(Lesson_event)
        self.subject.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.subject.setObjectName("subject")

        self.retranslateUi(Lesson_event)
        QtCore.QMetaObject.connectSlotsByName(Lesson_event)

    def retranslateUi(self, Lesson_event):
        _translate = QtCore.QCoreApplication.translate
        Lesson_event.setWindowTitle(_translate("Lesson_event", "Lesson_event"))
        self.create.setText(_translate("Lesson_event", "Create"))
        self.event.setText(_translate("Lesson_event", "Event"))
        self.label.setText(_translate("Lesson_event", "Time"))
        self.subject.setText(_translate("Lesson_event", "Subject"))
