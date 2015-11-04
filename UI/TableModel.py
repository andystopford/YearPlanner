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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class TableModel(QAbstractTableModel):
    def __init__(self, data_in, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.data_in = data_in
        self.test_flag = True

    def rowCount(self, parent):
        return 12

    def columnCount(self, parent):
        return 37

    def data(self, index, role):
        if not index.isValid():
            return None
        # vvvv this is the magic part
        elif role == Qt.BackgroundRole:
            if (index.column() % 7) - 6 == 0:           # Weekend colour
                return QBrush(QColor(100, 250, 213))    #
            elif (index.column() % 7) - 5 == 0:         #
                return QBrush(QColor(100, 250, 213))    #

            #elif index.column() == 0 and index.row() == 0:
            #    return QBrush(Qt.green)

            else:
                return QBrush(QColor(188, 250, 213)) #weekdays colour
        # ^^^^ this is the magic part
        elif role != Qt.DisplayRole:
            return None
        return QVariant(self.data_in[index.row()][index.column()])


    def flags(self, index):
        return (Qt.ItemIsEditable | Qt.ItemIsEnabled |
         Qt.NoItemFlags) | Qt.ItemIsSelectable 

    def item_data(self):
        return self.itemData()



class HorizHeader(QHeaderView):
    def __init__(self, parent, text):
        super(HorizHeader, self).__init__(Qt.Horizontal, parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.ctxMenu)
        self.hello = QAction("Hello", self)
        self.hello.triggered.connect(self.printHello)
        self.currentSection = None
        self.text = text

    def paintSection(self,painter, rect, logicalIndex):    
 
        gradient = QLinearGradient (QPointF(rect.topLeft()),QPointF(rect.topRight()))
        pen =  QPen (Qt.white)
        painter.setPen(pen)
        index = logicalIndex
        painter.drawText(QRectF(rect), self.text[index])     

    def printHello(self):
        data = self.model().headerData(self.currentSection, Qt.Horizontal)
        print data.toString()

    def ctxMenu(self, point):
        menu = QMenu(self)
        self.currentSection = self.logicalIndexAt(point)
        menu.addAction(self.hello)
        menu.exec_(self.mapToGlobal(point))


class VertHeader(QHeaderView):
    def __init__(self, parent, text):
        super(VertHeader, self).__init__(Qt.Vertical, parent)
        self.currentSection = None
        self.text = text

    def paintSection(self,painter, rect, logicalIndex):     
        gradient = QLinearGradient (QPointF(rect.topLeft()),QPointF(rect.topRight()))
        pen =  QPen (Qt.white)         
        painter.setPen(pen)
        index = logicalIndex
        painter.drawText(QRectF(rect), self.text[index])

