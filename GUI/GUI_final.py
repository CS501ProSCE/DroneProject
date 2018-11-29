# -*- coding: utf-8 -*-

# **************************** My import *********************************
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from matplotlib.figure import Figure
import GUIFunctions
# import SpliceDataFunctions
# import Learn
# import Learn_original
import sys
from parameterGUI import Ui_parameterSelection
import multi_param_learn
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from splicing import  Ui_Splicing_mode_Dialog

# **************************** My import *********************************

# **************************** Class Canvas  *****************************
class Figure_Canvas(FigureCanvas):

    def __init__(self, parent=None, width=3.28, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig) #
        FigureCanvas.updateGeometry(self)
        self.setParent(parent)

        # Figure_Canvas.set_window_title(self,"hello")

        self.axes = fig.add_subplot(111)

    def test(self,a):
        self.axes.plot(a)
        # a=SpliceDataFunctions.getTSData(Ui_DroneGUI.readedFileList[0])
        # self.axes.plot(a)
        # print (Ui_DroneGUI().return_plot())

# **************************** Class Canvas  *****************************





class Ui_DroneGUI(QWidget):
# **************************** My initialtion ************************
    def __init__(self, parent=None):
        super(Ui_DroneGUI, self).__init__()
        self.setupUi()
        self.ui = Ui_parameterSelection()
# **************************** My initialtion ************************
    def setupUi(self):
        DroneGUI.setObjectName("DroneGUI")
        DroneGUI.resize(616, 508)
        self.centralwidget = QtWidgets.QWidget(DroneGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 0, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(260, 20, 351, 471))
        self.tab.setObjectName("tab")
        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.layoutWidget = QtWidgets.QWidget(self.Data)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 390, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.Data)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 299, 150))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.Data)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 299, 13))
        self.label_2.setObjectName("label_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.Data)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 230, 299, 150))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_1 = QtWidgets.QLabel(self.Data)
        self.label_1.setGeometry(QtCore.QRect(20, 211, 320, 16))
        self.label_1.setObjectName("label_1")
        self.tab.addTab(self.Data, "")
        self.Parameter = QtWidgets.QWidget()
        self.Parameter.setObjectName("Parameter")
        self.listWidget_3 = QtWidgets.QListWidget(self.Parameter)
        self.listWidget_3.setGeometry(QtCore.QRect(30, 50, 281, 321))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label = QtWidgets.QLabel(self.Parameter)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 31))
        self.label.setObjectName("label")
        self.pushButton_11 = QtWidgets.QPushButton(self.Parameter)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 390, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tab.addTab(self.Parameter, "")
        self.Graph = QtWidgets.QWidget()
        self.Graph.setObjectName("Graph")
        self.graphicsView = QtWidgets.QGraphicsView(self.Graph)
        self.graphicsView.setGeometry(QtCore.QRect(10, 100, 331, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_1 = QtWidgets.QPushButton(self.Graph)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 20, 199, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.Graph)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 199, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tab.addTab(self.Graph, "")
        self.Report = QtWidgets.QWidget()
        self.Report.setObjectName("Report")
        self.textBrowser = QtWidgets.QTextBrowser(self.Report)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 311, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.Report)
        self.pushButton.setGeometry(QtCore.QRect(110, 390, 131, 23))
        self.pushButton.setObjectName("pushButton")
        self.tab.addTab(self.Report, "")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 201, 431))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 0, 1, 1)
        DroneGUI.setCentralWidget(self.centralwidget)
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

        self.retranslateUi(DroneGUI)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DroneGUI)


# **************************** My Code_Multi-selectionmode *****************
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
# **************************** My Code_Multi-selectionmode *****************

# **************************** My Code_select parameter*********************
        self.pushButton_2.clicked.connect(self.show_parameter)
# **************************** My Code_select parameter*********************

# **************************** My Code_Qlistwidget_2 ***********************
        self.pushButton_6.clicked.connect(self.addtolist)
        self.pushButton_7.clicked.connect(self.removeitem)
# **************************** My Code_Qlistwidget_2 ***********************

# **************************** My Code_Trigger open file *******************
        self.pushButton_13.clicked.connect(self.import_training_data)
# **************************** My Code_Trigger open file *******************

# **************************** My Code_splice data automatically ***********
        self.pushButton_4.clicked.connect(self.datasplicing_mode_selection)
# **************************** My Code_splice data automatically ***********

# **************************** My code_show training data*******************
        self.pushButton_1.clicked.connect(self.traning_data_display)
# **************************** My code_show traing data*********************

# **************************** My code_show test data **********************
        self.pushButton_3.clicked.connect(self.test_data_display)
# **************************** My code_show test data **********************

