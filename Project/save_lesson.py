# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_lesson.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lesson(object):
    def setupUi(self, Lesson):
        Lesson.setObjectName("Lesson")
        Lesson.resize(208, 201)
        self.subject = QtWidgets.QLineEdit(Lesson)
        self.subject.setGeometry(QtCore.QRect(0, 30, 113, 32))
        self.subject.setObjectName("subject")
        self.week_day = QtWidgets.QLineEdit(Lesson)
        self.week_day.setGeometry(QtCore.QRect(0, 70, 111, 32))
        self.week_day.setObjectName("week_day")
        self.label = QtWidgets.QLabel(Lesson)
        self.label.setGeometry(QtCore.QRect(0, 110, 58, 18))
        self.label.setObjectName("label")
        self.create = QtWidgets.QPushButton(Lesson)
        self.create.setGeometry(QtCore.QRect(120, 160, 88, 34))
        self.create.setObjectName("create")
        self.remove = QtWidgets.QPushButton(Lesson)
        self.remove.setGeometry(QtCore.QRect(0, 160, 88, 34))
        self.remove.setObjectName("remove")
        self.time = QtWidgets.QLineEdit(Lesson)
        self.time.setGeometry(QtCore.QRect(0, 130, 113, 32))
        self.time.setObjectName("time")

        self.retranslateUi(Lesson)
        QtCore.QMetaObject.connectSlotsByName(Lesson)

    def retranslateUi(self, Lesson):
        _translate = QtCore.QCoreApplication.translate
        Lesson.setWindowTitle(_translate("Lesson", "Lesson"))
        self.subject.setText(_translate("Lesson", "Subject"))
        self.week_day.setText(_translate("Lesson", "Week day"))
        self.label.setText(_translate("Lesson", "Time"))
        self.create.setText(_translate("Lesson", "Create"))
        self.remove.setText(_translate("Lesson", "Remove"))
        self.time.setText(_translate("Lesson", "00:00"))
