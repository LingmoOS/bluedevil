# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lingmo/project/nx_pkg/LingmoOS/shell/frameworks/bluedevil/src/sendfile/discover.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Discover(object):
    def setupUi(self, Discover):
        Discover.setObjectName("Discover")
        Discover.resize(571, 525)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Discover)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.devices = QtWidgets.QListView(Discover)
        self.devices.setIconSize(QtCore.QSize(48, 48))
        self.devices.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.devices.setObjectName("devices")
        self.verticalLayout.addWidget(self.devices)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Discover)
        QtCore.QMetaObject.connectSlotsByName(Discover)

    def retranslateUi(self, Discover):
        pass