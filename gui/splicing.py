# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splicing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Splicing_mode_Dialog(object):
    def setupUi(self, Splicing_mode_Dialog):
        Splicing_mode_Dialog.setObjectName("Splicing_mode_Dialog")
        Splicing_mode_Dialog.resize(292, 94)
        self.buttonBox = QtWidgets.QDialogButtonBox(Splicing_mode_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.radioButton = QtWidgets.QRadioButton(Splicing_mode_Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Splicing_mode_Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 151, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Splicing_mode_Dialog)
        self.buttonBox.accepted.connect(Splicing_mode_Dialog.accept)
        self.buttonBox.rejected.connect(Splicing_mode_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Splicing_mode_Dialog)

    def retranslateUi(self, Splicing_mode_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Splicing_mode_Dialog.setWindowTitle(_translate("Splicing_mode_Dialog", "Splicing Mode Selection"))
        self.radioButton.setText(_translate("Splicing_mode_Dialog", "Manual Splicing"))
        self.radioButton_2.setText(_translate("Splicing_mode_Dialog", "Automatic Splicing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Splicing_mode_Dialog = QtWidgets.QDialog()
    ui = Ui_Splicing_mode_Dialog()
    ui.setupUi(Splicing_mode_Dialog)
    Splicing_mode_Dialog.show()
    sys.exit(app.exec_())

