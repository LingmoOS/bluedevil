# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lingmo/project/nx_pkg/LingmoOS/shell/frameworks/bluedevil/src/wizard/pages/fail.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fail(object):
    def setupUi(self, Fail):
        Fail.setObjectName("Fail")
        Fail.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Fail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.failIcon = QtWidgets.QLabel(Fail)
        self.failIcon.setMaximumSize(QtCore.QSize(48, 48))
        self.failIcon.setObjectName("failIcon")
        self.horizontalLayout.addWidget(self.failIcon)
        self.failLbl = QtWidgets.QLabel(Fail)
        self.failLbl.setText("")
        self.failLbl.setTextFormat(QtCore.Qt.PlainText)
        self.failLbl.setObjectName("failLbl")
        self.horizontalLayout.addWidget(self.failLbl)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Fail)
        QtCore.QMetaObject.connectSlotsByName(Fail)

    def retranslateUi(self, Fail):
        pass
