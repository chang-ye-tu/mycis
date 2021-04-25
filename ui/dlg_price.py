# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cytu/usr/src/py/mycis/designer/dlg_price.ui'
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

class Ui_dlg_price(object):
    def setupUi(self, dlg_price):
        dlg_price.setObjectName(_fromUtf8("dlg_price"))
        dlg_price.resize(450, 139)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        dlg_price.setFont(font)
        dlg_price.setStyleSheet(_fromUtf8("font: 75 12pt \"Microsoft JhengHei\";"))
        self.verticalLayout = QtGui.QVBoxLayout(dlg_price)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout1 = QtGui.QHBoxLayout()
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.lbl1 = QtGui.QLabel(dlg_price)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl1.sizePolicy().hasHeightForWidth())
        self.lbl1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl1.setFont(font)
        self.lbl1.setObjectName(_fromUtf8("lbl1"))
        self.horizontalLayout1.addWidget(self.lbl1)
        self.dsp_price = QtGui.QDoubleSpinBox(dlg_price)
        self.dsp_price.setObjectName(_fromUtf8("dsp_price"))
        self.horizontalLayout1.addWidget(self.dsp_price)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.horizontalLayout2 = QtGui.QHBoxLayout()
        self.horizontalLayout2.setObjectName(_fromUtf8("horizontalLayout2"))
        self.lbl2 = QtGui.QLabel(dlg_price)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl2.sizePolicy().hasHeightForWidth())
        self.lbl2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl2.setFont(font)
        self.lbl2.setObjectName(_fromUtf8("lbl2"))
        self.horizontalLayout2.addWidget(self.lbl2)
        self.ded_effect = QtGui.QDateEdit(dlg_price)
        self.ded_effect.setObjectName(_fromUtf8("ded_effect"))
        self.horizontalLayout2.addWidget(self.ded_effect)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.bnb = QtGui.QDialogButtonBox(dlg_price)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.bnb.setFont(font)
        self.bnb.setStyleSheet(_fromUtf8(""))
        self.bnb.setOrientation(QtCore.Qt.Horizontal)
        self.bnb.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.bnb.setCenterButtons(False)
        self.bnb.setObjectName(_fromUtf8("bnb"))
        self.verticalLayout.addWidget(self.bnb)
        self.lbl2.setBuddy(self.ded_effect)

        self.retranslateUi(dlg_price)
        QtCore.QObject.connect(self.bnb, QtCore.SIGNAL(_fromUtf8("accepted()")), dlg_price.accept)
        QtCore.QObject.connect(self.bnb, QtCore.SIGNAL(_fromUtf8("rejected()")), dlg_price.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_price)
        dlg_price.setTabOrder(self.ded_effect, self.bnb)

    def retranslateUi(self, dlg_price):
        dlg_price.setWindowTitle(_translate("dlg_price", "價格輸入", None))
        self.lbl1.setText(_translate("dlg_price", "價格", None))
        self.lbl2.setText(_translate("dlg_price", "日期", None))

import mycis_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg_price = QtGui.QDialog()
    ui = Ui_dlg_price()
    ui.setupUi(dlg_price)
    dlg_price.show()
    sys.exit(app.exec_())