# **************************** My code_splicing the data button clicked ****
        self.pushButton_5.clicked.connect(self.machinelearning)
# **************************** My code_splicing the data button clicked ****

# **************************** My code_delete parameter ********************
        self.pushButton_11.clicked.connect(self.del_parameter)
# **************************** My code_delete parameter ********************


    def retranslateUi(self, DroneGUI):
        _translate = QtCore.QCoreApplication.translate
        DroneGUI.setWindowTitle(_translate("DroneGUI", "DroneGUI"))
        self.pushButton_6.setText(_translate("DroneGUI", "Add"))
        self.pushButton_7.setText(_translate("DroneGUI", "Delete"))
        self.label_2.setText(_translate("DroneGUI", "All Test  Datasets"))
        self.label_1.setText(_translate("DroneGUI", "Selected Test Datasets to Predict (1 file per run)"))
        self.tab.setTabText(self.tab.indexOf(self.Data), _translate("DroneGUI", "Data"))
        self.label.setText(_translate("DroneGUI", "Parameter Selected"))
        self.pushButton_11.setText(_translate("DroneGUI", "Delete"))
        self.tab.setTabText(self.tab.indexOf(self.Parameter), _translate("DroneGUI", "Parameter"))
        self.pushButton_1.setText(_translate("DroneGUI", "Show Training Data Profile"))
        self.pushButton_3.setText(_translate("DroneGUI", "Show Test Data Profile"))
        self.tab.setTabText(self.tab.indexOf(self.Graph), _translate("DroneGUI", "Prediction"))
        self.pushButton.setText(_translate("DroneGUI", "Make Report"))
        self.tab.setTabText(self.tab.indexOf(self.Report), _translate("DroneGUI", "Report"))
        self.pushButton_4.setText(_translate("DroneGUI", "Splice Test datasets"))
        self.pushButton_5.setText(_translate("DroneGUI", "Predict Disturbance"))
        self.pushButton_2.setText(_translate("DroneGUI", "Select Parameters"))
        self.pushButton_13.setText(_translate("DroneGUI", "Import Test Data"))
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

# *******************************************************************************
# ******************************* -------------------  **************************
#  ****************************   | Define functions |   ************************
# ******************************  -------------------    ************************
# *******************************************************************************

# **************************** My Code_import training data*********************
    def import_training_data(self):
        self.tab.setCurrentIndex(0)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Training datasets import)", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        # if files:
        # print(files)

        for i in range(len(files)):
            item = QtWidgets.QListWidgetItem(files[i])
            self.listWidget.addItem(item)



# **************************** My Code_import training data*********************

# **************************** My Code_def_addtolist & remove********************

    def addtolist(self):


        if self.listWidget_2.count() is 1:
            pass
        else:
            self.listWidget_2.addItem(self.listWidget.selectedItems()[0].text())
        # for i in range (len(selecteditem)):
        #     self.listWidget_2.addItem(self.listWidget.selectedItems()[i].text())
        self.listWidget.clearSelection()

    def removeitem(self):
        selecteditem=self.listWidget.selectedItems()
        for i in selecteditem:
            self.listWidget.takeItem(self.listWidget.row(i))

        selecteditem2=self.listWidget_2.selectedItems()

        for i in selecteditem2:
            self.listWidget_2.takeItem(self.listWidget_2.row(i))

# **************************** My Code_define addtolist & remove****************

