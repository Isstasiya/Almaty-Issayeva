# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_event.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Event(object):
    def setupUi(self, Event):
        Event.setObjectName("Event")
        Event.resize(240, 147)
        self.event = QtWidgets.QLineEdit(Event)
        self.event.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.event.setObjectName("event")
        self.date_time = QtWidgets.QDateTimeEdit(Event)
        self.date_time.setGeometry(QtCore.QRect(0, 70, 194, 32))
        self.date_time.setObjectName("date_time")
        self.label = QtWidgets.QLabel(Event)
        self.label.setGeometry(QtCore.QRect(0, 50, 58, 18))
        self.label.setObjectName("label")
        self.create = QtWidgets.QPushButton(Event)
        self.create.setGeometry(QtCore.QRect(150, 110, 88, 34))
        self.create.setObjectName("create")

        self.retranslateUi(Event)
        QtCore.QMetaObject.connectSlotsByName(Event)

    def retranslateUi(self, Event):
        _translate = QtCore.QCoreApplication.translate
        Event.setWindowTitle(_translate("Event", "Event"))
        self.event.setText(_translate("Event", "Event"))
        self.label.setText(_translate("Event", "Time"))
        self.create.setText(_translate("Event", "Create"))
