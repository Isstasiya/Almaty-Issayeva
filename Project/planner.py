# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'planner.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Planner(object):
    def setupUi(self, Planner):
        Planner.setObjectName("Planner")
        Planner.resize(420, 320)
        self.planner = QtWidgets.QTabWidget(Planner)
        self.planner.setGeometry(QtCore.QRect(-10, 0, 431, 321))
        self.planner.setMinimumSize(QtCore.QSize(431, 321))
        self.planner.setMaximumSize(QtCore.QSize(431, 321))
        self.planner.setObjectName("planner")
        self.day = QtWidgets.QWidget()
        self.day.setEnabled(True)
        self.day.setObjectName("day")
        self.label_school = QtWidgets.QLabel(self.day)
        self.label_school.setGeometry(QtCore.QRect(230, 10, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_school.setFont(font)
        self.label_school.setObjectName("label_school")
        self.label_dop = QtWidgets.QLabel(self.day)
        self.label_dop.setGeometry(QtCore.QRect(10, 130, 141, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dop.setFont(font)
        self.label_dop.setObjectName("label_dop")
        self.label_task = QtWidgets.QLabel(self.day)
        self.label_task.setGeometry(QtCore.QRect(230, 150, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_task.setFont(font)
        self.label_task.setObjectName("label_task")
        self.label_event = QtWidgets.QLabel(self.day)
        self.label_event.setGeometry(QtCore.QRect(10, 10, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_event.setFont(font)
        self.label_event.setObjectName("label_event")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.day)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 171, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.event = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.event.setContentsMargins(0, 0, 0, 0)
        self.event.setObjectName("event")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.day)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(230, 170, 171, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.task_day = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.task_day.setContentsMargins(0, 0, 0, 0)
        self.task_day.setObjectName("task_day")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.day)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(230, 30, 171, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.school_task = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.school_task.setContentsMargins(0, 0, 0, 0)
        self.school_task.setObjectName("school_task")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.day)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 170, 171, 101))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.additional = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.additional.setContentsMargins(0, 0, 0, 0)
        self.additional.setObjectName("additional")
        self.create_task = QtWidgets.QPushButton(self.day)
        self.create_task.setGeometry(QtCore.QRect(320, 150, 81, 21))
        self.create_task.setObjectName("create_task")
        self.create_task_2 = QtWidgets.QPushButton(self.day)
        self.create_task_2.setGeometry(QtCore.QRect(320, 10, 81, 21))
        self.create_task_2.setObjectName("create_task_2")
        self.create_task_3 = QtWidgets.QPushButton(self.day)
        self.create_task_3.setGeometry(QtCore.QRect(100, 150, 81, 21))
        self.create_task_3.setObjectName("create_task_3")
        self.create_my_event = QtWidgets.QPushButton(self.day)
        self.create_my_event.setGeometry(QtCore.QRect(100, 10, 81, 21))
        self.create_my_event.setObjectName("create_my_event")
        self.planner.addTab(self.day, "")
        self.week = QtWidgets.QWidget()
        self.week.setObjectName("week")
        self.label_task_week = QtWidgets.QLabel(self.week)
        self.label_task_week.setGeometry(QtCore.QRect(10, 10, 71, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_task_week.setFont(font)
        self.label_task_week.setObjectName("label_task_week")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.week)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 160, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.task_week = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.task_week.setContentsMargins(0, 0, 0, 0)
        self.task_week.setObjectName("task_week")
        self.create_task_week = QtWidgets.QPushButton(self.week)
        self.create_task_week.setGeometry(QtCore.QRect(80, 30, 88, 31))
        self.create_task_week.setObjectName("create_task_week")
        self.create_event_week = QtWidgets.QPushButton(self.week)
        self.create_event_week.setGeometry(QtCore.QRect(320, 30, 88, 31))
        self.create_event_week.setObjectName("create_event_week")
        self.label_event_week = QtWidgets.QLabel(self.week)
        self.label_event_week.setGeometry(QtCore.QRect(200, 10, 111, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_event_week.setFont(font)
        self.label_event_week.setObjectName("label_event_week")
        self.table_events = QtWidgets.QTableWidget(self.week)
        self.table_events.setGeometry(QtCore.QRect(200, 60, 211, 221))
        self.table_events.setObjectName("table_events")
        self.table_events.setColumnCount(0)
        self.table_events.setRowCount(0)
        self.planner.addTab(self.week, "")
        self.school = QtWidgets.QWidget()
        self.school.setObjectName("school")
        self.label_shedule = QtWidgets.QLabel(self.school)
        self.label_shedule.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_shedule.setFont(font)
        self.label_shedule.setObjectName("label_shedule")
        self.create_school_event = QtWidgets.QPushButton(self.school)
        self.create_school_event.setGeometry(QtCore.QRect(320, 40, 88, 34))
        self.create_school_event.setObjectName("create_school_event")
        self.label_event_school = QtWidgets.QLabel(self.school)
        self.label_event_school.setGeometry(QtCore.QRect(220, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_event_school.setFont(font)
        self.label_event_school.setObjectName("label_event_school")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.school)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 70, 160, 211))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.shedule = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.shedule.setContentsMargins(0, 0, 0, 0)
        self.shedule.setSpacing(0)
        self.shedule.setObjectName("shedule")
        self.change_shedule = QtWidgets.QPushButton(self.school)
        self.change_shedule.setGeometry(QtCore.QRect(80, 40, 88, 31))
        self.change_shedule.setObjectName("change_shedule")
        self.event_school = QtWidgets.QTableWidget(self.school)
        self.event_school.setGeometry(QtCore.QRect(220, 70, 191, 211))
        self.event_school.setObjectName("event_school")
        self.event_school.setColumnCount(0)
        self.event_school.setRowCount(0)
        self.planner.addTab(self.school, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.open_txt = QtWidgets.QPushButton(self.tab)
        self.open_txt.setGeometry(QtCore.QRect(287, 10, 131, 34))
        self.open_txt.setObjectName("open_txt")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 50, 411, 231))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.l_view = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.l_view.setContentsMargins(0, 0, 0, 0)
        self.l_view.setObjectName("l_view")
        self.open_img = QtWidgets.QPushButton(self.tab)
        self.open_img.setGeometry(QtCore.QRect(10, 10, 161, 34))
        self.open_img.setObjectName("open_img")
        self.planner.addTab(self.tab, "")

        self.retranslateUi(Planner)
        self.planner.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Planner)

    def retranslateUi(self, Planner):
        _translate = QtCore.QCoreApplication.translate
        Planner.setWindowTitle(_translate("Planner", "Planner"))
        self.label_school.setText(_translate("Planner", "School"))
        self.label_dop.setText(_translate("Planner", "Additional"))
        self.label_task.setText(_translate("Planner", "Tasks"))
        self.label_event.setText(_translate("Planner", "Events"))
        self.create_task.setText(_translate("Planner", "Create"))
        self.create_task_2.setText(_translate("Planner", "Create"))
        self.create_task_3.setText(_translate("Planner", "Create"))
        self.create_my_event.setText(_translate("Planner", "Create"))
        self.planner.setTabText(self.planner.indexOf(self.day), _translate("Planner", "Day"))
        self.label_task_week.setText(_translate("Planner", "Tasks"))
        self.create_task_week.setText(_translate("Planner", "Create"))
        self.create_event_week.setText(_translate("Planner", "Create"))
        self.label_event_week.setText(_translate("Planner", "Events"))
        self.planner.setTabText(self.planner.indexOf(self.week), _translate("Planner", "Week"))
        self.label_shedule.setText(_translate("Planner", "Shedule"))
        self.create_school_event.setText(_translate("Planner", "Create"))
        self.label_event_school.setText(_translate("Planner", "ZOOM, Events"))
        self.change_shedule.setText(_translate("Planner", "Change"))
        self.planner.setTabText(self.planner.indexOf(self.school), _translate("Planner", "School"))
        self.open_txt.setText(_translate("Planner", "Показать документ"))
        self.open_img.setText(_translate("Planner", "Показать изображение"))
        self.planner.setTabText(self.planner.indexOf(self.tab), _translate("Planner", "View"))