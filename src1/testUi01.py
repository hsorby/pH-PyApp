# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUi01.ui'
#
# Created: Thu Sep 05 16:30:19 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.co2Source = QtGui.QSlider(self.centralwidget)
        self.co2Source.setGeometry(QtCore.QRect(50, 29, 20, 221))
        self.co2Source.setOrientation(QtCore.Qt.Vertical)
        self.co2Source.setTickPosition(QtGui.QSlider.TicksBelow)
        self.co2Source.setObjectName("co2Source")
        self.co2Sink = QtGui.QSlider(self.centralwidget)
        self.co2Sink.setGeometry(QtCore.QRect(130, 29, 20, 221))
        self.co2Sink.setOrientation(QtCore.Qt.Vertical)
        self.co2Sink.setTickPosition(QtGui.QSlider.TicksBelow)
        self.co2Sink.setObjectName("co2Sink")
        self.widget = MatplotlibWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(310, 30, 291, 231))
        self.widget.setObjectName("widget")
        self.protonSource = QtGui.QSlider(self.centralwidget)
        self.protonSource.setGeometry(QtCore.QRect(210, 29, 20, 221))
        self.protonSource.setOrientation(QtCore.Qt.Vertical)
        self.protonSource.setTickPosition(QtGui.QSlider.TicksBelow)
        self.protonSource.setObjectName("protonSource")
        self.co2SourceLabel = QtGui.QLabel(self.centralwidget)
        self.co2SourceLabel.setGeometry(QtCore.QRect(30, 260, 61, 20))
        self.co2SourceLabel.setObjectName("co2SourceLabel")
        self.co2SinkLabel = QtGui.QLabel(self.centralwidget)
        self.co2SinkLabel.setGeometry(QtCore.QRect(120, 260, 51, 20))
        self.co2SinkLabel.setObjectName("co2SinkLabel")
        self.protonSourceLabel = QtGui.QLabel(self.centralwidget)
        self.protonSourceLabel.setGeometry(QtCore.QRect(190, 260, 61, 20))
        self.protonSourceLabel.setObjectName("protonSourceLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Simulate", None, QtGui.QApplication.UnicodeUTF8))
        self.co2SourceLabel.setText(QtGui.QApplication.translate("MainWindow", "CO2 source", None, QtGui.QApplication.UnicodeUTF8))
        self.co2SinkLabel.setText(QtGui.QApplication.translate("MainWindow", "CO2 sink", None, QtGui.QApplication.UnicodeUTF8))
        self.protonSourceLabel.setText(QtGui.QApplication.translate("MainWindow", "H+ source", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import MatplotlibWidget
