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
#from int
## Final de Import's del Usario
class MainWindow(QtWidgets.QWidget):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        
        """
        ##venta 1
        self.ui = Ui_Inicio_Form()
        self.ui.setupUi(self)
        """
        """
        ##Ventanas 2
        self.ui = Ui_Login_Form()
        self.ui.setupUi(self)
        """
        """
        ##Venta 3
        self.ui = Ui_Interal_Form()
        self.ui.setupUi(self)
        """
        #self.ui = Ui_ImageType_Form()
        #self.ui.setupUi(self)

        self.ui = Ui_ImageMat_Form()
        self.ui.setupUi(self)

        ## Inicio de Codigo de Usario 
        
        ## Final de Codigo de Usario 
    ## Inicio de Callbacks de Usario 

    ## Final de Callbacks de Usario 


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())