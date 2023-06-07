# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Stylesheet_format import Stylesheet

class Ui_Upload_Form(object):
    def setupUi(self, Upload_Form):
        Upload_Form.setObjectName("Upload_Form")
        Upload_Form.resize(1440, 900)

        self.BiotextureX_Label = QtWidgets.QLabel(Upload_Form)
        self.BiotextureX_Label.setGeometry(QtCore.QRect(121, 24, 298, 68))
        self.BiotextureX_Label.setObjectName("BiotextureX_Label")
        self.BiotextureX_Label.setStyleSheet(Stylesheet)

        self.selectImage_label = QtWidgets.QLabel(Upload_Form)
        self.selectImage_label.setGeometry(QtCore.QRect(446, 168, 513, 69))
        self.selectImage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selectImage_label.setObjectName("selectImage_label")
        self.selectImage_label.setStyleSheet(Stylesheet)

        self.sampleImage_pushButton = QtWidgets.QPushButton(Upload_Form)
        self.sampleImage_pushButton.setGeometry(QtCore.QRect(311,352, 793,110))
        self.sampleImage_pushButton.setObjectName("sampleImage_pushButton")
        self.sampleImage_pushButton.setStyleSheet(Stylesheet)

        self.surfaceImage_pushButton = QtWidgets.QPushButton(Upload_Form)
        self.surfaceImage_pushButton.setGeometry(QtCore.QRect(311,538, 793,110))
        self.surfaceImage_pushButton.setObjectName("surfaceImage_pushButton")
        self.surfaceImage_pushButton.setStyleSheet(Stylesheet)

        self.UpLoad_pushButton = QtWidgets.QPushButton(Upload_Form,icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/Upload_icon2.svg")))
        self.UpLoad_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.UpLoad_pushButton.setGeometry(QtCore.QRect(106, 798, 213, 89))
        self.UpLoad_pushButton.setObjectName("UpLoad_pushButton")
        self.UpLoad_pushButton.setStyleSheet(Stylesheet)

        self.Home_pushButton = QtWidgets.QPushButton(Upload_Form, icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/House_icon.svg")))
        self.Home_pushButton.setIconSize(QtCore.QSize(66, 66))
        self.Home_pushButton.setGeometry(QtCore.QRect(601, 798, 213, 89))
        self.Home_pushButton.setObjectName("Home_pushButton")
        self.Home_pushButton.setStyleSheet(Stylesheet)

        self.User_pushButton = QtWidgets.QPushButton(Upload_Form,icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/User_icon.svg")))
        self.User_pushButton.setIconSize(QtCore.QSize(66, 66))
        self.User_pushButton.setGeometry(QtCore.QRect(1121, 798, 213, 89))
        self.User_pushButton.setObjectName("User_pushButton")
        self.User_pushButton.setStyleSheet(Stylesheet)

        self.line = QtWidgets.QFrame(Upload_Form)
        self.line.setGeometry(QtCore.QRect(0, 792, 1440, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.Analisis_pushButton = QtWidgets.QPushButton(Upload_Form)
        self.Analisis_pushButton.setGeometry(QtCore.QRect(1227,726,127,58))
        self.Analisis_pushButton.setObjectName("SignIn_pushButton")
        self.Analisis_pushButton.setStyleSheet(Stylesheet)


        self.retranslateUi(Upload_Form)
        QtCore.QMetaObject.connectSlotsByName(Upload_Form)

    def retranslateUi(self, Upload_Form):
        _translate = QtCore.QCoreApplication.translate
        Upload_Form.setWindowTitle(_translate("Upload_Form", "Form"))
        self.BiotextureX_Label.setText(_translate("Upload_Form", "BioTextureX"))
        self.sampleImage_pushButton.setText(_translate("Upload_Form", "Sample Image"))
        self.surfaceImage_pushButton.setText(_translate("Upload_Form", "Surface Image"))
        self.selectImage_label.setText(_translate("Upload_Form", "Select the type of image"))
        self.UpLoad_pushButton.setText(_translate("Upload_Form", ""))
        self.Home_pushButton.setText(_translate("Upload_Form", ""))
        self.User_pushButton.setText(_translate("Upload_Form", ""))
        self.Analisis_pushButton.setText(_translate("Upload_Form", "Start Analisis"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Upload_Form = QtWidgets.QWidget()
    ui = Ui_Upload_Form()
    ui.setupUi(Upload_Form)
    Upload_Form.show()
    sys.exit(app.exec_())