# ****************************    My Code_data select paramter     *************

    def show_parameter(self):
        self.tab.setCurrentIndex(1)
        self.parameter=QtWidgets.QWidget()
        self.ui=Ui_parameterSelection()
        self.ui.setupUi(self.parameter)
        self.parameter.show()
        self.ui.Confirmation_buttonBox.accepted.connect(self.confirmed)


    def confirmed(self):
        self.para_dic2={"Pitch":"mavlink_ahrs3_t_pitch",
                       "Yaw":"mavlink_ahrs3_t_yaw","Pitch rate":"mavlink_attitude_t_pitch rate",
                       "Roll rate":"mavlink_attitude_t_roll rate",
                       "Yaw angle":"mavlink_attitude_t_yaw angle" ,"Roll":"mavlink_ahrs3_t_roll",
                       "Altitude":"mavlink_ahrs3_t_altitude","X Accel":"mavlink_raw_imu_t_Xaccel",
                       "X Gyro": "mavlink_raw_imu_t_XGyro","X Mag": "mavlink_raw_imu_t_XMag",
                        "Y Accel":"mavlink_raw_imu_t_Yaccel", "Y Gyro":"mavlink_raw_imu_t_YGyro", "Y Mag": "mavlink_raw_imu_t_YMag",
                       "Z Accel":"mavlink_raw_imu_t_Zaccel","Z Gyro":"mavlink_raw_imu_t_ZGyro","Z Mag":"mavlink_raw_imu_t_ZMag",
                        "Z vibration":"mavlink_vibration_t_vibration_z","Yaw rate":"mavlink_attitude_t_yaw rate"}
        self.para_dic = {"Pitch": "pitch",
                         "Yaw": "yaw", "Pitch rate": "pitch rate",
                         "Roll rate": "roll rate",
                         "Yaw angle": "yaw angle",
                         "Roll": "roll",
                         "Altitude": "altitude", "X Accel": "Xaccel",
                         "X Gyro": "XGyro", "X Mag": "XMag",
                         "Y Accel": "Yaccel", "Y Gyro": "YGyro",
                         "Y Mag": "YMag",
                         "Z Accel": "Zaccel", "Z Gyro": "ZGyro",
                         "Z Mag": "ZMag",
                         "Z vibration": "vibration_z","Yaw rate":"yaw rate"}

        global selection
        global selection_name
        self.selection_name=[]
        self.selection = []

        if self.ui.Pitch.isChecked():
            # self.selection.append("mavlink_nav_controller_output_t_nav_pitch")
            self.selection_name.append("Pitch")
        if self.ui.Yaw.isChecked():
            # self.selection.append("mavlink_ahrs3_t_yaw")
            self.selection_name.append("Yaw")
        if self.ui.Pitch_rate.isChecked():
            # self.selection.append("mavlink_attitude_t_pitch rate")
            self.selection_name.append("Pitch rate")
        if self.ui.Roll_rate.isChecked():
            # self.selection.append("mavlink_attitude_t_roll rate")
            self.selection_name.append("Roll rate")
        if self.ui.Yaw_angle.isChecked():
            # self.selection.append("mavlink_attitude_t_yaw angle")
            self.selection_name.append("Yaw angle")
        if self.ui.Roll.isChecked():
            # self.selection.append("mavlink_nav_controller_output_t_nav_roll")
            self.selection_name.append("Roll")
        if self.ui.Altitude.isChecked():
            # self.selection.append("mavlink_ahrs2_t_altitude")
            self.selection_name.append("Altitude")
        if self.ui.X_Accel.isChecked():
            # self.selection.append("mavlink_raw_imu_t_Xaccel")
            self.selection_name.append("X Accel")
        if self.ui.X_Gyro.isChecked():
            # self.selection.append("mavlink_raw_imu_t_XGyro")
            self.selection_name.append("X Gyro")
        if self.ui.X_Mag.isChecked():
            # self.selection.append("mavlink_raw_imu_t_XMag")
            self.selection_name.append("X Mag")
        if self.ui.Y_Accel.isChecked():
            # self.selection.append("mavlink_raw_imu_t_Yaccel")
            self.selection_name.append("Y Accel")
        if self.ui.Y_Gyro.isChecked():
            # self.selection.append("mavlink_raw_imu_t_YGyro")
            self.selection_name.append("Y Gyro")
        if self.ui.Y_Mag.isChecked():
            # self.selection.append("mavlink_raw_imu_t_YMag")
            self.selection_name.append("Y Mag")
        if self.ui.Z_Accel.isChecked():
            # self.selection.append("mavlink_raw_imu_t_Zaccel")
            self.selection_name.append("Z Accel")
        if self.ui.Z_Gyro.isChecked():
            # self.selection.append("mavlink_raw_imu_t_ZGyro")
            self.selection_name.append("Z Gyro")
        if self.ui.Z_Mag.isChecked():
            # self.selection.append("mavlink_raw_imu_t_ZMag")
            self.selection_name.append("Z Mag")
        if self.ui.Z_vibration.isChecked():
            # self.selection.append("mavlink_vibration_t_vibration_z")
            self.selection_name.append("Z vibration")
        if self.ui.Yaw_rate.isChecked():
            # self.selection.append("mavlink_vibration_t_vibration_z")
            self.selection_name.append("Yaw rate")
        self.parameter.close()


        for i in range(len(self.selection_name)):
            self.listWidget_3.addItem(self.selection_name[i])




# ****************************    My Code_data select paramter     *************

# ****************************    My Code_delete parameter     *****************

    def del_parameter(self):
        selecteditem3 = self.listWidget_3.selectedItems()
        for i in selecteditem3:
            self.listWidget_3.takeItem(self.listWidget_3.row(i))


# ****************************    My Code_delete parameter     *****************

