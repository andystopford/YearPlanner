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
from PyQt4 import QtCore, QtGui
import inspect, types
from EventPopup import Ui_Window



class Year:
    def __init__(self, parent, year):
        """ Make list of the year's dates sorted by month """
        self.cal = calendar.Calendar()
        self.year = year
        self.parent = parent
        self.date_list = []        
        self.get_days()
       
    def get_days(self):
        for month in range(1, 13):
            self.days = self.cal.monthdayscalendar(self.year, month)
            self.days = list(itertools.chain(*self.days))
            day_num = 0
            for day in self.days:
                day = str(day)
                if day != "0":
                    date = Date(self. parent, (month-1, day_num), day)
                    self.date_list.append(date)
                day_num += 1
        cell = Cell()
        cell.init_cells(self.date_list)


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
        """ Instanciates a QGraphicsScene for each cell and adds
        the date display"""
        for date in date_list:
            self.scene = QScene()
            self.scene.store_date(date)
            self.view = QtGui.QGraphicsView()
            self.view.setScene(self.scene)
            self.view.setSceneRect(0, 0, 35, 52) 
            self.transform = QtGui.QTransform()  
            parent = date.get_parent()
            posn = date.get_posn()
            day = date.get_day()         
            #parent.setCellWidget(posn[0], posn[1], self.view)  
            text = QtCore.QString(day)
            #text = self.scene.addText(text)       
            #text.setTransform(self.transform.translate(3, -5))
            # New...
            temp = CellWidget(parent)
            parent.setCellWidget(posn[0], posn[1], temp)
            for x in range(0, 37):
                parent.resizeColumnToContents(x)
            for x in range(0, 12):
                parent.resizeRowToContents(x)


class CellWidget(QtGui.QWidget):

    def __init__(self, parent):        
        super(CellWidget, self).__init__(parent)
        self.layout = QtGui.QGridLayout(self)

        self.button1 = QtGui.QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QtGui.QPushButton("Button 2")
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)


class QScene(QtGui.QGraphicsScene):
    def __init__(self, *args, **kwds):
        QtGui.QGraphicsScene.__init__(self, *args, **kwds)

        self.font = QtGui.QFont('Times', 8)
        self.color_pen = QtGui.QColor()
        self.color_pen.setRgb(0,0,255)
        self.color_brush = QtGui.QColor()
        self.color_brush.setRgb(255,0,0)
        self.color_brush.setAlpha(127)
        self.brush = QtGui.QBrush()
        self.brush.setColor(self.color_brush)
        self.brush.setStyle(1)
        self.pen = QtGui.QPen()
        self.pen.setColor(self.color_pen) 
        self.date = ""

    def store_date(self, date):
        self.date = date

    def get_date(self):
        day = self.date.get_day()
        month = self.date.get_posn()
        self.popup = EventPopup(day, month[0])

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            item = QtGui.QGraphicsTextItem("CLICK")
            item.setPos(event.scenePos())
            self.addItem(item)
            self.insert_marker()
            self.get_content()
        if event.button() == QtCore.Qt.RightButton:
            self.get_date()

    def insert_marker(self):
        self.color_brush.setRgb(0,0,255)
        self.brush.setColor(self.color_brush)
        self.addRect(0, 20, 10, 10, pen = self.pen, brush = self.brush)

    def get_content(self):
        item_list = self.items()
        for item in item_list:
            if type(item) == QtGui.QGraphicsTextItem:
                text = item.toPlainText()
                self.popup = MyPopup(text)
                

class EventPopup(QtGui.QMainWindow):
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

        #self.scrollLayout = QtGui.QFormLayout()
        #self.evp_ui.scrollArea.setLayout(self.scrollLayout)
        #event_form = EventForm()
        #self.scrollLayout.addRow(event_form)



class EventForm(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.event_form = QtGui.QWidget(self)
        self.event_form.setGeometry(0, 0, 284, 120)
        self.table = QtGui.QTableWidget(1, 2)
        self.table.setGeometry(0, 0, 256, 51)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.event_form )
        layout.addWidget(self.table)
        self.setLayout(layout)


class MyPopup(QtGui.QWidget):
    def __init__(self, text):
        QtGui.QWidget.__init__(self)
        self.text = text
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()

    def message(self, text):
        msg = QtGui.QPainter(self)
        msg.begin(self)
        text = QtGui.QStaticText(text)
        msg.drawStaticText(0, 0, text)

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()
        
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)
        



