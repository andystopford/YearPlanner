# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1341, 718)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setAutoFillBackground(False)
        self.table.setMidLineWidth(0)
        self.table.setAlternatingRowColors(True)
        self.table.setRowCount(12)
        self.table.setColumnCount(37)
        self.table.setObjectName(_fromUtf8("table"))
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(11, item)
        self.table.horizontalHeader().setDefaultSectionSize(35)
        self.table.verticalHeader().setDefaultSectionSize(52)
        self.table.verticalHeader().setSortIndicatorShown(False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.table, 1, 0, 1, 6)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 2)
        self.button_forward = QtGui.QPushButton(self.centralwidget)
        self.button_forward.setFlat(False)
        self.button_forward.setObjectName(_fromUtf8("button_forward"))
        self.gridLayout_3.addWidget(self.button_forward, 0, 4, 1, 1)
        self.button_back = QtGui.QPushButton(self.centralwidget)
        self.button_back.setObjectName(_fromUtf8("button_back"))
        self.gridLayout_3.addWidget(self.button_back, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1341, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Jan", None))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Feb", None))
        item = self.table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mar", None))
        item = self.table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apr", None))
        item = self.table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "May", None))
        item = self.table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Jun", None))
        item = self.table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Jul", None))
        item = self.table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Aug", None))
        item = self.table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Sep", None))
        item = self.table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Oct", None))
        item = self.table.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Nov", None))
        item = self.table.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Dec", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.button_forward.setText(_translate("MainWindow", "Next", None))
        self.button_back.setText(_translate("MainWindow", "Previous", None))

