# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cytu/usr/src/py/mycis/designer/wdg_self.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_wdg_self(object):
    def setupUi(self, wdg_self):
        wdg_self.setObjectName(_fromUtf8("wdg_self"))
        wdg_self.resize(1364, 688)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        wdg_self.setFont(font)
        wdg_self.setWindowTitle(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(wdg_self)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spl = QtGui.QSplitter(wdg_self)
        self.spl.setOrientation(QtCore.Qt.Horizontal)
        self.spl.setObjectName(_fromUtf8("spl"))
        self.tbv = QtGui.QTableView(self.spl)
        self.tbv.setObjectName(_fromUtf8("tbv"))
        self.widget = QtGui.QWidget(self.spl)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.vbl = QtGui.QVBoxLayout(self.widget)
        self.vbl.setObjectName(_fromUtf8("vbl"))
        self.led_locate = QtGui.QLineEdit(self.widget)
        self.led_locate.setObjectName(_fromUtf8("led_locate"))
        self.vbl.addWidget(self.led_locate)
        self.tbv_price = QtGui.QTableView(self.widget)
        self.tbv_price.setObjectName(_fromUtf8("tbv_price"))
        self.vbl.addWidget(self.tbv_price)
        self.horizontalLayout.addWidget(self.spl)

        self.retranslateUi(wdg_self)
        QtCore.QMetaObject.connectSlotsByName(wdg_self)

    def retranslateUi(self, wdg_self):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    wdg_self = QtGui.QWidget()
    ui = Ui_wdg_self()
    ui.setupUi(wdg_self)
    wdg_self.show()
    sys.exit(app.exec_())

