# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lingmo/project/nx_pkg/LingmoOS/shell/frameworks/bluedevil/src/wizard/pages/connect.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Connect(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Connect)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connecting = QtWidgets.QLabel(Connect)
        self.connecting.setObjectName("connecting")
        self.verticalLayout.addWidget(self.connecting)
        self.progressBar = QtWidgets.QProgressBar(Connect)
        self.progressBar.setMaximum(0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        pass
