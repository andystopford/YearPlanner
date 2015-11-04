#!/usr/bin/python
# -*- coding: utf-8 -*-
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
#import datetime
import sys
sys.path.append("./UI")
import itertools
#from calendar import*
import calendar
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import inspect, types
from EventPopup import Ui_Window



class Year:
    def __init__(self, parent, year):
        """ Make list of the year's dates sorted by month """
        self.test = "Nothing"
        self.cal = calendar.Calendar()
        self.year = year
        self.parent = parent
        self.date_list = []
        self.month_list = []        
        #self.get_days()
        #return self.test
       
    def get_months(self):
        for month in range(1, 13):
            self.days = self.cal.monthdayscalendar(self.year, month)

            self.days = list(itertools.chain(*self.days))   # 12 lists of dates
            for n, i in enumerate(self.days):
                if i == 0:
                    self.days[n] = ''   # Removes Zeros at beginning of month
            self.days += ['']*(37 - len(self.days)) #pads list to fill table
            self.month_list.append(self.days)
            
            day_num = 0
            for day in self.days:
                day = str(day)
                if day != "0":
                    date = Date(self. parent, (month-1, day_num), day)
                    self.date_list.append(date)
                day_num += 1
        return self.month_list   


    def get_indices(self, date_list):
        for date in date_list:
            parent = date.get_parent()
            posn = date.get_posn()
            day = date.get_day()         
            day = QString(day)
            cell = CellWidget(day)
            cell.store_date(date)
            self.index = (posn[0], posn[1])
            #self.index.column = posn[0]
            #self.index.row = posn[1]
            self.index_list.append(self.index)
            self.test = "OK"

            


class Date():
    def __init__(self, parent, posn, day):
        """ Instanciate dates """
        self.parent = parent
        self.posn = posn
        self.day = day
    def get_parent(self):
        return self.parent
    def get_posn(self):
        return self.posn
    def get_day(self):
        return self.day

        
class Cell:
    def __init__(self):
        pass
    def init_cells(self, date_list):
        """ Instanciates CellWidget for each cell """
        for date in date_list:
            parent = date.get_parent()
            posn = date.get_posn()
            day = date.get_day()         
            day = QString(day)
            cell = CellWidget(day)
            cell.store_date(date)
            index = QModelIndex()
            index.column = posn[0]
            index.row = posn[1]
            return index
            #parent.setIndexWidget(index, cell)
            #for x in range(0, 37):
            #    parent.resizeColumnToContents(x)
            #for x in range(0, 12):
            #    parent.resizeRowToContents(x)


class CellWidget(QWidget):

    def __init__(self, day_num):        
        super(CellWidget, self).__init__()
        if day_num == "1":
            self.set_fill =1
        else:
            self.set_fill =0
        self.date_box = QVBoxLayout()
        self.day_num = QLabel(day_num)
        self.date_box.addWidget(self.day_num)
        self.day_num.setAlignment(Qt.AlignHCenter)
        #self.parent = parent
        self.hbox = QHBoxLayout()
        self.left_box = QVBoxLayout()
        self.right_box = QVBoxLayout()
        self.hbox.addLayout(self.left_box)
        self.hbox.addLayout(self.right_box)
        self.date_box.addLayout(self.hbox)
        self.setLayout(self.date_box)

        self.date = ""
        self.left_box.setSpacing(0)
        self.right_box.setSpacing(0)  
        self.red_marker_count = 0
        self.blue_marker_count = 0 

    """
    def paintEvent(self, event):
        if self.set_fill == 1:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.fill_weekend(event, qp)
            qp.end()

    def fill_weekend(self, event, qp):      
        qp.fillRect(QtCore.QRect(0, 0, 32, 52),QtGui.QColor(188, 250, 213)) 
    """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mark_red()
        if event.button() == Qt.RightButton:
            self.get_date()
            #self.mark_blue()

    def store_date(self, date):
        self.date = date

    def get_date(self):
        day = self.date.get_day()
        month = self.date.get_posn()
        self.popup = EventPopup(day, month[0])

    def mark_red(self):
        marker = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap("red_square.png")
        marker.setPixmap(pixmap)
        self.left_box.addWidget(marker)
        self.red_marker_count += 1
                
    def mark_blue(self):
        marker = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap("blue_square.png")
        marker.setPixmap(pixmap)
        self.right_box.addWidget(marker)
        self.blue_marker_count += 1


class EventPopup(QMainWindow):
    def __init__(self, day, month):
        QtGui.QWidget.__init__(self)
        self.evp_ui = Ui_Window()
        self.evp_ui.setupUi(self)
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
        "Aug", "Sept", "Oct", "Nov", "Dec"]
        day = str(day)
        month = months[month]
        date = day + ' ' + month
        self.evp_ui.display_date.setText(date)
        horiz_header = self.evp_ui.table.horizontalHeader()
        horiz_header.setResizeMode(QtGui.QHeaderView.Stretch)
        vert_header = self.evp_ui.table.verticalHeader()
        vert_header.setResizeMode(QtGui.QHeaderView.Stretch)
        self.show()



        



