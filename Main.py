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

# Inicio de Import's basicos 
import sys
from PyQt5 import QtCore    # Qtcore    (Importa principales funciones de Qt)
from PyQt5 import QtWidgets # QtWidget  (Importa nuevos componentes Widgets)
from PyQt5 import QtGui     # QtGui     (Importa los texturas, texturas, y fuentes des escritura)

## Inicio de Import's del Usario 
from Login import Ui_Login_Form
from Internal import Ui_Inicio_Form
from MenuPrincipal import Ui_Interal_Form
from SubVentanaTipoIMG import Ui_ImageType_Form
from SubVentanaMuestra import Ui_ImageMat_Form
from SubVentanaSuperficie import Ui_ImageSup_Form
#from int
## Final de Import's del Usario
class MainWindow(QtWidgets.QWidget):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.resize(800,600)
        layout = QtWidgets.QHBoxLayout(self)

        # Creamos un QStackedWidget y lo añadimos al layout
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        layout.addWidget(self.stacked_widget)

        # Creamos dos páginas para el QStackedWidget
        self.page1 = QtWidgets.QWidget()
        self.page2 = QtWidgets.QWidget()
        #Importar ventana 
        self.ui_Inicio_Form = Ui_Inicio_Form()
        self.ui_Login_Form = Ui_Login_Form()
        #Configuracion del Layout
        #self.page1.layout = QtWidgets.QHBoxLayout(self.page1)
        #self.page1.layout.addWidget(self.ui_Inicio_Form)
        self.page1.setLayout(self.ui_Inicio_Form)

        #self.page2.layout = QtWidgets.QHBoxLayout(self.page2)
        #self.page2.layout.add(self.ui_Login_Form)
        self.page2.setLayout(self.ui_Login_Form)

        #Agregar layout
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        #Accion
        
        self.stacked_widget.addWidget(self.ui_Inicio_Form)
        self.stacked_widget.addWidget(self.ui_Login_Form)

        
    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)
        print('hola')

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)
        print('adios')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())