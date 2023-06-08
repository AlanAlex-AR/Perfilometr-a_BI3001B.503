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

class Ui_ImageMat_Form(object):
    def setupUi(self, ImageMat_Form):
        ImageMat_Form.setObjectName("ImageMat_Form")
        ImageMat_Form.resize(707, 336)
        

        self.IDMues_label = QtWidgets.QLabel(ImageMat_Form)
        self.IDMues_label.setGeometry(QtCore.QRect(66,26,165,40))
        self.IDMues_label.setAlignment(QtCore.Qt.AlignCenter)
        self.IDMues_label.setObjectName("IDMues_label")
        self.IDMues_label.setStyleSheet(Stylesheet)
        self.IDMues_lineEdit = QtWidgets.QLineEdit(ImageMat_Form)
        self.IDMues_lineEdit.setGeometry(QtCore.QRect(277,26,405,40))
        self.IDMues_lineEdit.setObjectName("IDMues_lineEdit")
        self.IDMues_lineEdit.setStyleSheet(Stylesheet)
        
        
        self.MaterialMues_label = QtWidgets.QLabel(ImageMat_Form)
        self.MaterialMues_label.setGeometry(QtCore.QRect(66,86,165,40))
        self.MaterialMues_label.setObjectName("MaterialMues_label")
        self.MaterialMues_label.setAlignment(QtCore.Qt.AlignCenter)
        self.MaterialMues_label.setStyleSheet(Stylesheet)
        self.Material_lineEdit = QtWidgets.QLineEdit(ImageMat_Form)
        self.Material_lineEdit.setGeometry(QtCore.QRect(277,86,405,40))
        self.Material_lineEdit.setObjectName("Material_lineEdit")
        self.Material_lineEdit.setStyleSheet(Stylesheet)

        self.Entrecruz_label = QtWidgets.QLabel(ImageMat_Form)
        self.Entrecruz_label.setGeometry(QtCore.QRect(66,149,165,40))
        self.Entrecruz_label.setObjectName("Entrecruz_label")
        self.Entrecruz_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Entrecruz_label.setStyleSheet(Stylesheet)
        self.Entrecruz_spinBox = QtWidgets.QSpinBox(ImageMat_Form)
        self.Entrecruz_spinBox.setGeometry(QtCore.QRect(277,149,165,40))
        self.Entrecruz_spinBox.setObjectName("Entrecruz_spinBox")
        self.Entrecruz_spinBox.setStyleSheet(Stylesheet)


        self.DimMat_label = QtWidgets.QLabel(ImageMat_Form)
        self.DimMat_label.setGeometry(QtCore.QRect(66,209,165,40))
        self.DimMat_label.setObjectName("DimMat_label")
        self.DimMat_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DimMat_label.setStyleSheet(Stylesheet)
        self.DimMat_lineEdit = QtWidgets.QLineEdit(ImageMat_Form)
        self.DimMat_lineEdit.setGeometry(QtCore.QRect(277,209,405,40))
        self.DimMat_lineEdit.setObjectName("DimMat_lineEdit")
        self.DimMat_lineEdit.setStyleSheet(Stylesheet)
        
        
        self.upload_pushButton = QtWidgets.QPushButton(ImageMat_Form)
        self.upload_pushButton.setGeometry(QtCore.QRect(25,273,257,35))
        self.upload_pushButton.setObjectName("upload_pushButton")
        self.upload_pushButton.setStyleSheet(Stylesheet)

        self.exit_pushButton = QtWidgets.QPushButton(ImageMat_Form)
        self.exit_pushButton.setGeometry(QtCore.QRect(425,273,257,35))
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.exit_pushButton.setStyleSheet(Stylesheet)

        self.retranslateUi(ImageMat_Form)
        QtCore.QMetaObject.connectSlotsByName(ImageMat_Form)

    def retranslateUi(self, ImageMat_Form):
        _translate = QtCore.QCoreApplication.translate
        ImageMat_Form.setWindowTitle(_translate("ImageMat_Form", "Form"))
        self.IDMues_label.setText(_translate("ImageMat_Form", "ID:"))
        self.MaterialMues_label.setText(_translate("ImageMat_Form", "Material:"))
        self.Entrecruz_label.setText(_translate("ImageMat_Form", "Cross-linking:"))
        self.DimMat_label.setText(_translate("ImageMat_Form", "Dimentions:"))
        
        self.upload_pushButton.setText(_translate("ImageMat_Form", "Upload"))
        self.exit_pushButton.setText(_translate("ImageMat_Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageMat_Form = QtWidgets.QWidget()
    ui = Ui_ImageMat_Form()
    ui.setupUi(ImageMat_Form)
    ImageMat_Form.show()
    sys.exit(app.exec_())
