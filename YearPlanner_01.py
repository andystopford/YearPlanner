#!/usr/bin/env python
# coding=utf8
######################################################################

#Copyright (C)2015 Andy Stopford                                
#
#This is free software: you can redistribute it and/or modify 
#under the terms of the GNU General Public License
#as published by the Free Software Foundation; version 2.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, see <http://www.gnu.org/licenses/>.

#######################################################################

import sys
sys.path.append("./modules")
sys.path.append("./UI")
from PyQt4 import QtCore, QtGui
from MainWindow import Ui_MainWindow
from almanac import*


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
        "Aug", "Sept", "Oct", "Nov", "Dec"]
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
        "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue",
         "Wed", "Thu", "Fri", "Sat", "Sun","Mon", "Tue", "Wed", "Thu",
          "Fri", "Sat", "Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat",
           "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon",
           "Tue"]

        horiz_header = self.ui.table.horizontalHeader()
        horiz_header.setResizeMode(QtGui.QHeaderView.Stretch)
        vert_header = self.ui.table.verticalHeader()
        vert_header.setResizeMode(QtGui.QHeaderView.Stretch)
        vehic_header = self.ui.table_vehicles.horizontalHeader()
        vehic_header.setResizeMode(QtGui.QHeaderView.Stretch)
        driver_header = self.ui.table_drivers.horizontalHeader()
        driver_header.setResizeMode(QtGui.QHeaderView.Stretch)

        self.init_calendar()

    def init_calendar(self):
        Year(self.ui.table, 2015)
        self.ui.label.setText("2015")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())