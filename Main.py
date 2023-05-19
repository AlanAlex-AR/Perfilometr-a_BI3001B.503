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
class MainForm(QtWidgets.QMainWindow):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setWindowTitle("My App")
        MainForm.resize(self, 800, 600)
        # Creamos un QHBoxLayout
        self.stacked_widget = QtWidgets.QStackedLayout(self)


        # Creamos dos páginas para el QStackedWidget
        self.page1 = QtWidgets.QWidget()
        self.page2 = QtWidgets.QWidget()
        self.page3 = QtWidgets.QWidget()
        #Importar Form
        self.Form1 = Ui_Inicio_Form()
        self.Form2 = Ui_Login_Form()
        self.Form3 = Ui_Interal_Form()
        #self.Form4 = Ui
        
        # SetUp graficos
        self.Form1.setupUi(self.page1)
        self.Form2.setupUi(self.page2)
        self.Form3.setupUi(self.page3)

        # Agregar al formato
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        
        # Conneciones 
        self.Form1.Continuar_pushButton.pressed.connect(self.show_Form2)

        # Widget inicial 
        self.stacked_widget.setCurrentIndex(0)

        # Ultimo configuración
        self.widget =QtWidgets.QWidget()
        self.widget.setLayout(self.stacked_widget)
        self.setCentralWidget(self.widget)



    def show_Form2(self):
        self.stacked_widget.setCurrentIndex(1)
        print('hola')

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)
        print('adios')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())