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

class Ui_MainW_Form(object):
    def setupUi(self, MainW_Form):
        MainW_Form.setObjectName("MainW_Form")
        MainW_Form.resize(1440, 900)

        # variables de control
        fabian = 1
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
        
        self.table = QtWidgets.QTableWidget(MainW_Form) 
        self.table.setRowCount(5)
        self.table.setColumnCount(2)
        self.table.setGeometry(QtCore.QRect(493, 528, 455, 190))
        self.table.setObjectName("return_pushButton")
        #self.horizontalLayout.addWidget(self.table)
        self.table.setStyleSheet(Stylesheet)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Disable editing
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # Enable selecting a single cell
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Enable selecting entire rows
        if fabian == 1:
            self.horizontalLayoutWidget2 = QtWidgets.QWidget(MainW_Form)
            self.horizontalLayoutWidget2.setGeometry(QtCore.QRect(314,167,330,250))
            self.horizontalLayoutWidget2.setObjectName("horizontalLayoutWidget")
            self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget2)
            self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout2.setObjectName("horizontalLayout")
            self.scene = QtWidgets.QGraphicsScene(0, 0, 660, 560)
            
            self.BioTextureX_ImagePath = ""
            self.BioTextureX_Image = QtGui.QPixmap(self.BioTextureX_ImagePath)
            self.scene.setSceneRect(0, 0, self.horizontalLayoutWidget2.width(), self.horizontalLayoutWidget2.height())
            self.pixmapitem = self.scene.addPixmap(self.BioTextureX_Image.scaled(self.scene.sceneRect().size().toSize()))
            self.pixmapitem.setPos(0,0)
            
            view = QtWidgets.QGraphicsView(self.scene)
            view.setRenderHint(QtGui.QPainter.Antialiasing)
            view.setStyleSheet("border: none;")
            
            self.horizontalLayout2.addWidget(view)
            ## Segunda imagen
            self.horizontalLayoutWidget3 = QtWidgets.QWidget(MainW_Form)
            self.horizontalLayoutWidget3.setGeometry(QtCore.QRect(775,167, 330,250))
            self.horizontalLayoutWidget3.setObjectName("horizontalLayoutWidget")
            self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget3)
            self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout3.setObjectName("horizontalLayout")
            self.scene2 = QtWidgets.QGraphicsScene(0, 0, 660, 560)
            
            self.BioTextureX_ImagePath2 = ""
            self.BioTextureX_Image2 = QtGui.QPixmap(self.BioTextureX_ImagePath2)
            self.scene2.setSceneRect(0, 0, self.horizontalLayoutWidget3.width(), self.horizontalLayoutWidget3.height())
            self.pixmapitem2 = self.scene2.addPixmap(self.BioTextureX_Image2.scaled(self.scene2.sceneRect().size().toSize()))
            self.pixmapitem2.setPos(0,0)
            
            view2 = QtWidgets.QGraphicsView(self.scene2)
            view2.setRenderHint(QtGui.QPainter.Antialiasing)
            view2.setStyleSheet("border: none;")
        
        self.horizontalLayout3.addWidget(view2)
        

        # Adjust table size to contents

        self.table.horizontalHeader().resizeSection(0, 210)
        self.table.horizontalHeader().resizeSection(1, 210)


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
