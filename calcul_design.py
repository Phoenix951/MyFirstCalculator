# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcul_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(543, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultLine = QtWidgets.QLineEdit(self.centralwidget)
        self.resultLine.setGeometry(QtCore.QRect(20, 20, 501, 31))
        self.resultLine.setObjectName("resultLine")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget)
        self.plusButton.setGeometry(QtCore.QRect(410, 60, 111, 41))
        self.plusButton.setObjectName("plusButton")
        self.oneBut = QtWidgets.QPushButton(self.centralwidget)
        self.oneBut.setGeometry(QtCore.QRect(20, 120, 111, 41))
        self.oneBut.setObjectName("oneBut")
        self.twoBut = QtWidgets.QPushButton(self.centralwidget)
        self.twoBut.setGeometry(QtCore.QRect(150, 120, 111, 41))
        self.twoBut.setObjectName("twoBut")
        self.threeBut = QtWidgets.QPushButton(self.centralwidget)
        self.threeBut.setGeometry(QtCore.QRect(280, 120, 111, 41))
        self.threeBut.setObjectName("threeBut")
        self.clearAll = QtWidgets.QPushButton(self.centralwidget)
        self.clearAll.setGeometry(QtCore.QRect(20, 60, 181, 41))
        self.clearAll.setObjectName("clearAll")
        self.deleteItem = QtWidgets.QPushButton(self.centralwidget)
        self.deleteItem.setGeometry(QtCore.QRect(220, 60, 171, 41))
        self.deleteItem.setObjectName("deleteItem")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(410, 300, 111, 41))
        self.equalButton.setObjectName("equalButton")
        self.fourBut = QtWidgets.QPushButton(self.centralwidget)
        self.fourBut.setGeometry(QtCore.QRect(20, 180, 111, 41))
        self.fourBut.setObjectName("fourBut")
        self.fiveBut = QtWidgets.QPushButton(self.centralwidget)
        self.fiveBut.setGeometry(QtCore.QRect(150, 180, 111, 41))
        self.fiveBut.setObjectName("fiveBut")
        self.sixBut = QtWidgets.QPushButton(self.centralwidget)
        self.sixBut.setGeometry(QtCore.QRect(280, 180, 111, 41))
        self.sixBut.setObjectName("sixBut")
        self.sevenBut = QtWidgets.QPushButton(self.centralwidget)
        self.sevenBut.setGeometry(QtCore.QRect(20, 240, 111, 41))
        self.sevenBut.setObjectName("sevenBut")
        self.eightBut = QtWidgets.QPushButton(self.centralwidget)
        self.eightBut.setGeometry(QtCore.QRect(150, 240, 111, 41))
        self.eightBut.setObjectName("eightBut")
        self.nineBut = QtWidgets.QPushButton(self.centralwidget)
        self.nineBut.setGeometry(QtCore.QRect(280, 240, 111, 41))
        self.nineBut.setObjectName("nineBut")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(410, 120, 111, 41))
        self.minusButton.setObjectName("minusButton")
        self.multButton = QtWidgets.QPushButton(self.centralwidget)
        self.multButton.setGeometry(QtCore.QRect(410, 180, 111, 41))
        self.multButton.setObjectName("multButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(410, 240, 111, 41))
        self.divideButton.setObjectName("divideButton")
        self.zeroBut = QtWidgets.QPushButton(self.centralwidget)
        self.zeroBut.setGeometry(QtCore.QRect(150, 300, 111, 41))
        self.zeroBut.setObjectName("zeroBut")
        self.degreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.degreeButton.setGeometry(QtCore.QRect(280, 360, 111, 41))
        self.degreeButton.setObjectName("degreeButton")
        self.radicalButton = QtWidgets.QPushButton(self.centralwidget)
        self.radicalButton.setGeometry(QtCore.QRect(20, 360, 111, 41))
        self.radicalButton.setObjectName("radicalButton")
        self.exponButton = QtWidgets.QPushButton(self.centralwidget)
        self.exponButton.setGeometry(QtCore.QRect(150, 410, 111, 41))
        self.exponButton.setObjectName("exponButton")
        self.degreeToYButton = QtWidgets.QPushButton(self.centralwidget)
        self.degreeToYButton.setGeometry(QtCore.QRect(410, 360, 111, 41))
        self.degreeToYButton.setObjectName("degreeToYButton")
        self.numPIButton = QtWidgets.QPushButton(self.centralwidget)
        self.numPIButton.setGeometry(QtCore.QRect(20, 410, 111, 41))
        self.numPIButton.setObjectName("numPIButton")
        self.sinButton = QtWidgets.QPushButton(self.centralwidget)
        self.sinButton.setGeometry(QtCore.QRect(410, 410, 111, 41))
        self.sinButton.setObjectName("sinButton")
        self.reverseButton = QtWidgets.QPushButton(self.centralwidget)
        self.reverseButton.setGeometry(QtCore.QRect(280, 410, 111, 41))
        self.reverseButton.setObjectName("reverseButton")
        self.thirdRadicalButton = QtWidgets.QPushButton(self.centralwidget)
        self.thirdRadicalButton.setGeometry(QtCore.QRect(150, 360, 111, 41))
        self.thirdRadicalButton.setObjectName("thirdRadicalButton")
        self.intInFloat = QtWidgets.QPushButton(self.centralwidget)
        self.intInFloat.setGeometry(QtCore.QRect(280, 300, 111, 41))
        self.intInFloat.setObjectName("intInFloat")
        self.procentButton = QtWidgets.QPushButton(self.centralwidget)
        self.procentButton.setGeometry(QtCore.QRect(20, 300, 111, 41))
        self.procentButton.setObjectName("procentButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.oneBut.setText(_translate("MainWindow", "1"))
        self.twoBut.setText(_translate("MainWindow", "2"))
        self.threeBut.setText(_translate("MainWindow", "3"))
        self.clearAll.setText(_translate("MainWindow", "CE"))
        self.deleteItem.setText(_translate("MainWindow", "C"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.fourBut.setText(_translate("MainWindow", "4"))
        self.fiveBut.setText(_translate("MainWindow", "5"))
        self.sixBut.setText(_translate("MainWindow", "6"))
        self.sevenBut.setText(_translate("MainWindow", "7"))
        self.eightBut.setText(_translate("MainWindow", "8"))
        self.nineBut.setText(_translate("MainWindow", "9"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.multButton.setText(_translate("MainWindow", "*"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.zeroBut.setText(_translate("MainWindow", "0"))
        self.degreeButton.setText(_translate("MainWindow", "x^2"))
        self.radicalButton.setText(_translate("MainWindow", "sqrt(x)"))
        self.exponButton.setText(_translate("MainWindow", "exp"))
        self.degreeToYButton.setText(_translate("MainWindow", "x^y"))
        self.numPIButton.setText(_translate("MainWindow", "pi"))
        self.sinButton.setText(_translate("MainWindow", "sin(x)"))
        self.reverseButton.setText(_translate("MainWindow", "1/x"))
        self.thirdRadicalButton.setText(_translate("MainWindow", "3sqrt(x)"))
        self.intInFloat.setText(_translate("MainWindow", "."))
        self.procentButton.setText(_translate("MainWindow", "%"))

