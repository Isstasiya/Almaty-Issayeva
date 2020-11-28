# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_big_task.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Big_task(object):
    def setupUi(self, Big_task):
        Big_task.setObjectName("Big_task")
        Big_task.resize(240, 161)
        self.create = QtWidgets.QPushButton(Big_task)
        self.create.setGeometry(QtCore.QRect(150, 120, 88, 34))
        self.create.setObjectName("create")
        self.task = QtWidgets.QLineEdit(Big_task)
        self.task.setGeometry(QtCore.QRect(0, 10, 151, 32))
        self.task.setObjectName("task")
        self.label_important = QtWidgets.QLabel(Big_task)
        self.label_important.setGeometry(QtCore.QRect(10, 110, 81, 18))
        self.label_important.setObjectName("label_important")
        self.important = QtWidgets.QSpinBox(Big_task)
        self.important.setGeometry(QtCore.QRect(80, 100, 51, 32))
        self.important.setObjectName("important")
        self.clas = QtWidgets.QLineEdit(Big_task)
        self.clas.setGeometry(QtCore.QRect(0, 40, 151, 32))
        self.clas.setObjectName("clas")
        self.deadline = QtWidgets.QDateTimeEdit(Big_task)
        self.deadline.setGeometry(QtCore.QRect(0, 70, 194, 32))
        self.deadline.setObjectName("deadline")

        self.retranslateUi(Big_task)
        QtCore.QMetaObject.connectSlotsByName(Big_task)

    def retranslateUi(self, Big_task):
        _translate = QtCore.QCoreApplication.translate
        Big_task.setWindowTitle(_translate("Big_task", "Frame"))
        self.create.setText(_translate("Big_task", "Create"))
        self.task.setText(_translate("Big_task", "Task"))
        self.label_important.setText(_translate("Big_task", "Важность"))
        self.clas.setText(_translate("Big_task", "Class"))