# ****************************    My Code_data splice       ********************
    def datasplicing_mode_selection(self):

        self.mode_selection=QtWidgets.QDialog()
        self.ui2=Ui_Splicing_mode_Dialog()
        self.ui2.setupUi(self.mode_selection)
        self.mode_selection.show()
        self.ui2.buttonBox.accepted.connect(self.datasplicing)
        # self.ui.Confirmation_buttonBox.accepted.connect(self.confirmed)

    def datasplicing(self):
        self.tab.setCurrentIndex(2)
        self.para_selection = []
        self.para_selection2 = []
        self.para_selection_name = []
        self.x_test_final = []

        for i in range(self.listWidget_3.count()):
            self.para_selection_name.append(self.listWidget_3.item(i).text())
            self.para_selection.append(self.para_dic[self.listWidget_3.item(i).text()])
            self.para_selection2.append(self.para_dic2[self.listWidget_3.item(i).text()])
            self.readedFileList = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
            # print (self.readedFileList,self.para_selection,self.para_selection_name,self.para_selection2)

        print("Selected parameters are:", self.para_selection_name)



        if self.ui2.radioButton.isChecked(): #manual
            self.b = GUIFunctions.main(self.readedFileList[0], self.para_selection[0], self.para_selection_name[0])
            self.x_test_final.append(self.b[4])
            self.check = 0

            for i in range (1,len(self.para_selection)):

                self.x_test=GUIFunctions.main3(self.readedFileList[0],self.para_selection[i],self.b[3])
                self.x_test_final.append(self.x_test)


        if self.ui2.radioButton_2.isChecked(): #automatic
            self.check=1
            self.b = GUIFunctions.main2(self.readedFileList[0], self.para_selection[0])
            self.x_test_final.append(self.b[3])

            for i in range(1, len(self.para_selection)):
                # GUIFunctions.main3(self.readedFileList[0],self.para_selection[i],self.b[1])
                self.x_test2=GUIFunctions.main4(self.readedFileList[0], self.para_selection[i], self.b[1])

                self.x_test_final.append(self.x_test2)

        self.dr = Figure_Canvas()

        # a = GUIFunctions.csvParaExtract(self.readedFileList[0], self.para_selection[0])[0]

        # a = SpliceDataFunctions.getTSData(self.readedFileList[0])
        self.dr.test(self.b[0])
        self.graphicscene = QtWidgets.QGraphicsScene()  #
        self.graphicscene.addWidget(self.dr)  #
        self.graphicsView.setScene(self.graphicscene)  #
        self.graphicsView.show()  #
        # self.graphicsView.setAutoFillBackground()

        # self.setCentralWidget(self.graphicsView)
        # self.graphicsView.setFixedSize(100, 600)


# ****************************    My Code_data splice      ********************

# ****************************    My Code_display prediction   ****************
    def machinelearning(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                    'Enter K value: ')
        if ok:
            self.k_value=int(text)
            # print (self.k_value)


            self.learning = multi_param_learn.multi_param_learn(self.para_selection2,None,'Data/')


            # self.label_result=Learn_original.machine_learning(self.learning[0],self.learning[1],self.learning[2],self.learning[3])
            self.label_result = multi_param_learn.machine_learning(self.x_test_final, self.learning[1], self.learning[2],self.learning[3],self.learning[4],self.learning[5],self.learning[6],self.k_value)

            print ("detection result: ",self.label_result[0])

            print("majority voting result: ",self.label_result[1])


            multi_param_learn.test_data_plot(self.para_selection_name[0],self.x_test_final[0])
            # print (self.label_result)
            if self.check==0:
                GUIFunctions.distLabel(self.b[0],self.b[1],self.label_result[1],self.para_selection_name[0])
            if self.check==1:
                GUIFunctions.distLabelAuto(self.b[0],self.b[1],self.label_result[1],self.para_selection_name[0])
        else:
            pass



# ****************************    My Code_display prediction   ****************


# ****************************    My Code_display training data     ************
    def traning_data_display(self):
        learning = multi_param_learn.multi_param_learn(self.para_selection2,None,'Data/')
        print (self.para_selection_name[0])
        # print (learning[1][0])
        # print (learning[2][0])
        # print (learning[3][0])
        multi_param_learn.training_data_plot(self.para_selection_name[0],learning[1][0],learning[2][0],learning[3])

# ****************************    My Code_display training data     ************

# ****************************    My Code_display test data         ************
    def test_data_display(self):
        self.a= GUIFunctions.csvParaExtract(self.readedFileList[0],self.para_selection[0])[0]
        # a= SpliceDataFunctions.getTSData(self.readedFileList[0])
        GUIFunctions.plotTSData(self.a,self.para_selection_name[0])
        # SpliceDataFunctions.plotTSData()
# ****************************    My Code_display test data         ************
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DroneGUI = QtWidgets.QMainWindow()
    ui = Ui_DroneGUI()
    # ui.setupUi(DroneGUI)
    DroneGUI.show()
    sys.exit(app.exec_())
