# -*- coding: utf-8 -*-

# **************************** My import*****************************
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import DSpliceMPL
import sys


# import DSpliceMPL
# **************************** My import*****************************

class Ui_DroneGUI(QWidget):
# **************************** My initialtion*****************************
    def __init__(self):
        super().__init__()
        self.setupUi()

# **************************** My initialtion*****************************



    def setupUi(self):
        DroneGUI.setObjectName("DroneGUI")
        DroneGUI.resize(647, 522)
        self.centralwidget = QtWidgets.QWidget(DroneGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 80, 150, 21))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 130, 191, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton_3.setGeometry(QtCore.QRect(40, 180, 140, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 230, 191, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 280, 138, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 0, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 450, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 450, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(260, 230, 141, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 141, 16))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(260, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(260, 250, 256, 192))
        self.listWidget_2.setObjectName("listWidget_2")

# **************************** My Code_Multi-selectionmode *****************************
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.listWidget_2.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )

# **************************** My Code_Multi-selectionmode *****************************
# **************************** My Code_Qlistwidget_2 *****************************

        self.pushButton_6.clicked.connect(self.addtolist)
        self.pushButton_7.clicked.connect(self.removeitem)

# **************************** My Code_Qlistwidget_2 *****************************
        DroneGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DroneGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 21))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.Import_Data = QtWidgets.QMenu(self.File)
        self.Import_Data.setObjectName("Import_Data")
        self.Edit = QtWidgets.QMenu(self.menubar)
        self.Edit.setObjectName("Edit")
        self.Analysis = QtWidgets.QMenu(self.menubar)
        self.Analysis.setObjectName("Analysis")
        DroneGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DroneGUI)
        self.statusbar.setObjectName("statusbar")
        DroneGUI.setStatusBar(self.statusbar)
        self.Training_Data = QtWidgets.QAction(DroneGUI)
        self.Training_Data.setObjectName("Training_Data")
        self.Test_Data = QtWidgets.QAction(DroneGUI)
        self.Test_Data.setObjectName("Test_Data")
        self.Current_Datasets = QtWidgets.QAction(DroneGUI)
        self.Current_Datasets.setObjectName("Current_Datasets")
        self.Splice_Data = QtWidgets.QAction(DroneGUI)
        self.Splice_Data.setObjectName("Splice_Data")
        self.Edit_Selected_Datasets = QtWidgets.QAction(DroneGUI)
        self.Edit_Selected_Datasets.setObjectName("Edit_Selected_Datasets")
        self.Feature_Vector_Plotting = QtWidgets.QAction(DroneGUI)
        self.Feature_Vector_Plotting.setObjectName("Feature_Vector_Plotting")
        self.actionConfusion_Matrix = QtWidgets.QAction(DroneGUI)
        self.actionConfusion_Matrix.setObjectName("actionConfusion_Matrix")
        self.actionTest_Data_Analysis_Report = QtWidgets.QAction(DroneGUI)
        self.actionTest_Data_Analysis_Report.setObjectName("actionTest_Data_Analysis_Report")
        self.Edit_Feature_Vector = QtWidgets.QAction(DroneGUI)
        self.Edit_Feature_Vector.setObjectName("Edit_Feature_Vector")
        self.Manual_Mode_Switch = QtWidgets.QAction(DroneGUI)
        self.Manual_Mode_Switch.setObjectName("Manual_Mode_Switch")
        self.Import_Data.addAction(self.Training_Data)
        self.Import_Data.addAction(self.Test_Data)
        self.File.addAction(self.Import_Data.menuAction())
        self.File.addAction(self.Current_Datasets)
        self.File.addAction(self.Splice_Data)
        self.Edit.addAction(self.Edit_Selected_Datasets)
        self.Edit.addAction(self.Edit_Feature_Vector)
        self.Edit.addAction(self.Manual_Mode_Switch)
        self.Analysis.addAction(self.Feature_Vector_Plotting)
        self.Analysis.addAction(self.actionConfusion_Matrix)
        self.Analysis.addSeparator()
        self.Analysis.addAction(self.actionTest_Data_Analysis_Report)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Edit.menuAction())
        self.menubar.addAction(self.Analysis.menuAction())
# **************************** My Code_Triggrr open file *****************************
        self.Training_Data.triggered.connect(self.import_training_data)

# **************************** My Code_Triggrr open file *****************************
        self.retranslateUi(DroneGUI)
        QtCore.QMetaObject.connectSlotsByName(DroneGUI)
