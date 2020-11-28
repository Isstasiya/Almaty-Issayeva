# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_task.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Task(object):
    def setupUi(self, Task):
        Task.setObjectName("Task")
        Task.resize(249, 189)
        self.task = QtWidgets.QLineEdit(Task)
        self.task.setGeometry(QtCore.QRect(0, 20, 151, 32))
        self.task.setObjectName("task")
        self.label = QtWidgets.QLabel(Task)
        self.label.setGeometry(QtCore.QRect(0, 57, 61, 21))
        self.label.setObjectName("label")
        self.create = QtWidgets.QPushButton(Task)
        self.create.setGeometry(QtCore.QRect(160, 150, 88, 34))
        self.create.setObjectName("create")
        self.important = QtWidgets.QSpinBox(Task)
        self.important.setGeometry(QtCore.QRect(70, 120, 51, 32))
        self.important.setObjectName("important")
        self.label_2 = QtWidgets.QLabel(Task)
        self.label_2.setGeometry(QtCore.QRect(0, 130, 81, 18))
        self.label_2.setObjectName("label_2")
        self.deadline = QtWidgets.QDateTimeEdit(Task)
        self.deadline.setGeometry(QtCore.QRect(0, 80, 194, 32))
        self.deadline.setObjectName("deadline")

        self.retranslateUi(Task)
        QtCore.QMetaObject.connectSlotsByName(Task)

    def retranslateUi(self, Task):
        _translate = QtCore.QCoreApplication.translate
        Task.setWindowTitle(_translate("Task", "Task"))
        self.task.setText(_translate("Task", "Task"))
        self.label.setText(_translate("Task", "Deadline"))
        self.create.setText(_translate("Task", "Create"))
        self.label_2.setText(_translate("Task", "Important"))
