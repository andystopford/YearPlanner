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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from almanac import*
from TableModel import*
import datetime
import calendar

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
"Aug", "Sept", "Oct", "Nov", "Dec"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue",
 "Wed", "Thu", "Fri", "Sat", "Sun","Mon", "Tue", "Wed", "Thu",
  "Fri", "Sat", "Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat",
   "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon",
   "Tue"]


class MainWindow(QTableView):
    def __init__(self, *args):
        QTableView.__init__(self, *args)
        today = datetime.date.today()
        self.year = today.year
        self.cal = calendar.Calendar()
        
        horiz_header = HorizHeader(self, days)
        self.setHorizontalHeader(horiz_header)
        horiz_header.setResizeMode(QHeaderView.Stretch)
        horiz_header.setMinimumSectionSize(37)

        vert_header = VertHeader(self, months)
        self.setVerticalHeader(vert_header)
        vert_header.setResizeMode(QHeaderView.Stretch)
        vert_header.setMinimumSectionSize(52)
        
        #self.ui.button_back.clicked.connect(self.year_back)
        #self.ui.button_forward.clicked.connect(self.year_forward)
        self.col1 = QBrush(QColor(100, 250, 213))
        self.col2 = QBrush(QColor(200, 150, 213))
        self.init_calendar(self.year)
        

    def year_back(self):
        self.year -= 1
        self.init_calendar(self.year)

    def year_forward(self):
        self.year += 1
        self.init_calendar(self.year)

    def init_calendar(self, year):
        year_instance = Year(self, year)
        months = year_instance.get_months()
        self.tablemodel = TableModel(months)
        self.setModel(self.tablemodel)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            ep = event.pos() # QPoint
            ind = self.indexAt(ep)  #QModelIndex
            year_instance = Year(self, self.year)
            months = year_instance.get_months()
            print ind.column(), ind.row()
            col = ind.column()
            row = ind.row()
            month = months[row]
            day = month[col]
            print day, row + 1, self.year   # Date in dd/mm/yr format

        if event.button() == Qt.RightButton:
            ep = event.pos() # QPoint
            ind = self.indexAt(ep)  #QModelIndex
            date_data = self.tablemodel.itemData(ind)    #Data at this index
            day = date_data[0].toString() #date_data[8].type() returns cell's QBrush
            col = ind.column()
            row = ind.row()
            self.tablemodel.colour_cell(ind, Qt.BackgroundRole, QBrush(QColor(200, 150, 213)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())