# **************************** My code_splicing the data button clicked*****************************
        self.pushButton_3.clicked.connect(self.datasplicing)

# **************************** My code_splicing the data button clicked*****************************

    def retranslateUi(self, DroneGUI):
        _translate = QtCore.QCoreApplication.translate
        DroneGUI.setWindowTitle(_translate("DroneGUI", "DroneGUI"))
        self.pushButton_1.setText(_translate("DroneGUI", "Show All Datasets"))
        self.pushButton_2.setText(_translate("DroneGUI", "Select Spacific Dataset(s)"))
        self.pushButton_3.setText(_translate("DroneGUI", "Datasets Splicing"))
        self.pushButton_4.setText(_translate("DroneGUI", "Feature Vectors Labelling"))
        self.pushButton_5.setText(_translate("DroneGUI", "Confusion Matrix"))
        self.pushButton_6.setText(_translate("DroneGUI", "Add"))
        self.pushButton_7.setText(_translate("DroneGUI", "Delete"))
        self.label_1.setText(_translate("DroneGUI", "Selected Datasets"))
        self.label_2.setText(_translate("DroneGUI", "All Datasets"))
        self.File.setTitle(_translate("DroneGUI", "File"))
        self.Import_Data.setTitle(_translate("DroneGUI", "Import Data"))
        self.Edit.setTitle(_translate("DroneGUI", "Edit"))
        self.Analysis.setTitle(_translate("DroneGUI", "Analysis"))
        self.Training_Data.setText(_translate("DroneGUI", "Training Data"))
        self.Test_Data.setText(_translate("DroneGUI", "Test Data"))
        self.Current_Datasets.setText(_translate("DroneGUI", "Current Selected Datasets"))
        self.Splice_Data.setText(_translate("DroneGUI", "Splice Data and labelling"))
        self.Edit_Selected_Datasets.setText(_translate("DroneGUI", "Edit Selected Datasets"))
        self.Feature_Vector_Plotting.setText(_translate("DroneGUI", "Feature Vector Plotting"))
        self.actionConfusion_Matrix.setText(_translate("DroneGUI", "Confusion Matrix"))
        self.actionTest_Data_Analysis_Report.setText(_translate("DroneGUI", "Test Data Analysis Report"))
        self.Edit_Feature_Vector.setText(_translate("DroneGUI", "Edit Feature Vector"))
        self.Manual_Mode_Switch.setText(_translate("DroneGUI", "Manual Mode Switch"))

# **********************************************************************************
# ******************************* -------------------  *****************************
#  ****************************   | Define functions:|   *****************************
# ******************************  ---------------------- ****************************
# **********************************************************************************
# **************************** My Code_def_addtolist & remove*****************************

    def addtolist(self):
        selecteditem=self.listWidget.selectedItems()
        for i in range (len(selecteditem)):
            self.listWidget_2.addItem(self.listWidget.selectedItems()[i].text())


    def removeitem(self):
        selecteditem2=self.listWidget_2.selectedItems()
        for i in selecteditem2:
            self.listWidget_2.takeItem(self.listWidget_2.row(i))


      #  self.listWidget_2.takeItem(self.listWidget_2.currentRow())
    # print the selected item text
    # def printItemText(self):
    #     items = self.listWidget.selectedItems()
    #     x = []
    #     for i in range(len(items)):
    #         x.append(str(self.listWidget.selectedItems()[i].text()))
    #
    #     print (x)

# **************************** My Code_define addtolist & remove*****************************


# **************************** My Code_import training data*****************************
    def import_training_data(self):


        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Training datasets import)", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        # if files:
        # print(files)

        for i in range(len(files)):
            item = QtWidgets.QListWidgetItem(files[i])
            self.listWidget.addItem(item)



# **************************** My Code_import training data*****************************
# ****************************    My Code_data splice       *****************************
    def datasplicing(self):
        # from PyQt5.QtCore import pyqtRemoveInputHook
        # from pdb import set_trace
        # pyqtRemoveInputHook()
        # set_trace()

        readedFileList = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
        # print(readedFileList)
        # import os
        # from DSpliceMPL import ADDRESS, change_address
        # change_address(readedFileList[0])
        # os.system("DSpliceMPL.py")

        DSpliceMPL.get_data(readedFileList[0])








# ****************************    My Code_data splice      *****************************
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    DroneGUI = QtWidgets.QMainWindow()
    ui = Ui_DroneGUI()
    # ui.setupUi(DroneGUI)

    DroneGUI.show()
    sys.exit(app.exec_())

