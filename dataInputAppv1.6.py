# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SHoose\Desktop\Coding\Python Projects\app\dataInputApp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox
import os
import csv
from datetime import datetime

class Error(Exception):
    pass

class ModelError(Error):
    pass

class SNError(Error):
    pass

class WoError(Error):
    pass

class Ui_MainWindow(object):
    global version
    version = "1.6"
    global mode
    mode = "day"
    def setupUi(self, MainWindow):
        global modelsGathered
        global woInput
        woInput = True
        modelsGathered = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 675)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(169, 166, 166);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Date
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox.setGeometry(QtCore.QRect(20, 10, 191, 80))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalGroupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.dateEdit = QtWidgets.QDateEdit(self.horizontalGroupBox)
        self.dateEdit.setStyleSheet("color: rgb(50, 50, 50); background-color: #b8cfcf;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.horizontalLayout.addWidget(self.dateEdit, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 575, 141, 60))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        dropShadow = QtWidgets.QGraphicsDropShadowEffect()
        dropShadow.setColor(QColor(112, 112, 112))
        dropShadow.setOffset(4)
        dropShadow.setBlurRadius(5)

        #Save button
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{color: #e2e2e2; background-color: #009500; border-radius: 5px;}" ":pressed {color: black; background-color: #43aa8b;}")
        self.pushButton.setGraphicsEffect(dropShadow)
        self.pushButton.setObjectName("pushButton")

        dropShadow = QtWidgets.QGraphicsDropShadowEffect()
        dropShadow.setColor(QColor(112, 112, 112))
        dropShadow.setOffset(4)
        dropShadow.setBlurRadius(5)

        #Clear button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 575, 141, 60))
        self.pushButton_2.setStyleSheet("QPushButton{background-color: #e2e2e2; border-radius: 5px;}" ":pressed{background-color: #313638; color: #e2e2e2}")
        self.pushButton_2.setGraphicsEffect(dropShadow)
        self.pushButton_2.setObjectName("pushButton_2")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(75, 100, 742, 445))
        self.tableWidget.setMaximumSize(QtCore.QSize(781, 16777215))
        self.tableWidget.setStyleSheet("background-color: rgb(37, 68, 65); alternate-background-color: rgb(136, 153, 151); color: #e2e2e2;")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)

        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setStyleSheet("color: rgb(75,75,75);")
        self.tableWidget.verticalHeader().setStyleSheet("color: rgb(75,75,75);")

        #Add P/F buttons to each appropriate cell
        for i in range(self.tableWidget.rowCount()):
            for j in range(3,7):
                self.QGroupBox = QtWidgets.QGroupBox(self.tableWidget)
                Pbutton = QtWidgets.QCheckBox("P", self.QGroupBox)
                Fbutton = QtWidgets.QCheckBox("F", self.QGroupBox)

                if i%2 == 0:
                    self.QGroupBox.setStyleSheet("background-color: rgb(37, 68, 65);")
                else:
                    self.QGroupBox.setStyleSheet("background-color: rgb(136, 153, 151); border: none;")

                self.bg = QtWidgets.QButtonGroup(self.QGroupBox)
                self.bg.addButton(Pbutton)
                self.bg.addButton(Fbutton)
                self.bg.setExclusive(True)

                self.horizontalLayout = QtWidgets.QHBoxLayout(self.QGroupBox)
                self.horizontalLayout.addWidget(Pbutton)
                self.horizontalLayout.addWidget(Fbutton)
                self.QGroupBox.setLayout(self.horizontalLayout)
                self.tableWidget.setCellWidget(i,j,self.QGroupBox)
                Pbutton.clicked.connect(self.onButtonClicked)
                Fbutton.clicked.connect(self.onButtonClicked)

            self.tableWidget.resizeRowToContents(i)

        self.btnLastChecked = None

        dropShadow = QtWidgets.QGraphicsDropShadowEffect()
        dropShadow.setColor(QColor(112, 112, 112))
        dropShadow.setOffset(4)
        dropShadow.setBlurRadius(5)

        #Model name import button
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 575, 141, 60))
        self.pushButton_3.setStyleSheet("QPushButton{background-color: #6E7E85; color: #e2e2e2; border-radius: 5px;}" ":pressed{background-color: #eb9486}")
        self.pushButton_3.setGraphicsEffect(dropShadow)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800,20,100,20))
        self.pushButton_4.setStyleSheet("QPushButton{background-color: #1F2041; color: #E2E2E2;}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 290, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        #App title
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: RGBA(255,255,255,0); color: #e2e2e2;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760,0,140,20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(25)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255,255,255,0); color: rgb(120,120,120);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.importModels)
        self.pushButton_4.clicked.connect(self.changeMode)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeMode(self):
        global mode
        rows = self.tableWidget.rowCount()
        button = MainWindow.sender()

        if mode == "day":
            button.setStyleSheet("QPushButton{background-color: #FFC857; color: #1F2041;}")
            button.setText("Day Mode")

            MainWindow.setStyleSheet("background-color: #1F2041")

            self.tableWidget.setStyleSheet("background-color: #4DA1A9; alternate-background-color: #19647E; color: #e2e2e2;")

            self.dateEdit.setStyleSheet("color: #e2e2e2; background-color: #4DA1A9;")

            dropShadow = QtWidgets.QGraphicsDropShadowEffect()
            dropShadow.setColor(QColor(55, 55, 55))
            dropShadow.setOffset(4)
            dropShadow.setBlurRadius(5)

            self.pushButton.setStyleSheet("QPushButton{color: #e2e2e2; background-color: #19647E; border-radius: 5px;}" ":pressed {color: black; background-color: #81769C;}")
            self.pushButton.setGraphicsEffect(dropShadow)

            dropShadow = QtWidgets.QGraphicsDropShadowEffect()
            dropShadow.setColor(QColor(55, 55, 55))
            dropShadow.setOffset(4)
            dropShadow.setBlurRadius(5)

            self.pushButton_3.setStyleSheet("QPushButton{background-color: #FFC857; color: #1E1E24; border-radius: 5px;}" ":pressed{background-color: #4B3F72;}")
            self.pushButton_3.setGraphicsEffect(dropShadow)

            dropShadow = QtWidgets.QGraphicsDropShadowEffect()
            dropShadow.setColor(QColor(55, 55, 55))
            dropShadow.setOffset(4)
            dropShadow.setBlurRadius(5)

            self.pushButton_2.setGraphicsEffect(dropShadow)

            self.label.setStyleSheet("color:#E2E2E2")

            groupBox = self.tableWidget.findChildren(QtWidgets.QGroupBox)
            for row in range(rows):
                #Ensures groupboxes are correctly colored
                i=0
                while i < len(groupBox):
                    if i < (row*4): #If before the row to be deleted
                        for box in groupBox[i:i+4]:
                            # box.setStyleSheet("")
                            box.setStyleSheet("background-color: #4DA1A9;")
                        i += 4
                        for box in groupBox[i:i+4]:
                            # box.setStyleSheet("")
                            box.setStyleSheet("background-color: #19647E; border: none;")
                        if i < (len(groupBox) - 4):
                            i+=4
                    else: #Deleted row and after
                        for box in groupBox[i:i+4]:
                            # box.setStyleSheet("")
                            box.setStyleSheet("background-color: #19647E; border: none;")
                        i += 4
                        for box in groupBox[i:i+4]:
                            # box.setStyleSheet("")
                            box.setStyleSheet("background-color: #4DA1A9;")
                        if i < (len(groupBox) - 4):
                            i+=4
            mode = "night"

        else:
            button.setStyleSheet("QPushButton{background-color: #1F2041; color: #E2E2E2;}")
            button.setText("Night Mode")
            MainWindow.setStyleSheet("background-color:rgb(169, 166, 166);")
            self.tableWidget.setStyleSheet("background-color: rgb(37, 68, 65); alternate-background-color: rgb(136, 153, 151); color: #e2e2e2;")
            self.dateEdit.setStyleSheet("color: rgb(50, 50, 50); background-color: #b8cfcf;")

            dropShadow = QtWidgets.QGraphicsDropShadowEffect()
            dropShadow.setColor(QColor(112, 112, 112))
            dropShadow.setOffset(4)
            dropShadow.setBlurRadius(5)

            self.pushButton.setStyleSheet("QPushButton{color: #e2e2e2; background-color: #009500; border-radius: 5px;}" ":pressed {color: black; background-color: #43aa8b;}")
            self.pushButton.setGraphicsEffect(dropShadow)

            dropShadow = QtWidgets.QGraphicsDropShadowEffect()
            dropShadow.setColor(QColor(112, 112, 112))
            dropShadow.setOffset(4)
            dropShadow.setBlurRadius(5)

            self.pushButton_3.setStyleSheet("QPushButton{background-color: #6E7E85; color: #e2e2e2; border-radius: 5px;}" ":pressed{background-color: #eb9486}")
            self.pushButton_3.setGraphicsEffect(dropShadow)

            dropShadow = QtWidgets.QGraphicsDropShadowEffect()
            dropShadow.setColor(QColor(112, 112, 112))
            dropShadow.setOffset(4)
            dropShadow.setBlurRadius(5)

            self.pushButton_2.setGraphicsEffect(dropShadow)

            self.label.setStyleSheet("")

            groupBox = self.tableWidget.findChildren(QtWidgets.QGroupBox)
            for row in range(rows):
                #Ensures groupboxes are correctly colored
                i=0
                while i < len(groupBox):
                    if i < (row*4): #If before the row to be deleted
                        for box in groupBox[i:i+4]:
                            box.setStyleSheet("background-color: rgb(37, 68, 65);")
                        i += 4
                        for box in groupBox[i:i+4]:
                            box.setStyleSheet("background-color: rgb(136, 153, 151); border: none;")
                        if i < (len(groupBox) - 4):
                            i+=4
                    else: #Deleted row and after
                        for box in groupBox[i:i+4]:
                            box.setStyleSheet("background-color: rgb(136, 153, 151); border: none;")
                        i += 4
                        for box in groupBox[i:i+4]:
                            box.setStyleSheet("background-color: rgb(37, 68, 65);")
                        if i < (len(groupBox) - 4):
                            i+=4
            mode = "day"
        return

    def onButtonClicked(self): #Checks or unchecks box while maintaining exclusivity
        if not self.btnLastChecked: #If no last button checked
            self.btnLastChecked = MainWindow.sender() #checked box is last box checked
        else:
            if self.btnLastChecked == MainWindow.sender():
                child = MainWindow.sender().parent().findChild(QtWidgets.QButtonGroup) #Get button group parent of checkboxe
                child.setExclusive(False)
                MainWindow.sender().setChecked(False)
                child.setExclusive(True)
                self.btnLastChecked = None
            else:
                self.btnLastChecked = MainWindow.sender()

    def retranslateUi(self, MainWindow):
        global version
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laser Status Updater v" + version))
        MainWindow.setWindowIcon(QtGui.QIcon("*REMOVED*"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.dateEdit.setProperty("setDateTime", _translate("MainWindow", "QtCore.QDateTime.currentDateTime()"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S/N"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Model"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Work Order"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Chamber"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Vibration"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Long Term"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Final Test Report"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("MainWindow", "Gather Model Names"))
        self.label_2.setText(_translate("MainWindow", "Laser Status Updater"))
        self.label_3.setText(_translate("MainWindow", "Shawn Hoose - Sept 2019"))
        self.pushButton_4.setText(_translate("MainWindow", "Night Mode"))

    def gatherData(self):
        rows = self.tableWidget.rowCount()
        blankModel = False
        if modelsGathered == False:
            for z in range(rows):
                model = self.tableWidget.item(z,1)
                if model:
                    model = model.text()
                    if model.isspace() or not model:
                        blankModel = True

            if blankModel == True:
                display = QMessageBox(QMessageBox.Critical,"Models not gathered!","System models were not gathered.\nPress 'Gather Model Names' button.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                raise ModelError
                return

        data = {}
        checkboxes = self.tableWidget.findChildren(QtWidgets.QCheckBox) #All checkboxes in the table

        for y in range(rows):
            SN = self.tableWidget.item(y,0) #If something in the first column
            if SN:
                if SN.text().isspace() or not SN.text(): #If the text is all white space or is blank
                    display = QMessageBox(QMessageBox.Warning,"No Serial Number!","There is no serial number at row " + str(y+1) + "! Please enter the serial number and try again.")
                    display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                    display.exec()
                    raise SNError
                    return

                try:
                    wo = self.woCheck(y)
                except WoError:
                    display = QMessageBox(QMessageBox.Critical,"Work Order not input correctly!","The Work Order for " + SN.text() +" has not been input correctly. Please input the Work Order and try again.")
                    display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                    display.exec()
                    raise WoError
                    return

                try:
                    model = self.tableWidget.item(y,1).text() #Gather model name
                except AttributeError as e:
                    display = QMessageBox(QMessageBox.Warning,"No Model!","There is no model for " + str(SN.text()) + "! Please press the 'Gather Model Names' button.")
                    display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                    display.exec()
                    raise ModelError
                    return

                separatedCheckBoxes = []
                rowCheckBoxes = checkboxes[8*y:8*y + 8]

                for i in range(0,len(rowCheckBoxes),2): #separates checkboxes per test
                    separatedCheckBoxes.append(rowCheckBoxes[i:i+2])

                #Default values
                *REMOVED*
                *REMOVED*
                *REMOVED*
                *REMOVED*

                SN = SN.text()
                try:
                    model = self.tableWidget.item(row,1).text()
                except:
                    pass

                boxcount = 1 #Which set of checkboxes we're looking at
                for checkbox in separatedCheckBoxes:
                    for i in range(len(checkbox)): #Logic to determine which tests failed and passed; 1 is pass, 0 is fail.
                        if boxcount == 1:
                            if i == 0 and checkbox[i].isChecked() is True:
                                *REMOVED* = 1
                            if i == 1 and checkbox[i].isChecked() is True:
                                *REMOVED* = 0

                        if boxcount == 2:
                            if i == 0 and checkbox[i].isChecked() is True:
                                *REMOVED* = 1
                            if i == 1 and checkbox[i].isChecked() is True:
                                *REMOVED* = 0

                        if boxcount == 3:
                            if i == 0 and checkbox[i].isChecked() is True:
                                *REMOVED* = 1
                            if i == 1 and checkbox[i].isChecked() is True:
                                *REMOVED* = 0

                        if boxcount == 4:
                            if i == 0 and checkbox[i].isChecked() is True:
                                *REMOVED* = 1
                            if i == 1 and checkbox[i].isChecked() is True:
                                *REMOVED* = 0

                    boxcount += 1

                data[SN] = *REMOVED*

        return data

    def save(self):
        savePath = "*REMOVED*"

        fileList = [f for f in os.listdir(savePath) if os.path.isfile(os.path.join(savePath, f))]

        data = None
        try: #Try and gather data
            data = self.gatherData()
        except ModelError as e:
            return
        except SNError as e:
            return
        except WoError as e:
            return

        if len(data) == 0:
            display = QMessageBox(QMessageBox.Critical,"No Serial Numbers","No Serial Numbers were input. Please fix and try again.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            return

        dateSave = self.dateEdit.date().toString("MM-dd-yy") #Date for filename
        date = self.dateEdit.date().toString("MM/dd/yyyy") #Date for CSV

        fileName = str(dateSave) + ".csv"
        filePath = os.path.join(savePath, fileName)

        try:
            if fileName in fileList: #If file exists, append
                oldData = [] #Data already existing in file
                found = {}

                for x in data:
                    found[x] = False

                with open(filePath) as readFile: #Get old data from CSV to compare against
                    reader = csv.reader(readFile)
                    for row in reader:
                        oldData.append(row) #add it to new list

                for x in data: #parse through new list, find the SN, change values to new values if the old value was blank.
                    dataSplit = data[x].split(",") #New data that has just been input
                    for laser in oldData:
                        if laser[0] == x:
                            found[x] = True
                            for y in range(1,6):
                                if dataSplit[y] and laser[y] == '':
                                    laser[y] = dataSplit[y]

                    if not found[x]:
                        dataSplit = data[x].split(",")
                        testData = ','.join(dataSplit[1:])
                        output = str(x)  + "," + str(testData) + "," + str(dataSplit[0]) + "," + str(date)
                        output = output.split(",")
                        oldData.append(output)

                os.remove(filePath)
                with open(filePath,'w', newline='') as file:
                    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                    for x in oldData:
                        testData = ','.join(x[1:])
                        output = str(x[0])  + "," + str(testData)
                        output = output.split(",")
                        wr.writerow(output)

                    display = QMessageBox(QMessageBox.NoIcon,"File Ammended","Data ammended to " + str(fileName) + "!")
                    display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                    display.exec()

            else: #Else, create new file
                with open(filePath,'w', newline='') as file:
                    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                    for x in data:
                        dataSplit = data[x].split(",")
                        testData = ','.join(dataSplit[1:])
                        output = str(x)  + "," + str(testData) + "," + str(dataSplit[0]) + "," + str(date)
                        output = output.split(",")
                        wr.writerow(output)

                    display = QMessageBox(QMessageBox.NoIcon,"File Saved","Data saved in " + str(fileName) + "!")
                    display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                    display.exec()

        except:
            display = QMessageBox(QMessageBox.Critical,"File Open","The file " + str(fileName) + " is currently open. Please close it and try again.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            return

    def clear(self):
        global mode
        self.setupUi(MainWindow) #Resets UI
        if mode == "night":
            mode = "day"
            self.changeMode()
            self.pushButton_4.setStyleSheet("QPushButton{background-color: #FFC857; color: #1F2041;}")

        display = QMessageBox(QMessageBox.NoIcon,"Table Cleared","The table has been cleared of all data!")
        display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
        display.exec()

    def woCheck(self, row):
        global woInput
        try:
            wo = self.tableWidget.item(row,2).text() #Gather work order
            if wo.isspace() or wo:
                if not (5 < len(wo) < 8):
                    woInput = False
                else:
                    woInput = True

                if woInput == False:
                    raise WoError
                    return
        except AttributeError as e:
            wo = ''

        return wo

    def importModels(self):
        global modelsGathered
        global mode
        row = 0
        rows = self.tableWidget.rowCount()
        models = []
        SNList = []
        for row in range(rows):
            SN = self.tableWidget.item(row,0)
            if SN:
                if SN.text().isspace() or not SN.text():
                    row2 = len(range(rows))-1
                    self.tableWidget.removeRow(row)
                    self.tableWidget.insertRow(row2)
                    for j in range(3,7):
                        self.QGroupBox = QtWidgets.QGroupBox(self.tableWidget)

                        Pbutton = QtWidgets.QCheckBox("P", self.QGroupBox)
                        Fbutton = QtWidgets.QCheckBox("F", self.QGroupBox)

                        self.bg = QtWidgets.QButtonGroup(self.QGroupBox)
                        self.bg.setExclusive(True)
                        self.bg.addButton(Pbutton)
                        self.bg.addButton(Fbutton)

                        self.horizontalLayout = QtWidgets.QHBoxLayout(self.QGroupBox)
                        self.horizontalLayout.addWidget(Pbutton)
                        self.horizontalLayout.addWidget(Fbutton)

                        Pbutton.clicked.connect(self.onButtonClicked)
                        Fbutton.clicked.connect(self.onButtonClicked)

                        self.QGroupBox.setLayout(self.horizontalLayout)
                        self.tableWidget.setCellWidget(row2,j,self.QGroupBox)
                        self.QGroupBox.setStyleSheet("background-color: rgb(136, 153, 151); border: none;")

                    self.tableWidget.resizeRowToContents(row2)

                    #Ensures groupboxes are correctly colored
                    groupBox = self.tableWidget.findChildren(QtWidgets.QGroupBox) #all groupboxes
                    if mode == "day":
                        primCol = "background-color: rgb(37, 68, 65);"
                        secCol = "background-color: rgb(136, 153, 151); border: none;"

                    else:
                        primCol = "background-color: #4DA1A9"
                        secCol = "background-color:#19647E; border: none;"

                    i=0
                    while i < len(groupBox):
                        if i < (row*4): #If before the row to be deleted
                            for box in groupBox[i:i+4]:
                                box.setStyleSheet(primCol)
                            i += 4
                            for box in groupBox[i:i+4]:
                                box.setStyleSheet(secCol)
                            if i < (len(groupBox) - 4):
                                i+=4
                        else: #Deleted row and after
                            for box in groupBox[i:i+4]:
                                box.setStyleSheet(secCol)
                            i += 4
                            for box in groupBox[i:i+4]:
                                box.setStyleSheet(primCol)
                            if i < (len(groupBox) - 4):
                                i+=4

                    display = QMessageBox(QMessageBox.Critical,"Blank Serial Number","A blank serial number was detected and removed from row " + str(row+1) + ".\nPlease try again.")
                    display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                    display.exec()
                    return
                else:
                    SNList.append(SN.text())

        try:
            Ui_MainWindow.SNCheck(SNList)
        except:
            return

        for row in range(rows):
            SN = self.tableWidget.item(row,0)
            if SN:
                SN = SN.text()
                try:
                    currentModel = self.tableWidget.item(row,1).text()
                    if len(currentModel) < 2:
                        splitSN = SN.split("-")
                        try:
                            folderPath = Ui_MainWindow.FindLaserDataFolder(splitSN[0],SN)
                            serialized = folderPath.split("\\")[-1]
                            splitSerial = serialized.split(" ")

                            try:
                                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(splitSerial[1])))
                            except IndexError as e:
                                display = QMessageBox(QMessageBox.Critical,"Improperly Named Folder","The folder for S/N " + SN + " is not formatted correctly.\nPlease correct the folder name and try again, or manually input the model name.")
                                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                                display.exec()
                                return

                        except:
                            display = QMessageBox(QMessageBox.Critical,"No Model Found","No folder found for S/N " + SN + ".\nPlease input this model manually and try again.")
                            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                            display.exec()
                            return

                except:
                    splitSN = SN.split("-")
                    try:
                        folderPath = Ui_MainWindow.FindLaserDataFolder(splitSN[0],SN)
                        serialized = folderPath.split("\\")[-1]
                        splitSerial = serialized.split(" ")

                        try:
                            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(splitSerial[1])))
                        except IndexError as e:
                            display = QMessageBox(QMessageBox.Critical,"Improperly Named Folder","The folder for S/N " + SN + " is not formatted correctly.\nPlease correct the folder name and try again, or manually input the model name.")
                            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                            display.exec()
                            return
                    except:
                        display = QMessageBox(QMessageBox.Critical,"No Model Found","No folder found for S/N " + SN + ".\nPlease create a folder or manually input the model and try again.")
                        display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                        display.exec()
                        return

        modelsGathered = True
        display = QMessageBox(QMessageBox.Warning,"Models Imported","Model Names Imported! Please double check and ensure they are correct. If they are not, correct them.")
        display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
        display.exec()
        return

    def SNCheck(SNList):
        dt = datetime.now().date()
        todayDate = '{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year % 100)

        if len(SNList) == 0:
            display = QMessageBox(QMessageBox.Critical,"No Serial Numbers","No Serial Numbers were input. Please fix and try again.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            raise Error
            return

        for x in SNList:
            xSplit = x.split("-")

            try:
                intCheck1 = type(int(xSplit[0]))
                intCheck2 = type(int(xSplit[1]))
            except:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is not formatted correctly. Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                raise Error
                return

            if len(x) is not 6:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is not formatted correctly (incorrect length). Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                raise Error
                return

            if x[2] is not "-":
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is not formatted correctly. Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                raise Error
                return

            if int(xSplit[0]) - int(todayDate[-2:]) > 1:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is out of the acceptable range. Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                raise Error
                return

            if len(xSplit[0])>2 or len(xSplit[1])>3:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is not formatted correctly. Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                raise Error
                return

            if SNList.count(x) > 1:
                display = QMessageBox(QMessageBox.Critical,"Duplicate Serial Number","The Serial Number " + str(x) + " occurs more than once in the list. Please clear the data and redo.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*o"))
                display.exec()
                raise Error
                return

    def FindLaserDataFolder(year, SN):
        folderDir = "\\20" + year + " Laser Data"
        parentDir = *REMOVED*

        try:
            z= os.listdir(path=parentDir)
        except:
            return

        for i in range(0,len(z)): # For Loop to check if Serial Number is in Laser Data folder of that year.
            Fname = z[i]# Full Serialized Folder Name.
            sNum = Fname[:6] # Takes just the Serial Number of full folder name.
            if sNum == SN:
                check = True
                temp = z[i]
                break # Breaks the for loop if Serial number is found.
            else:
                check = False
        if check == True:
            path2 = parentDir + "\\" + temp
        if check == False:
            return

        try:
            return path2
        except:
            return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
