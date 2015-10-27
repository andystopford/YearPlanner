# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventPopup.ui'
#
# Created by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(397, 283)
        self.centralwidget = QtGui.QWidget(Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.display_date = QtGui.QTextEdit(self.centralwidget)
        self.display_date.setMaximumSize(QtCore.QSize(16777215, 40))
        self.display_date.setObjectName(_fromUtf8("display_date"))
        self.gridLayout.addWidget(self.display_date, 0, 0, 1, 1)
        self.event_list = QtGui.QListWidget(self.centralwidget)
        self.event_list.setObjectName(_fromUtf8("event_list"))
        self.gridLayout.addWidget(self.event_list, 1, 0, 1, 1)
        self.button_add_event = QtGui.QPushButton(self.centralwidget)
        self.button_add_event.setObjectName(_fromUtf8("button_add_event"))
        self.gridLayout.addWidget(self.button_add_event, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 294, 233))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.table = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMaximumSize(QtCore.QSize(16777215, 53))
        self.table.setRowCount(1)
        self.table.setColumnCount(4)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.horizontalHeader().setDefaultSectionSize(60)
        self.gridLayout_2.addWidget(self.table, 0, 0, 1, 3)
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 3, 1)
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(_translate("Window", "MainWindow", None))
        self.button_add_event.setText(_translate("Window", "Add", None))
        self.pushButton.setText(_translate("Window", "PushButton", None))
        self.pushButton_2.setText(_translate("Window", "PushButton", None))
        self.pushButton_3.setText(_translate("Window", "PushButton", None))

