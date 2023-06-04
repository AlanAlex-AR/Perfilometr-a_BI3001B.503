# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Stylesheet_format import Stylesheet

class Ui_MainW_Form(object):
    def setupUi(self, MainW_Form):
        MainW_Form.setObjectName("MainW_Form")
        MainW_Form.resize(1440, 900)

        self.BiotextureX_Label = QtWidgets.QLabel(MainW_Form)
        self.BiotextureX_Label.setGeometry(QtCore.QRect(121, 24, 298, 68))
        self.BiotextureX_Label.setObjectName("BiotextureX_Label")
        self.BiotextureX_Label.setStyleSheet(Stylesheet)

        self.reconstructionAnalysis_label = QtWidgets.QLabel(MainW_Form)
        self.reconstructionAnalysis_label.setGeometry(QtCore.QRect(479, 87, 459, 48))
        self.reconstructionAnalysis_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reconstructionAnalysis_label.setObjectName("reconstructionAnalysis_label")
        self.reconstructionAnalysis_label.setStyleSheet(Stylesheet)

        self.UpLoad_pushButton = QtWidgets.QPushButton(MainW_Form,icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/Upload_icon2.svg")))
        self.UpLoad_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.UpLoad_pushButton.setGeometry(QtCore.QRect(106, 798, 213, 89))
        self.UpLoad_pushButton.setObjectName("UpLoad_pushButton")
        self.UpLoad_pushButton.setStyleSheet(Stylesheet)

        self.Home_pushButton = QtWidgets.QPushButton(MainW_Form, icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/House_icon.svg")))
        self.Home_pushButton.setIconSize(QtCore.QSize(66, 66))
        self.Home_pushButton.setGeometry(QtCore.QRect(601, 798, 213, 89))
        self.Home_pushButton.setObjectName("Home_pushButton")
        self.Home_pushButton.setStyleSheet(Stylesheet)

        self.User_pushButton = QtWidgets.QPushButton(MainW_Form,icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/User_icon.svg")))
        self.User_pushButton.setIconSize(QtCore.QSize(66, 66))
        self.User_pushButton.setGeometry(QtCore.QRect(1121, 798, 213, 89))
        self.User_pushButton.setObjectName("User_pushButton")
        self.User_pushButton.setStyleSheet(Stylesheet)

        self.line = QtWidgets.QFrame(MainW_Form)
        self.line.setGeometry(QtCore.QRect(0, 792, 1440, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(MainW_Form)
        self.line_2.setGeometry(QtCore.QRect(720, 135, 3, 337))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(MainW_Form)
        QtCore.QMetaObject.connectSlotsByName(MainW_Form)

    def retranslateUi(self, MainW_Form):
        _translate = QtCore.QCoreApplication.translate
        MainW_Form.setWindowTitle(_translate("MainW_Form", "Form"))
        self.BiotextureX_Label.setText(_translate("MainW_Form", "BioTextureX"))
        self.reconstructionAnalysis_label.setText(_translate("MainW_Form", "Reconstruction Analysis"))
        self.UpLoad_pushButton.setText(_translate("MainW_Form", ""))
        self.Home_pushButton.setText(_translate("MainW_Form", ""))
        self.User_pushButton.setText(_translate("MainW_Form", ""))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainW_Form = QtWidgets.QWidget()
    ui = Ui_MainW_Form()
    ui.setupUi(MainW_Form)
    MainW_Form.show()
    sys.exit(app.exec_())
