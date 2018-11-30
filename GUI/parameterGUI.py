# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_parameterSelection(QtWidgets.QDialog):
# # ****************************    My Code_define_non_parent    *****************************
#     def __init__(self):
#
#         super(Ui_parameterSelection, self).__init__(parent)

        #
        # buttonBox = QtWidgets.QDialogButtonBox()
        # buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        # buttonBox.accepted.connect(self.accept)
        # buttonBox.rejected.connect(self.reject)

# # ****************************    My Code_define_non_parent    *****************************

    def setupUi(self, parameterSelection):
        parameterSelection.setObjectName("parameterSelection")
        parameterSelection.resize(321, 205)
        self.Confirmation_buttonBox = QtWidgets.QDialogButtonBox(parameterSelection)
        self.Confirmation_buttonBox.setGeometry(QtCore.QRect(90, 170, 156, 23))
        self.Confirmation_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)

        self.Confirmation_buttonBox.setObjectName("Confirmation_buttonBox")
        self.widget = QtWidgets.QWidget(parameterSelection)
        self.widget.setGeometry(QtCore.QRect(21, 10, 270, 136))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.X_Gyro = QtWidgets.QCheckBox(self.widget)
        self.X_Gyro.setObjectName("X_Gyro")
        self.gridLayout.addWidget(self.X_Gyro, 0, 0, 1, 1)
        self.Y_Gyro = QtWidgets.QCheckBox(self.widget)
        self.Y_Gyro.setObjectName("Y_Gyro")
        self.gridLayout.addWidget(self.Y_Gyro, 1, 0, 1, 1)
        self.Z_Gyro = QtWidgets.QCheckBox(self.widget)
        self.Z_Gyro.setObjectName("Z_Gyro")
        self.gridLayout.addWidget(self.Z_Gyro, 2, 0, 1, 1)
        self.X_Accel = QtWidgets.QCheckBox(self.widget)
        self.X_Accel.setObjectName("X_Accel")
        self.gridLayout.addWidget(self.X_Accel, 3, 0, 1, 1)
        self.Y_Accel = QtWidgets.QCheckBox(self.widget)
        self.Y_Accel.setObjectName("Y_Accel")
        self.gridLayout.addWidget(self.Y_Accel, 4, 0, 1, 1)
        self.Z_Accel = QtWidgets.QCheckBox(self.widget)
        self.Z_Accel.setObjectName("Z_Accel")
        self.gridLayout.addWidget(self.Z_Accel, 5, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Pitch = QtWidgets.QCheckBox(self.widget)
        self.Pitch.setObjectName("Pitch")
        self.gridLayout_2.addWidget(self.Pitch, 0, 0, 1, 1)
        self.Roll = QtWidgets.QCheckBox(self.widget)
        self.Roll.setObjectName("Roll")
        self.gridLayout_2.addWidget(self.Roll, 1, 0, 1, 1)
        self.Yaw = QtWidgets.QCheckBox(self.widget)
        self.Yaw.setObjectName("Yaw")
        self.gridLayout_2.addWidget(self.Yaw, 2, 0, 1, 1)
        self.Yaw_angle = QtWidgets.QCheckBox(self.widget)
        self.Yaw_angle.setObjectName("Yaw_angle")
        self.gridLayout_2.addWidget(self.Yaw_angle, 3, 0, 1, 1)
        self.Pitch_angle= QtWidgets.QCheckBox(self.widget)
        self.Pitch_angle.setObjectName("Pitch_angle")
        self.gridLayout_2.addWidget(self.Pitch_angle, 4, 0, 1, 1)
        self.Roll_angle = QtWidgets.QCheckBox(self.widget)
        self.Roll_angle.setObjectName("Roll_angle")
        self.gridLayout_2.addWidget(self.Roll_angle, 5, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Pitch_rate = QtWidgets.QCheckBox(self.widget)
        self.Pitch_rate.setObjectName("Pitch_rate")
        self.gridLayout_5.addWidget(self.Pitch_rate, 4, 0, 1, 1)
        self.Z_Mag = QtWidgets.QCheckBox(self.widget)
        self.Z_Mag.setObjectName("Z_Mag")
        self.gridLayout_5.addWidget(self.Z_Mag, 3, 0, 1, 1)
        self.Roll_rate = QtWidgets.QCheckBox(self.widget)
        self.Roll_rate.setObjectName("Roll_rate")
        self.gridLayout_5.addWidget(self.Roll_rate, 5, 0, 1, 1)
        self.Y_Mag = QtWidgets.QCheckBox(self.widget)
        self.Y_Mag.setObjectName("Y_Mag")
        self.gridLayout_5.addWidget(self.Y_Mag, 2, 0, 1, 1)
        self.Yaw_rate = QtWidgets.QCheckBox(self.widget)
        self.Yaw_rate.setObjectName("Yaw_rate")
        self.gridLayout_5.addWidget(self.Yaw_rate, 6, 0, 1, 1)
        self.X_Mag = QtWidgets.QCheckBox(self.widget)
        self.X_Mag.setObjectName("X_Mag")
        self.gridLayout_5.addWidget(self.X_Mag, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)

        self.retranslateUi(parameterSelection)
        QtCore.QMetaObject.connectSlotsByName(parameterSelection)
# ****************************    My Code_confirm selection    *****************************
#         self.Confirmation_buttonBox.accepted.connect(self.confirmed)
#         self.Confirmation_buttonBox.accepted.connect(self.accept)


        # self.buttonBox.accepted.connect(Dialog.accept)
        self.Confirmation_buttonBox.rejected.connect(parameterSelection.close)

        # self.buttonBox.accepted.connect(self.accept)


 # ****************************    My Code_confirm selection      *****************************

    def retranslateUi(self, parameterSelection):
        _translate = QtCore.QCoreApplication.translate
        parameterSelection.setWindowTitle(_translate("parameterSelection", "Parameter Selection"))
        self.X_Gyro.setText(_translate("parameterSelection", "X Gyro"))
        self.Y_Gyro.setText(_translate("parameterSelection", "Y Gyro"))
        self.Z_Gyro.setText(_translate("parameterSelection", "Z Gyro"))
        self.X_Accel.setText(_translate("parameterSelection", "X Accel"))
        self.Y_Accel.setText(_translate("parameterSelection", "Y Accel"))
        self.Z_Accel.setText(_translate("parameterSelection", "Z Accel"))
        self.Pitch.setText(_translate("parameterSelection", "Pitch"))
        self.Roll.setText(_translate("parameterSelection", "Roll"))
        self.Yaw.setText(_translate("parameterSelection", "Yaw"))
        self.Yaw_angle.setText(_translate("parameterSelection", "Yaw angle"))
        self.Pitch_angle.setText(_translate("parameterSelection", "Pitch angle"))
        self.Roll_angle.setText(_translate("parameterSelection", "Roll angle"))
        self.Pitch_rate.setText(_translate("parameterSelection", "Pitch rate"))
        self.Z_Mag.setText(_translate("parameterSelection", "Z Mag"))
        self.Roll_rate.setText(_translate("parameterSelection", "Roll rate"))
        self.Y_Mag.setText(_translate("parameterSelection", "Y Mag"))
        self.Yaw_rate.setText(_translate("parameterSelection", "Yaw rate"))
        self.X_Mag.setText(_translate("parameterSelection", "X Mag"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     parameterSelection = QtWidgets.QWidget()
#     ui = Ui_parameterSelection()
#     ui.setupUi()
#     parameterSelection.show()
#     sys.exit(app.exec_())

