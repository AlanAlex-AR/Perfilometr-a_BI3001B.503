### Procedimiento para crear un Widget template 
# Autor: Alan 

### Descripcion 
    # El programa debe desplegar template de un widget en blanco 
    # de una ventana sin contenido, el objetivo de agregar codigo 
    # al gusto del usario. 

# Componentes requeridos 
#Inicio del programa 
# Importar librerias de sys 
# Importar liberiras de PyQt5 
# Definir Clase widget 
# Configuracion y ejecucion de la app


from PyQt5 import QtCore, QtGui, QtWidgets
from Stylesheet_format import Stylesheet

class Ui_imageUpload_Form(object):
    def setupUi(self, imageUpload_Form):
        imageUpload_Form.setObjectName("imageUpload_Form")
        imageUpload_Form.resize(1440, 900)

        self.BiotextureX_Label = QtWidgets.QLabel(imageUpload_Form)
        self.BiotextureX_Label.setGeometry(QtCore.QRect(121, 24, 298, 68))
        self.BiotextureX_Label.setObjectName("BiotextureX_Label")
        self.BiotextureX_Label.setStyleSheet(Stylesheet)

        self.typeImage_label = QtWidgets.QLabel(imageUpload_Form)
        self.typeImage_label.setGeometry(QtCore.QRect(372, 126, 695, 69))
        self.typeImage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.typeImage_label.setObjectName("typeImage_label")
        self.typeImage_label.setStyleSheet(Stylesheet)

        self.topView_label = QtWidgets.QLabel(imageUpload_Form)
        self.topView_label.setGeometry(QtCore.QRect(232, 234, 280, 26))
        self.topView_label.setAlignment(QtCore.Qt.AlignCenter)
        self.topView_label.setObjectName("topView_label")
        self.topView_label.setStyleSheet(Stylesheet)

        self.sideView_label = QtWidgets.QLabel(imageUpload_Form)
        self.sideView_label.setGeometry(QtCore.QRect(926, 234, 280, 26))
        self.sideView_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sideView_label.setObjectName("sideView_label")
        self.sideView_label.setStyleSheet(Stylesheet)

        self.topUploadImage_pushButton = QtWidgets.QPushButton(imageUpload_Form)
        self.topUploadImage_pushButton.setGeometry(QtCore.QRect(181,321, 389,102))
        self.topUploadImage_pushButton.setObjectName("topUploadImage_pushButton")
        self.topUploadImage_pushButton.setStyleSheet(Stylesheet)

        self.sideUploadImage_pushButton = QtWidgets.QPushButton(imageUpload_Form)
        self.sideUploadImage_pushButton.setGeometry(QtCore.QRect(872,321, 389,102))
        self.sideUploadImage_pushButton.setObjectName("sideUploadImage_pushButton")
        self.sideUploadImage_pushButton.setStyleSheet(Stylesheet)

        self.UpLoad_pushButton = QtWidgets.QPushButton(imageUpload_Form,icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/Upload_icon2.svg")))
        self.UpLoad_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.UpLoad_pushButton.setGeometry(QtCore.QRect(106, 798, 213, 89))
        self.UpLoad_pushButton.setObjectName("UpLoad_pushButton")
        self.UpLoad_pushButton.setStyleSheet(Stylesheet)

        self.Home_pushButton = QtWidgets.QPushButton(imageUpload_Form, icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/House_icon.svg")))
        self.Home_pushButton.setIconSize(QtCore.QSize(66, 66))
        self.Home_pushButton.setGeometry(QtCore.QRect(601, 798, 213, 89))
        self.Home_pushButton.setObjectName("Home_pushButton")
        self.Home_pushButton.setStyleSheet(Stylesheet)

        self.User_pushButton = QtWidgets.QPushButton(imageUpload_Form,icon = QtGui.QIcon(QtGui.QPixmap("PyQt_Images/User_icon.svg")))
        self.User_pushButton.setIconSize(QtCore.QSize(66, 66))
        self.User_pushButton.setGeometry(QtCore.QRect(1121, 798, 213, 89))
        self.User_pushButton.setObjectName("User_pushButton")
        self.User_pushButton.setStyleSheet(Stylesheet)

        self.line = QtWidgets.QFrame(imageUpload_Form)
        self.line.setGeometry(QtCore.QRect(0, 792, 1440, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        #Primera imagen                             
        self.horizontalLayoutWidget2 = QtWidgets.QWidget(imageUpload_Form)
        self.horizontalLayoutWidget2.setGeometry(QtCore.QRect(213,468, 330,250))
        self.horizontalLayoutWidget2.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget2)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setObjectName("horizontalLayout")
        self.scene = QtWidgets.QGraphicsScene(0, 0, 660, 560)
        
        self.BioTextureX_ImagePath = "PyQt_Images\DefaultImage_icon.svg"
        self.BioTextureX_Image = QtGui.QPixmap(self.BioTextureX_ImagePath)
        self.scene.setSceneRect(0, 0, self.horizontalLayoutWidget2.width(), self.horizontalLayoutWidget2.height())
        self.pixmapitem = self.scene.addPixmap(self.BioTextureX_Image.scaled(self.scene.sceneRect().size().toSize()))
        self.pixmapitem.setPos(0,0)
        
        view = QtWidgets.QGraphicsView(self.scene)
        view.setRenderHint(QtGui.QPainter.Antialiasing)
        view.setStyleSheet("border: none;")
        
        self.horizontalLayout2.addWidget(view)
        ## Segunda imagen
        self.horizontalLayoutWidget3 = QtWidgets.QWidget(imageUpload_Form)
        self.horizontalLayoutWidget3.setGeometry(QtCore.QRect(902,468, 330,250))
        self.horizontalLayoutWidget3.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget3)
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout3.setObjectName("horizontalLayout")
        self.scene2 = QtWidgets.QGraphicsScene(0, 0, 660, 560)
        
        self.BioTextureX_ImagePath2 = "PyQt_Images\DefaultImage_icon.svg"
        self.BioTextureX_Image2 = QtGui.QPixmap(self.BioTextureX_ImagePath2)
        self.scene2.setSceneRect(0, 0, self.horizontalLayoutWidget3.width(), self.horizontalLayoutWidget3.height())
        self.pixmapitem2 = self.scene2.addPixmap(self.BioTextureX_Image2.scaled(self.scene2.sceneRect().size().toSize()))
        self.pixmapitem2.setPos(0,0)
        
        view2 = QtWidgets.QGraphicsView(self.scene2)
        view2.setRenderHint(QtGui.QPainter.Antialiasing)
        view2.setStyleSheet("border: none;")
        
        self.horizontalLayout3.addWidget(view2)

        self.Continue_pushButton = QtWidgets.QPushButton(imageUpload_Form)
        self.Continue_pushButton.setGeometry(QtCore.QRect(1227,726,127,58))
        self.Continue_pushButton.setObjectName("SignIn_pushButton")
        self.Continue_pushButton.setStyleSheet(Stylesheet)

        self.retranslateUi(imageUpload_Form)
        QtCore.QMetaObject.connectSlotsByName(imageUpload_Form)

    def retranslateUi(self, imageUpload_Form):
        _translate = QtCore.QCoreApplication.translate
        imageUpload_Form.setWindowTitle(_translate("imageUpload_Form", "Form"))
        self.BiotextureX_Label.setText(_translate("imageUpload_Form", "BioTextureX"))
        self.typeImage_label.setText(_translate("imageUpload_Form", "Import each type of image"))
        self.topView_label.setText(_translate("imageUpload_Form", "Top View"))
        self.sideView_label.setText(_translate("imageUpload_Form", "Side View"))
        self.topUploadImage_pushButton.setText(_translate("imageUpload_Form", "Upload Image"))
        self.sideUploadImage_pushButton.setText(_translate("imageUpload_Form", "Upload Image"))
        self.UpLoad_pushButton.setText(_translate("imageUpload_Form", ""))
        self.Home_pushButton.setText(_translate("imageUpload_Form", ""))
        self.User_pushButton.setText(_translate("imageUpload_Form", ""))
        self.Continue_pushButton.setText(_translate("imageUpload_Form", "Continue"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    imageUpload_Form = QtWidgets.QWidget()
    ui = Ui_imageUpload_Form()
    ui.setupUi(imageUpload_Form)
    imageUpload_Form.show()
    sys.exit(app.exec_())
