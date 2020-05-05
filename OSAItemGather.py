# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OSAItemGather.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import os
import win32com.client
import xlwings as xw

class Error(Exception):
    pass

class idError(Error):
    pass

class inputError(Error):
    pass

class Ui_MainWindow(QObject):
    global version
    version = "1.0"
    global sheetLoc
    sheetLoc = "*REMOVED*"
    global masterFolderLoc
    masterFolderLoc = "*REMOVED*"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setStyleSheet("background-color: #f0ebda")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inputFrame = QtWidgets.QFrame(self.centralwidget)
        self.inputFrame.setGeometry(QtCore.QRect(100, 30, 391, 61))
        self.inputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputFrame.setObjectName("inputFrame")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.inputFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutInput = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutInput.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutInput.setObjectName("horizontalLayoutInput")

        self.itemLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.itemLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.itemLabel.setObjectName("itemLabel")

        self.horizontalLayoutInput.addWidget(self.itemLabel)
        self.itemLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.itemLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.itemLineEdit.setObjectName("itemLineEdit")
        self.itemLineEdit.setStyleSheet("background-color: #e2e2e2")
        self.horizontalLayoutInput.addWidget(self.itemLineEdit)

        self.gatherButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.gatherButton.setDefault(True)
        self.gatherButton.setObjectName("gatherButton")
        self.gatherButton.setStyleSheet("background-color: #BCDFC1")
        self.horizontalLayoutInput.addWidget(self.gatherButton)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.openFolderCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.openFolderCheck.setObjectName("openFolderCheck")
        self.verticalLayout.addWidget(self.openFolderCheck)
        self.openFileCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.openFileCheck.setObjectName("openFileCheck")
        self.verticalLayout.addWidget(self.openFileCheck)

        self.horizontalLayoutInput.addLayout(self.verticalLayout)

        #Display retreived data
        self.dataFrame = QtWidgets.QFrame(self.centralwidget)
        self.dataFrame.setGeometry(QtCore.QRect(10, 110, 380, 340))
        self.dataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataFrame.setObjectName("dataFrame")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.dataFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 380, 340))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutData = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayoutData.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutData.setObjectName("horizontalLayoutData")

        self.labelVertLayout = QtWidgets.QVBoxLayout()
        self.labelVertLayout.setObjectName("labelVertLayout")

        self.revLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.revLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.revLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.revLabel.setObjectName("revLabel")
        self.labelVertLayout.addWidget(self.revLabel)

        self.itemDescriptionLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.itemDescriptionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.itemDescriptionLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.itemDescriptionLabel.setObjectName("itemDescriptionLabel")
        self.labelVertLayout.addWidget(self.itemDescriptionLabel)

        self.procedureLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.procedureLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.procedureLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.procedureLabel.setObjectName("procedureLabel")
        self.labelVertLayout.addWidget(self.procedureLabel)

        self.procedureNumberLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.procedureNumberLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.procedureNumberLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.procedureNumberLabel.setObjectName("procedureNumberLabel")
        self.labelVertLayout.addWidget(self.procedureNumberLabel)

        self.oldProcedureNumberLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.oldProcedureNumberLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.oldProcedureNumberLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.oldProcedureNumberLabel.setObjectName("oldProcedureNumberLabel")
        self.labelVertLayout.addWidget(self.oldProcedureNumberLabel)

        self.newProcRevLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.newProcRevLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.newProcRevLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.newProcRevLabel.setObjectName("newProcRevLabel")
        self.labelVertLayout.addWidget(self.newProcRevLabel)

        self.weightLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.weightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weightLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.weightLabel.setObjectName("weightLabel")
        self.labelVertLayout.addWidget(self.weightLabel)

        self.horizontalLayoutData.addLayout(self.labelVertLayout)
        self.dataVertLayout = QtWidgets.QVBoxLayout()
        self.dataVertLayout.setObjectName("dataVertLayout")

        self.revData = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.revData.setText("")
        self.revData.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.revData.setAlignment(QtCore.Qt.AlignVCenter)
        self.revData.setObjectName("revData")
        self.dataVertLayout.addWidget(self.revData)

        self.itemDescData = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.itemDescData.setText("")
        self.itemDescData.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.itemDescData.setAlignment(QtCore.Qt.AlignVCenter)
        self.itemDescData.setObjectName("itemDescData")
        self.dataVertLayout.addWidget(self.itemDescData)

        self.procedureData = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.procedureData.setText("")
        self.procedureData.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.procedureData.setAlignment(QtCore.Qt.AlignVCenter)
        self.procedureData.setObjectName("procedureData")
        self.dataVertLayout.addWidget(self.procedureData)

        self.procedureNumberData = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.procedureNumberData.setText("")
        self.procedureNumberData.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.procedureNumberData.setAlignment(QtCore.Qt.AlignVCenter)
        self.procedureNumberData.setObjectName("procedureNumberData")
        self.dataVertLayout.addWidget(self.procedureNumberData)

        self.oldProcedureNumberData = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.oldProcedureNumberData.setText("")
        self.oldProcedureNumberData.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.oldProcedureNumberData.setAlignment(QtCore.Qt.AlignVCenter)
        self.oldProcedureNumberData.setObjectName("oldProcedureNumberData")
        self.dataVertLayout.addWidget(self.oldProcedureNumberData)

        self.newProcRevData = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.newProcRevData.setText("")
        self.newProcRevData.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.newProcRevData.setAlignment(QtCore.Qt.AlignVCenter)
        self.newProcRevData.setObjectName("newProcRevData")
        self.dataVertLayout.addWidget(self.newProcRevData)

        self.weightData = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.weightData.setText("")
        self.weightData.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.weightData.setAlignment(QtCore.Qt.AlignVCenter)
        self.weightData.setObjectName("weightData")
        self.dataVertLayout.addWidget(self.weightData)

        self.horizontalLayoutData.addLayout(self.dataVertLayout)

        self.dataFrame.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Procedure frame and textedit
        self.procedureFrame = QtWidgets.QFrame(self.centralwidget)
        self.procedureFrame.setGeometry(QtCore.QRect(410, 110, 321, 341))
        self.procedureFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.procedureFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.procedureFrame.setObjectName("procedureFrame")

        self.procedureText = QtWidgets.QTextEdit(self.procedureFrame)
        self.procedureText.setGeometry(QtCore.QRect(0, 0, 321, 341))
        self.procedureText.setStyleSheet("background-color:white")
        self.procedureText.setObjectName("procedureText")

        self.procedureFrame.hide()

        self.retranslateUi(MainWindow)
        self.gatherButton.clicked.connect(self.gatherSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OSA Item ID Lookup v" + version))
        self.itemLabel.setText(_translate("MainWindow", "Item ID"))
        self.gatherButton.setText(_translate("MainWindow", "Gather"))
        self.openFolderCheck.setText(_translate("MainWindow", "Open Procedure Folder"))
        self.openFileCheck.setText(_translate("MainWindow", "Display Procedure"))
        self.revLabel.setText(_translate("MainWindow", "Rev:"))
        self.itemDescriptionLabel.setText(_translate("MainWindow", "Item Description:"))
        self.procedureLabel.setText(_translate("MainWindow", "Procedure Name:"))
        self.procedureNumberLabel.setText(_translate("MainWindow", "New Procedure #:"))
        self.oldProcedureNumberLabel.setText(_translate("MainWindow", "Old Procedure #:"))
        self.newProcRevLabel.setText(_translate("MainWindow", "New Procedure Rev:"))
        self.weightLabel.setText(_translate("MainWindow", "Weight:"))


    @pyqtSlot()
    def gatherSlot(self):
        try:
            itemNumb = self.itemLineEdit.text()
            self.itemIDCheck(itemNumb)
        except idError as e:
            display = QMessageBox(QMessageBox.Critical,"Improper Item ID","The Item ID provided is improper. Please correct and try again.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            return
        except inputError as e:
            display = QMessageBox(QMessageBox.Critical,"No Item ID","No Item ID has been input. Please input and try again.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            return

        try:
            self.pullData(itemNumb)
        except idError as e:
            return

        MainWindow.resize(600,500)
        self.dataFrame.show()

        if self.openFolderCheck.isChecked():
            os.startfile(masterFolderLoc)

        if self.openFileCheck.isChecked():
            self.procedureFrame.show()
            MainWindow.resize(750,500)

            try:#Try to open procedure file, display error if there is no file
                self.findFile(itemNumb)
            except idError as e:
                return

        return

    def itemIDCheck(self, id):
        if len(id) != 7:
            if len(id) == 0:
                raise inputError
            if len(id) > 7:
                if id[-2] != "-":
                    raise idError
            else:
                raise idError
        if len(id) == 7:
            try:
                type(int(id))
            except:
                raise idError
        return

    def pullData(self, id):
        global sheetLoc
        data = []

        #Clear old data
        self.revData.setText("")
        self.itemDescData.setText("")
        self.procedureData.setText("")
        self.procedureNumberData.setText("")
        self.oldProcedureNumberData.setText("")
        self.newProcRevData.setText("")
        self.weightData.setText("")
        app.processEvents()

        excel_app = xw.App(visible=False)

        srcWkBk = excel_app.books.open(sheetLoc)
        srcWkBk.calculation = 'manual'

        try:
            targetSheet = srcWkBk.sheets["For ERP"]
        except:
            display = QMessageBox(QMessageBox.Critical,"Incorrect Excel Sheet","The Excel Sheet selected is not the correct sheet. Correct the error in the sheet, please.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()

        lastRow = targetSheet["A" + str(targetSheet.cells.last_cell.row)].end('up').row

        i = 2

        while i <= lastRow:
            try:
                currentBox = int(targetSheet["A" + str(i)].value)
            except ValueError:
                currentBox = targetSheet["A" + str(i)].value

            if str(currentBox) == str(id):
                rng = "B" + str(i) + ":H" + str(i)
                if len(data) == 1:
                    del data[:] #deletes (to clear up memory) and remakes list
                    data=[]
                data.append(targetSheet.range(rng).value)
            i += 1

        srcWkBk.calculation = 'automatic'
        srcWkBk.close()
        excel_app.quit()

        #data assignments
        try:
            self.revData.setText(str(data[0][0]))
            self.itemDescData.setText(str(data[0][1]))
            self.procedureData.setText(str(data[0][3]))
            self.procedureNumberData.setText(str(int(data[0][4])))
            self.oldProcedureNumberData.setText(str(int(data[0][2])))
            self.newProcRevData.setText(str(data[0][5]))
            self.weightData.setText(str(data[0][6]))
        except:
            display = QMessageBox(QMessageBox.Critical,"No Item ID Found","No Item ID " + str(id) + " was found. Please enter another ID and try again.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*o"))
            display.exec()
            raise idError

    def findFile(self, id):
        folderDir = "*REMOVED*"
        content = ""
        found = False
        for _,_,files in os.walk(folderDir): #Walk through all files in folder
            for filename in files:
                if str(id) in filename: #If procedure doc found
                    found = True #error tracer
                    #Start instance of word
                    wordApp = win32com.client.gencache.EnsureDispatch("Word.Application")
                    #Hide word window
                    wordApp.Visible = False
                    #open the doc
                    doc = wordApp.Documents.Open(os.path.join(folderDir,filename))
                    #Copy string of all contents of doc TODO: FIX FORMATTING ISSUE
                    content = str(doc.Range())
                    #Quit out of everything
                    doc.Close()
                    wordApp.Quit()
                    self.procedureText.setText(content)
                    app.processEvents()

        if not found:
            MainWindow.resize(600,500)
            self.procedureFrame.hide()
            display = QMessageBox(QMessageBox.Critical,"No Item ID Procedure","No procedure document found. Unable to display. Please check in folder to ensure proper naming convention.")
            display.setWindowIcon(QtGui.QIcon("*REMOVED*"))
            display.exec()
            return

        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
