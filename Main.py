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
import sqlite3
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
from Registro_SignUp import Ui_Register_Form
#from int
## Final de Import's del Usario
class MainForm(QtWidgets.QMainWindow):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setWindowTitle("FABIAN ES PUTO")
        MainForm.resize(self, 1440, 900)
        # Creamos un QHBoxLayout
        self.stacked_widget = QtWidgets.QStackedLayout(self)
        self.stacked_widget2 = QtWidgets.QStackedLayout(self)
        # Creamos páginas para el QStackedWidget
        self.page1 = QtWidgets.QWidget()
        self.page2 = QtWidgets.QWidget()
        self.page3 = QtWidgets.QWidget()
        self.page4 = QtWidgets.QWidget()
        self.page5 = QtWidgets.QWidget()
        self.page6 = QtWidgets.QWidget()
        self.page7 = QtWidgets.QWidget()
        #Importar Form
        self.Form1 = Ui_Inicio_Form()
        self.Form2 = Ui_Login_Form()
        self.Form3 = Ui_Interal_Form()
        self.Form4 = Ui_ImageType_Form()
        self.Form5 = Ui_ImageMat_Form()
        self.Form6 = Ui_ImageSup_Form()
        self.Form7 = Ui_Register_Form()
        
        # SetUp graficos
            # Ventana principal
        self.Form1.setupUi(self.page1)
        self.Form2.setupUi(self.page2)
        self.Form3.setupUi(self.page3)
        self.Form7.setupUi(self.page7)
            # Ventana secundario 
        self.Form4.setupUi(self.page4)
        self.Form5.setupUi(self.page5)
        self.Form6.setupUi(self.page6)

        # Agregar al formato
            # Ventana Principal
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page7)
            # Ventana Secundaria
        self.stacked_widget2.addWidget(self.page4)
        self.stacked_widget2.addWidget(self.page5)
        self.stacked_widget2.addWidget(self.page6)
        
        # Ultimo configuración
            #Ventana principal 
        self.widget =QtWidgets.QWidget()
        self.widget.setLayout(self.stacked_widget)
        self.setCentralWidget(self.widget)
            #Ventana Secundario
        self.widget2 =QtWidgets.QWidget()
        self.widget2.setLayout(self.stacked_widget2)
        self.widget2.resize(400, 300)
        #self.setCentralWidget(self.widget2)
        # Widget inicial 
        self.stacked_widget.setCurrentIndex(0)
    
        # Conneciones y Acciones 
            # Interacciónes Pagina 1 Ui_Inicio_Form
        self.Form1.Start_pushButton.pressed.connect(self.show_Ui_Login_Form)
            # Interacciónes Pagina 2 Ui_Login_Form
        self.Form2.SignIn_pushButton.pressed.connect(self.autenticate)
        self.Form2.SignUp_pushButton.pressed.connect(self.show_Ui_Register_Form)
        #self.Form2.Registrar_pushButton.pressed.connect()
            # Interacciones Pagina 3 Ui_Interal_Form
        self.Form3.ImagenSup_pushButton.pressed.connect(self.show_Ui_ImageType_Form)
        self.Form3.ImagenLat_pushButton.pressed.connect(self.show_Ui_ImageType_Form)
            # Interacciones Pagina 4 Ui_ImageType_Form
        self.Form4.ImagenMues_pushButton.pressed.connect(self.show_Ui_ImageMat_Form)
        self.Form4.ImagenSuperficie_pushButton.pressed.connect(self.show_Ui_ImageSup_Form)
            # Interaccion Pagina 5 Ui_ImageMat_Form
        self.Form5.pushButton_2.pressed.connect(self.open_file)
        self.Form5.pushButton.pressed.connect(self.widget2.close)
            # Interracion pagina 6 Ui_ImageSup_Form
        self.Form6.pushButton_2.pressed.connect(self.open_file)
        self.Form6.pushButton.pressed.connect(self.widget2.close)

   
    def show_Ui_Login_Form(self):
        self.stacked_widget.setCurrentIndex(1)
        print('hola')

    def autenticate(self):
        username = self.Form2.Email_lineEdit.text()
        password = self.Form2.password_lineEdit.text()

        if username == 'equipo' and password == 'dinamita':
            self.Ui_Interal_Form()
        else:
            QtWidgets.QMessageBox.information(self, 'Error', 'No se pudo ingresar')
    def show_Ui_Register_Form(self):
        self.stacked_widget.setCurrentIndex(3)
        print('hola')
    def Ui_Interal_Form(self):
        self.stacked_widget.setCurrentIndex(2)
        print('adios')
    
    def show_Ui_ImageType_Form(self):
        self.stacked_widget2.setCurrentIndex(0)
        self.widget2.show()
    def show_Ui_ImageMat_Form(self):
        self.stacked_widget2.setCurrentIndex(1)
    def show_Ui_ImageSup_Form(self):
        self.stacked_widget2.setCurrentIndex(2)
    def open_file(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        
        print(self.filename)
    def register(self):
        conn = sqlite3.connect('user_data.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL);''')

        username = input("Enter username: ")
        password = input("Enter password: ")

        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()


page_Format = """       
#Inicio_Form {background-color: white;}
#Login_Form {background-color: white;}
#Register {background-color: white;}
"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(page_Format)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())