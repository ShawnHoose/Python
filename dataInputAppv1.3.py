# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SHoose\Desktop\Coding\Python Projects\app\dataInputApp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
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

class Ui_MainWindow(object):
    global version
    version = "1.3"
    def setupUi(self, MainWindow):
        global modelsGathered
        modelsGathered = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(150, 150, 150);")

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
        self.pushButton.setGeometry(QtCore.QRect(30, 480, 141, 61))

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

        #Save button
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: #e2e2e2;"
"background-color: #008000;")
        self.pushButton.setObjectName("pushButton")

        #Clear button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 480, 141, 61))
        self.pushButton_2.setStyleSheet("background-color: #e2e2e2")
        self.pushButton_2.setObjectName("pushButton_2")


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 100, 641, 371))
        self.tableWidget.setMaximumSize(QtCore.QSize(781, 16777215))
        self.tableWidget.setStyleSheet("background-color: rgb(75, 75, 75); alternate-background-color: rgb(140, 140, 140); color: #e2e2e2;")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)

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
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)


        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setStyleSheet("color: rgb(75,75,75);")
        self.tableWidget.verticalHeader().setStyleSheet("color: rgb(75,75,75);")

        #Add P/F buttons to each appropriate cell
        for i in range(self.tableWidget.rowCount()):
            for j in range(2,6):
                self.QGroupBox = QtWidgets.QGroupBox(self.tableWidget)
                Pbutton = QtWidgets.QCheckBox("P", self.QGroupBox)
                Fbutton = QtWidgets.QCheckBox("F", self.QGroupBox)

                if i%2 == 0:
                    self.QGroupBox.setStyleSheet("background-color: rgb(75,75,75);")
                else:
                    self.QGroupBox.setStyleSheet("background-color: rgb(140,140,140); border: none;")

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

        #Model name import button
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 480, 141, 61))
        self.pushButton_3.setStyleSheet("background-color: #6E7E85; color: #e2e2e2;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 290, 50))
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
        self.label_3.setGeometry(QtCore.QRect(660,0,140,20))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        MainWindow.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon.ico"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.dateEdit.setProperty("setDateTime", _translate("MainWindow", "QtCore.QDateTime.currentDateTime()"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S/N"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Model"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Chamber"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Vibration"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Long Term"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Final Test Report"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("MainWindow", "Gather Model Names"))
        self.label_2.setText(_translate("MainWindow", "Laser Status Updater"))
        self.label_3.setText(_translate("MainWindow", "Shawn Hoose - Sept 2019"))



    def gatherData(self):
        if modelsGathered == False:
            display = QMessageBox(QMessageBox.Critical,"Models not gathered!","System models were not gathered.\nPress 'Gather Model Names' button.")
            display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
            display.exec()
            raise ModelError
            return
        else:
            rows = self.tableWidget.rowCount()
            data = {}
            checkboxes = self.tableWidget.findChildren(QtWidgets.QCheckBox) #All checkboxes in the table

            for y in range(rows):
                SN = self.tableWidget.item(y,0) #If something in the first column
                if SN:
                    if SN.text().isspace() or not SN.text(): #If the text is all white space or is blank
                        display = QMessageBox(QMessageBox.Warning,"No Serial Number!","There is no serial number at row " + str(y+1) + "! Please enter the serial number and try again.")
                        display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                        display.exec()
                        raise SNError
                        return

                    try:
                        model = self.tableWidget.item(y,1).text() #Gather model name
                    except AttributeError as e:
                        display = QMessageBox(QMessageBox.Warning,"No Model!","There is no model for " + str(SN.text()) + "! Please press the 'Gather Model Names' button.")
                        display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                        display.exec()
                        raise ModelError
                        return

            for row in range(rows):
                SN = self.tableWidget.item(row,0)
                if SN:
                    separatedCheckBoxes = []
                    rowCheckBoxes = checkboxes[8*row:8*row + 8]

                    for i in range(0,len(rowCheckBoxes),2): #separates checkboxes per test
                        separatedCheckBoxes.append(rowCheckBoxes[i:i+2])

                    #Default values
                    c = ""
                    v = ""
                    lt = ""
                    ftr = ""

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
                                    c = 1
                                if i == 1 and checkbox[i].isChecked() is True:
                                    c = 0

                            if boxcount == 2:
                                if i == 0 and checkbox[i].isChecked() is True:
                                    v = 1
                                if i == 1 and checkbox[i].isChecked() is True:
                                    v = 0

                            if boxcount == 3:
                                if i == 0 and checkbox[i].isChecked() is True:
                                    lt = 1
                                if i == 1 and checkbox[i].isChecked() is True:
                                    lt = 0

                            if boxcount == 4:
                                if i == 0 and checkbox[i].isChecked() is True:
                                    ftr = 1
                                if i == 1 and checkbox[i].isChecked() is True:
                                    ftr = 0

                        boxcount += 1

                    data[SN] = model + "," + str(c) + "," + str(v) + "," + str(lt) + "," + str(ftr)

            return data

    def save(self):
        savePath = "\\\photonix04\Interdepartmental Coordination\QC\Statistics Spreadsheet\CSV"

        fileList = [f for f in os.listdir(savePath) if os.path.isfile(os.path.join(savePath, f))]

        data = None
        try: #Try and gather data
            data = self.gatherData()
        except ModelError as e:
            return
        except SNError as e:
            return

        if len(data) == 0:
            display = QMessageBox(QMessageBox.Critical,"No Serial Numbers","No Serial Numbers were input. Please fix and try again.")
            display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
            display.exec()
            return

        dateSave = self.dateEdit.date().toString("MM-dd-yy") #Date for filename
        date = self.dateEdit.date().toString("MM/dd/yyyy") #Date for CSV

        fileName = str(dateSave) + ".csv"
        filePath = os.path.join(savePath, fileName)

        try:
            if fileName in fileList: #If file exists, append
                with open(filePath,'a', newline='') as file:
                    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                    for x in data:
                        dataSplit = data[x].split(",")
                        testData = ','.join(dataSplit[1:])
                        output = str(x)  + "," + str(testData) + "," + str(dataSplit[0]) + "," + str(date)
                        output = output.split(",")
                        wr.writerow(output)

                    display = QMessageBox(QMessageBox.NoIcon,"File Ammended","Data ammended to " + str(fileName) + "!")
                    display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon.ico"))
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
                    display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon.ico"))
                    display.exec()

        except:
            display = QMessageBox(QMessageBox.Critical,"File Open","The file " + str(fileName) + " is currently open. Please close it and try again.")
            display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
            display.exec()
            return

    def clear(self):
        self.setupUi(MainWindow) #Resets UI
        display = QMessageBox(QMessageBox.NoIcon,"Table Cleared","The table has been cleared of all data!")
        display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon.ico"))
        display.exec()

    def importModels(self):
        global modelsGathered
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
                    for j in range(2,6):
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
                        self.QGroupBox.setLayout(self.horizontalLayout)
                        self.tableWidget.setCellWidget(row2,j,self.QGroupBox)

                    self.tableWidget.resizeRowToContents(row2)
                    display = QMessageBox(QMessageBox.Critical,"Blank Serial Number","A blank serial number was detected and removed from row " + str(row+1) + ".\nPlease try again.")
                    display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
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

                            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(splitSerial[1])))
                        except:
                            display = QMessageBox(QMessageBox.Critical,"No Model Found","No folder found for S/N " + SN + ".\nPlease input this model manually and try again.")
                            display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                            display.exec()
                            return

                except:
                    splitSN = SN.split("-")
                    try:
                        folderPath = Ui_MainWindow.FindLaserDataFolder(splitSN[0],SN)
                        serialized = folderPath.split("\\")[-1]
                        splitSerial = serialized.split(" ")

                        self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(splitSerial[1])))
                    except:
                        display = QMessageBox(QMessageBox.Critical,"No Model Found","No folder found for S/N " + SN + ".\nPlease create a folder or manually input the model and try again.")
                        display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                        display.exec()
                        return

        modelsGathered = True
        display = QMessageBox(QMessageBox.Warning,"Models Imported","Model Names Imported! Please double check and ensure they are correct. If they are not, correct them.")
        display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-caution.ico"))
        display.exec()
        return

    def SNCheck(SNList):
        dt = datetime.now().date()
        todayDate = '{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year % 100)

        if len(SNList) == 0:
            display = QMessageBox(QMessageBox.Critical,"No Serial Numbers","No Serial Numbers were input. Please fix and try again.")
            display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
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
                display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                display.exec()
                raise Error
                return

            if len(x) is not 6:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is not formatted correctly (incorrect length). Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                display.exec()
                raise Error
                return

            if x[2] is not "-":
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is not formatted correctly. Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                display.exec()
                raise Error
                return

            if int(xSplit[0]) - int(todayDate[-2:]) > 1:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is out of the acceptable range. Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                display.exec()
                raise Error
                return

            if len(xSplit[0])>2 or len(xSplit[1])>3:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Serial Number","The Serial Number " + str(x) + " is not formatted correctly. Please fix and try again.")
                display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                display.exec()
                raise Error
                return

            if SNList.count(x) > 1:
                display = QMessageBox(QMessageBox.Critical,"Duplicate Serial Number","The Serial Number " + str(x) + " occurs more than once in the list. Please clear the data and redo.")
                display.setWindowIcon(QtGui.QIcon("\\\photonix04\Quality Control\\QC\Spreadsheets, Forms & Information\Import for laser status\Installer\icon-x.ico"))
                display.exec()
                raise Error
                return

    def FindLaserDataFolder(year, SN):
        folderDir = "\\20" + year + " Laser Data"
        parentDir = "\\\PHOTONIX04\Laser Data and Test Reports\Test Reports (by Year)" + folderDir

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
