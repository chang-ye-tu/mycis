# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cytu/usr/src/py/mycis/designer/dlg_self.ui'
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

class Ui_dlg_self(object):
    def setupUi(self, dlg_self):
        dlg_self.setObjectName(_fromUtf8("dlg_self"))
        dlg_self.resize(450, 184)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        dlg_self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/syringe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlg_self.setWindowIcon(icon)
        dlg_self.setStyleSheet(_fromUtf8("font: 75 12pt \"Microsoft JhengHei\";"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(dlg_self)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout1 = QtGui.QHBoxLayout()
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.lbl1 = QtGui.QLabel(dlg_self)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl1.setFont(font)
        self.lbl1.setObjectName(_fromUtf8("lbl1"))
        self.horizontalLayout1.addWidget(self.lbl1)
        self.led_name = QtGui.QLineEdit(dlg_self)
        self.led_name.setText(_fromUtf8(""))
        self.led_name.setEchoMode(QtGui.QLineEdit.Normal)
        self.led_name.setObjectName(_fromUtf8("led_name"))
        self.horizontalLayout1.addWidget(self.led_name)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.horizontalLayout2 = QtGui.QHBoxLayout()
        self.horizontalLayout2.setObjectName(_fromUtf8("horizontalLayout2"))
        self.lbl2 = QtGui.QLabel(dlg_self)
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
        self.dsp_price = QtGui.QDoubleSpinBox(dlg_self)
        self.dsp_price.setObjectName(_fromUtf8("dsp_price"))
        self.horizontalLayout2.addWidget(self.dsp_price)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self.lbl3 = QtGui.QLabel(dlg_self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl3.sizePolicy().hasHeightForWidth())
        self.lbl3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl3.setFont(font)
        self.lbl3.setObjectName(_fromUtf8("lbl3"))
        self.horizontalLayout3.addWidget(self.lbl3)
        self.ded_effect = QtGui.QDateEdit(dlg_self)
        self.ded_effect.setObjectName(_fromUtf8("ded_effect"))
        self.horizontalLayout3.addWidget(self.ded_effect)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.bnb = QtGui.QDialogButtonBox(dlg_self)
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
        self.verticalLayout_2.addWidget(self.bnb)
        self.lbl1.setBuddy(self.led_name)
        self.lbl3.setBuddy(self.ded_effect)

        self.retranslateUi(dlg_self)
        QtCore.QObject.connect(self.bnb, QtCore.SIGNAL(_fromUtf8("accepted()")), dlg_self.accept)
        QtCore.QObject.connect(self.bnb, QtCore.SIGNAL(_fromUtf8("rejected()")), dlg_self.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_self)
        dlg_self.setTabOrder(self.led_name, self.ded_effect)
        dlg_self.setTabOrder(self.ded_effect, self.bnb)

    def retranslateUi(self, dlg_self):
        dlg_self.setWindowTitle(_translate("dlg_self", "自訂項目輸入", None))
        self.lbl1.setText(_translate("dlg_self", "名稱", None))
        self.lbl2.setText(_translate("dlg_self", "價格", None))
        self.lbl3.setText(_translate("dlg_self", "日期", None))

import mycis_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg_self = QtGui.QDialog()
    ui = Ui_dlg_self()
    ui.setupUi(dlg_self)
    dlg_self.show()
    sys.exit(app.exec_())

