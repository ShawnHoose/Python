# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cat1Export.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys
import os
import time
from datetime import datetime
import xlwings as xw

class Error(Exception):
    pass

class SNError(Error):
    pass

class folderError(Error):
    pass

class dataError(Error):
    pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowOpacity(1.0)
        MainWindow.resize(550,300)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("background-color: #ABC8C0;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.fileFrame = QtWidgets.QFrame(self.centralwidget)
        self.fileFrame.setGeometry(QtCore.QRect(10, 0, 521, 41))
        self.fileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileFrame.setObjectName("fileFrame")

        self.widget = QtWidgets.QWidget(self.fileFrame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 491, 31))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setStyleSheet("QLineEdit{background-color:rgb(201, 201, 201)}")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.browseButton = QtWidgets.QPushButton(self.widget)
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setStyleSheet("QPushButton{background-color:#9EE493; color:black;} ::pressed{color:#9ee493; background-color:black}")
        self.horizontalLayout.addWidget(self.browseButton)

        self.progFrame = QtWidgets.QFrame(self.centralwidget)
        self.progFrame.setGeometry(QtCore.QRect(20, 270, 501, 41))
        self.progFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.progFrame.setObjectName("progFrame")

        self.progressBar = QtWidgets.QProgressBar(self.progFrame)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 491, 23))
        self.progressBar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 5px;text-align: center;}::chunk{background-color: #35D1BA;width: 20px;}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 50, 501, 211))
        self.widget1.setObjectName("widget1")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tableFrame = QtWidgets.QFrame(self.widget1)
        self.tableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableFrame.setObjectName("tableFrame")

        self.tableWidget = QtWidgets.QTableWidget(self.tableFrame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 151, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("QTableWidget{background:#DAF7DC;}")
        self.horizontalLayout_2.addWidget(self.tableFrame)

        self.exportFrame = QtWidgets.QFrame(self.widget1)
        self.exportFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exportFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exportFrame.setObjectName("exportFrame")

        self.exportButton = QtWidgets.QPushButton(self.exportFrame)
        self.exportButton.setGeometry(QtCore.QRect(50, 0, 180, 160))
        self.exportButton.setObjectName("exportButton")
        self.exportButton.setStyleSheet("QPushButton{background-color: #35D1BA}::pressed{color:white}")
        self.horizontalLayout_2.addWidget(self.exportFrame)

        self.clearButton = QtWidgets.QPushButton(self.exportFrame)
        self.clearButton.setGeometry(QtCore.QRect(98, 180,90,30))
        self.clearButton.setStyleSheet("QPushButton{background-color: #EAF2E3}::pressed{color:#EAF2E3; background-color: black;}")
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.clearSlot)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.workingLabel = QtWidgets.QLabel(self.centralwidget)
        self.workingLabel.setGeometry(QtCore.QRect(20, 100, 531, 81))
        self.workingLabel.setStyleSheet("QLabel{color: purple;font-size: 30px; background-color: rgba(255,255,255,0)}")
        self.workingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.workingLabel.setObjectName("workingLabel")
        self.workingLabel.hide()

        self.retranslateUi(MainWindow)
        self.browseButton.clicked.connect(self.browseSlot)
        self.exportButton.clicked.connect(self.exportSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QC Mass Cat 1 Data Export"))
        MainWindow.setWindowIcon(QtGui.QIcon("*REMOVED*"))
        self.label.setText(_translate("MainWindow", "File Location"))
        self.workingLabel.setText(_translate("MainWindow", "Working..."))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))

    def browseSlot(self):
        filename = self.openDialog()
        self.lineEdit.setText(filename)
        return

    def clearSlot(self):
        self.tableWidget.clear()
        self.progressBar.hide()
        self.progressBar.setValue(0)
        display = QMessageBox(QMessageBox.NoIcon,"Table Cleared","The table has been cleared of all data!")
        display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
        display.exec()

    def exportSlot(self):
        destLoc = self.lineEdit.text()
        if len(destLoc) < 4:
            display = QMessageBox(QMessageBox.Critical,"Cat1 Sheet not selected","No Cat1 sheet has been selected! Select one and try again.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            return

        snDict = {}
        for i in range(self.tableWidget.rowCount()):
            SN = self.tableWidget.item(i,0)
            if SN:
                if SN.text() and not SN.text().isspace():
                    if SN.text() in snDict:
                        display = QMessageBox(QMessageBox.Warning,"Duplicate SN found","S/N " + SN.text() + " is a duplicate. Skipping.")
                        display.exec()
                        continue
                    snDict[SN.text()] = ""

        try:
            Ui_MainWindow.SNCheck(snDict)
        except Error as e:
            return

        for SN in snDict.keys():
            try:
                finalFolder = Ui_MainWindow.findFolder(SN[:2],SN)
                snDict[SN] = finalFolder

                try:
                    for _,_,files in os.walk(snDict[SN]): #Get WaistSolver location
                        for file in files:
                            if "WaistSolverCopyVersion" in file:
                                srcLoc = snDict[SN] + "\\" + file
                except:
                    display = QMessageBox(QMessageBox.Warning,"Folder not found!","Could not find an appropriate folder for S/N " + SN + "! Please ensure it exists and try again.")
                    display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                    display.exec()
                    self.workingLabel.hide()
                    return

                snDict[SN] = srcLoc

            except folderError as e:
                display = QMessageBox(QMessageBox.Warning,"Folder not found!","Could not find an appropriate folder for S/N " + SN + "! Please ensure it exists and try again.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                return

            except ValueError as e:
                return

        if len(destLoc) < 2:
            display = QMessageBox(QMessageBox.Warning,"No Cat 1 Sheet selected!","Please select a Cat 1 sheet to import to before trying to export!")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            return

        excel_app = xw.App(visible=False)
        x = 1
        countMax = 100 / len(snDict)
        MainWindow.resize(550,325)
        self.progressBar.setValue(0)
        self.progressBar.show()
        self.workingLabel.show()
        app.processEvents()

        for SN in snDict.keys():
            srcWkBk = excel_app.books.open(snDict[SN]) #open source workbook
            tgtWkBk = excel_app.books.open(destLoc) #open target workbook
            tgtWkBk.calculation = 'manual'
            srcWkBk.calculation = 'manual'

            try:
                targetSheet = tgtWkBk.sheets["data"] #Target sheet
            except:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Excel Sheet","The Excel Sheet selected is not a Cat 1 sheet.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                self.workingLabel.hide()
                return

            try:
                dataSheet = srcWkBk.sheets["Data Import CAT1 & Outgoing"] #Cat 1 Data Sheet selection
            except:
                display = QMessageBox(QMessageBox.Critical,"Incorrect Excel Sheet","The Waist Solver selected is not a Waist Solver.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                self.workingLabel.hide()
                return

            copyData = dataSheet["A5:AT5"].value #Copy Cat 1 data

            try:
                Ui_MainWindow.dataCheck(copyData) #Check if data is blank
            except dataError as e:
                self.workingLabel.hide()
                return

            targetRow = targetSheet["F" + str(targetSheet.cells.last_cell.row)].end('up').row + 1 #Target row

            rng = "F" + str(targetRow) + ":AY" + str(targetRow) #Target Range string
            targetRange = targetSheet[rng]
            targetRange.value = copyData

            snCell = "D" + str(targetRow) #SN Cell copy and paste
            targetSheet[snCell].value = dataSheet["D8"].value

            srcWkBk.calculation = 'automatic'
            tgtWkBk.calculation = 'automatic'

            tgtWkBk.save(destLoc) #save and quit workbooks

            tgtWkBk.close()
            srcWkBk.close()
            excel_app.quit()

            self.progressBar.setValue(x*countMax)
            app.processEvents()
            x += 1

        self.workingLabel.hide()
        exportLoc = destLoc
        display = QMessageBox(QMessageBox.Information,"Export Complete","All of the data has been exported to " + exportLoc + ".")
        display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
        display.exec()
        self.progressBar.hide()
        MainWindow.resize(550,300)
        return

    def openDialog(self): #Open file selector dialog box
        dialog = QFileDialog(MainWindow)
        filter = "Excel Files (*.xls)"
        path = "*REMOVED*"
        title = "Open Cat 1 Data Sheet"
        filename, _ = QFileDialog.getOpenFileName(dialog,title,path,filter)

        if len(filename) > 1:
            return filename
        else:
            display = QMessageBox(QMessageBox.Warning,"No File Selected","No Cat 1 Data sheet has been selected.")
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

        for x in SNList.keys():
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

    def findFolder(year, SN):
        folderDir = "\\20" + year + " Laser Data"
        parentDir = "*REMOVED*

        dt = datetime.now().date()
        date = '{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year%100)

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

        folders = {}
        for _, subdir, _ in os.walk(path2):
            for x in subdir:
                if "Final Test Report" in x:
                    folderDate = x.split(" ")[-1][1:-1]
                    folderDateSplit = folderDate.split("-")
                    folderDateYear = folderDateSplit[-1]

                    if len(folderDateYear) > 2:
                        folderDateYear = folderDateYear[:-2]
                        folderDateSplit[-1] = folderDateYear
                        folderDate = "-".join(folderDateSplit)

                    delta = (datetime.strptime(date, "%m-%d-%y") - datetime.strptime(folderDate, "%m-%d-%y")).days

                    folders[x] = delta

            try:
                mostRecent = min(folders.values())
            except ValueError as e:
                display = QMessageBox(QMessageBox.Warning,"Folder not found!","Could not find an appropriate folder for S/N " + SN + "! Please ensure it exists and try again.")
                display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
                display.exec()
                raise ValueError
                return

            targetFolder = [key for key in folders if folders[key] == mostRecent]
            targetFolder = "".join(targetFolder)

        if len(folders) == 0:
            raise folderError

        returnFolder = path2 + "\\" + targetFolder
        return returnFolder

    def dataCheck(dataList):
        blank = True
        for x in dataList:
            if x != 0.0:
                blank = False

        if blank:
            display = QMessageBox(QMessageBox.Information,"Blank Cat  1Data","The Cat 1 data is blank. Not copying.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            raise dataError
            return
        else:
            return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
