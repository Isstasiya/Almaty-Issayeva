# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_school_task.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_School_task(object):
    def setupUi(self, School_task):
        School_task.setObjectName("School_task")
        School_task.resize(191, 199)
        self.create = QtWidgets.QPushButton(School_task)
        self.create.setGeometry(QtCore.QRect(100, 160, 88, 34))
        self.create.setObjectName("create")
        self.task = QtWidgets.QLineEdit(School_task)
        self.task.setGeometry(QtCore.QRect(0, 30, 151, 32))
        self.task.setObjectName("task")
        self.label = QtWidgets.QLabel(School_task)
        self.label.setGeometry(QtCore.QRect(0, 100, 58, 18))
        self.label.setObjectName("label")
        self.time = QtWidgets.QTimeEdit(School_task)
        self.time.setGeometry(QtCore.QRect(0, 120, 118, 32))
        self.time.setObjectName("time")
        self.week_day = QtWidgets.QLineEdit(School_task)
        self.week_day.setGeometry(QtCore.QRect(0, 60, 111, 32))
        self.week_day.setObjectName("week_day")

        self.retranslateUi(School_task)
        QtCore.QMetaObject.connectSlotsByName(School_task)

    def retranslateUi(self, School_task):
        _translate = QtCore.QCoreApplication.translate
        School_task.setWindowTitle(_translate("School_task", "School_task"))
        self.create.setText(_translate("School_task", "Создать"))
        self.task.setText(_translate("School_task", "Задача"))
        self.label.setText(_translate("School_task", "Время"))
        self.week_day.setText(_translate("School_task", "День недели"))
