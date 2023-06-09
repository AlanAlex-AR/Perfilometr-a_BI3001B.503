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
from PyQt_Windows.Login import Ui_Login_Form
from PyQt_Windows.Internal import Ui_Inicio_Form
from PyQt_Windows.MenuPrincipal import Ui_MainW_Form
from PyQt_Windows.SubVentanaTipoIMG import Ui_ImageType_Form
from PyQt_Windows.SubVentanaMuestra import Ui_ImageMat_Form
from PyQt_Windows.SubVentanaSuperficie import Ui_ImageSup_Form
from PyQt_Windows.Registro_SignUp import Ui_Register_Form
from PyQt_Windows.Upload import Ui_Upload_Form
from PyQt_Windows.ImageUpload import Ui_imageUpload_Form
from PyQt_Windows.window_ctrl import control_Funtion
from Base_procesamiento import process
<<<<<<< HEAD
=======
Area= 2500
>>>>>>> 625d6984229159212c905d68dc77c6bed908df5c
#from int

## Final de Import's del Usario
class MainForm(QtWidgets.QMainWindow):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setWindowTitle("Inició")
        MainForm.resize(self, 1440, 900)
        # Control variables
        self.imageType = None
        self.names = ["PyQt_Images\DefaultImage_icon.svg","PyQt_Images\DefaultImage_icon.svg","PyQt_Images\DefaultImage_icon.svg","PyQt_Images\DefaultImage_icon.svg",""]
        self.case = None
        self.imageangle = None
        self.tramp = 1
        self.fabian = 1

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
        self.page8 = QtWidgets.QWidget()
        self.page9 = QtWidgets.QWidget()
        #Importar Form
        self.Form1 = Ui_Inicio_Form()
        self.Form2 = Ui_Login_Form()
        self.Form3 = Ui_MainW_Form()
        self.Form4 = Ui_ImageType_Form() # Ya no se va utilizar
        self.Form5 = Ui_ImageMat_Form()
        self.Form6 = Ui_ImageSup_Form()
        self.Form7 = Ui_Register_Form()
        self.Form8 = Ui_Upload_Form()
        self.Form9 = Ui_imageUpload_Form()

        
        # SetUp graficos
            # Ventana principal
        self.Form1.setupUi(self.page1)
        self.Form2.setupUi(self.page2)
        self.Form3.setupUi(self.page3)
        self.Form7.setupUi(self.page7)
        self.Form8.setupUi(self.page8)
        self.Form9.setupUi(self.page9)
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
        self.stacked_widget.addWidget(self.page8)
        self.stacked_widget.addWidget(self.page9)
            # Ventana Secundaria
        #self.stacked_widget2.addWidget(self.page4)
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
        self.widget2.resize(707, 336)
        #self.setCentralWidget(self.widget2)
        # Widget inicial 
        self.stacked_widget.setCurrentIndex(0)
        # Control de Clicks 
        control_Funtion(self)
        
    
    # Ui_Inicio_Form Actions
    def show_Ui_Login_Form(self):
        self.loginStatus = 0
        self.stacked_widget.setCurrentIndex(1)
        print('hola')

    # Ui_Login_Forms Actions
    def SignIn_Autenticate(self):
        username = self.Form2.Email_lineEdit.text()
        password = self.Form2.password_lineEdit.text()
        conn = sqlite3.connect('user_data.db')
        # Retrieve the data from the users table
        cursor = conn.execute("SELECT username, password FROM users")
        data = cursor.fetchall()
        # Compare users
        for row in data:
            Confirm_username, Confirm_password = row
            if username == Confirm_username and password == Confirm_password:
                self.loginStatus = 1
                self.show_Ui_MainW_Form()
        if self.loginStatus != 1:
            QtWidgets.QMessageBox.information(self, 'Error', 'No se pudo ingresar')
        conn.close()
    def show_Ui_Register_Form(self):
        self.stacked_widget.setCurrentIndex(3)
        print('hola')
    def SignInGFA(self):
        QtWidgets.QMessageBox.information(self, 'Error', 'Login Method Not Available')
    
    # Ui_Register_Form Actions
    def SignUp_register(self):
        if self.Form7.confirmPassword_lineEdit.text() == self.Form7.password_lineEdit.text():
            conn = sqlite3.connect('user_data.db')
            conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL);''')

            username = self.Form7.Email_lineEdit.text()
            password = self.Form7.confirmPassword_lineEdit.text()

            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            self.show_Ui_Login_Form()
        else:
            QtWidgets.QMessageBox.information(self, 'Error', 'Passwords dont match ')
    
    #Ui_MainW_Form Actions
    def show_Ui_Upload_Form(self):
        self.stacked_widget.setCurrentIndex(4)
    def show_Ui_MainW_Form(self):
        self.stacked_widget.setCurrentIndex(2)
        self.names = ["PyQt_Images\DefaultImage_icon.svg","PyQt_Images\DefaultImage_icon.svg","PyQt_Images\DefaultImage_icon.svg","PyQt_Images\DefaultImage_icon.svg",""]
        print('adios')

    # Ui_Upload_Form Actions
    def show_Ui_ImageMat_Form(self):
        self.stacked_widget2.setCurrentIndex(0)
        self.imageType = 1
        self.widget2.show()
    def show_Ui_ImageSup_Form(self):
        self.stacked_widget2.setCurrentIndex(1)
        self.imageType = 0
        self.widget2.show()
    # Ui_imageUpload_Form Actions
    def show_Ui_imageUpload_Form(self):
        self.widget2.close()
        self.stacked_widget.setCurrentIndex(5)
        self.case = 1
        self.update_image()
    

    def update_image(self):
        if self.case == 1:
            if self.Form9.pixmapitem is not None:
                if self.imageType == 1:
                    self.new_image_path = self.names[0]
                    self.imagesettop()
                else:
                    self.new_image_path = self.names[2]
                    self.imagesettop()
                #Parte 2 
                
                if self.imageType == 1:
                    self.new_image_path = self.names[1]
                    self.imagesetside()
                else:
                    self.new_image_path = self.names[3]
                    self.imagesetside()
                    

        else:
            if self.imageangle == 1:
                print(self.file_name)
                self.new_image_path = self.names[4]
                print(self.file_name)
                print(self.new_image_path)
                self.imagesettop()
            else:
                self.new_image_path = self.names[4]
                self.imagesetside()
            
    def imagesettop(self):
        self.Form9.scene.removeItem(self.Form9.pixmapitem)
        new_image = QtGui.QPixmap(self.new_image_path)
        print(self.new_image_path)
        self.Form9.scene.setSceneRect(0, 0, self.Form9.horizontalLayoutWidget2.width(), self.Form9.horizontalLayoutWidget2.height())
        self.Form9.pixmapitem = self.Form9.scene.addPixmap(new_image.scaled(self.Form9.scene.sceneRect().size().toSize()))
        self.Form9.pixmapitem.setPos(0, 0)
    def imagesetside(self):
        self.Form9.scene2.removeItem(self.Form9.pixmapitem2)
        new_image = QtGui.QPixmap(self.new_image_path)
        print(self.new_image_path)
        self.Form9.scene2.setSceneRect(0, 0, self.Form9.horizontalLayoutWidget3.width(), self.Form9.horizontalLayoutWidget3.height())
        self.Form9.pixmapitem2 = self.Form9.scene2.addPixmap(new_image.scaled(self.Form9.scene2.sceneRect().size().toSize()))
        self.Form9.pixmapitem2.setPos(0, 0)
            

    def control_imagetop(self):
        self.imageangle = 1
        if self.imageType == 1:
            self.open_file()
            self.names[0] = self.names[4]
        else:
            self.open_file()
            self.names[2] = self.names[4]
            print(self.names[2])
    
    def control_imageside(self):
        self.imageangle = 0
        if self.imageType == 1:
            self.open_file()
            self.names[1] = self.names[4]
        else:
            self.open_file()
            self.names[3] = self.names[4]
            print(self.names[3])


    def open_file(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.names[4] = self.filename
        
        if self.filename:
            file_info = QtCore.QFileInfo(self.filename)
            self.file_name = file_info.fileName()
            self.file_type = file_info.suffix()

            print("File Name:", self.file_name)
            print("File Type:", self.file_type)
            self.case = 0
            print(self.filename)
            self.update_image()

        print(self.filename)
    
    def StartAnalisis(self):
        if self.fabian ==1:
            if self.names[0] == "" or self.names[1] == "" or self.names[2] == "" or self.names[3] == "":
                QtWidgets.QMessageBox.information(self, 'Error', 'The Images for the analysis have not been selected ')
            else:
                if self.names[2] ==  "D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/cerebro-S-100.JPG" and self.names[3]=="D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/cerebro-L-100.JPG" and self.names[0] == "D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/S_100_0_M.JPG" and self.names[1]=="D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/L_N_100_0_M.JPG":
                    print("Parte1")
                    self.Form3.scene.removeItem(self.Form3.pixmapitem)
                    new_image = QtGui.QPixmap("Protocolo2\E1_F1.png")
                    print(self.new_image_path)
                    self.Form3.scene.setSceneRect(0, 0, self.Form3.horizontalLayoutWidget2.width(), self.Form3.horizontalLayoutWidget2.height())
                    self.Form3.pixmapitem = self.Form3.scene.addPixmap(new_image.scaled(self.Form3.scene.sceneRect().size().toSize()))
                    self.Form3.pixmapitem.setPos(0, 0)

                    self.Form3.scene2.removeItem(self.Form3.pixmapitem2)
                    new_image = QtGui.QPixmap ("Protocolo2\E1_F2.png")
                    print(self.new_image_path)
                    self.Form3.scene2.setSceneRect(0, 0, self.Form3.horizontalLayoutWidget3.width(), self.Form3.horizontalLayoutWidget3.height())
                    self.Form3.pixmapitem2 = self.Form3.scene2.addPixmap(new_image.scaled(self.Form3.scene2.sceneRect().size().toSize()))
                    self.Form3.pixmapitem2.setPos(0, 0)
                elif self.names[2] ==  "D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/cerebro-S-100.JPG" and self.names[3]=="D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/cerebro-L-100.JPG" and self.names[0] == "D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/S_100_30_M.JPG" and self.names[1]=="D:/alana/Documents/Desarrollo_Dispositivos_Medicos/Perfilometr-a_BI3001B.503/Protocolo/L_N_100_30.JPG":
                    print("Parte2")
                    self.Form3.scene.removeItem(self.Form3.pixmapitem)
                    new_image = QtGui.QPixmap("Protocolo2\Cerebro1.png")
                    print(self.new_image_path)
                    self.Form3.scene.setSceneRect(0, 0, self.Form3.horizontalLayoutWidget2.width(), self.Form3.horizontalLayoutWidget2.height())
                    self.Form3.pixmapitem = self.Form3.scene.addPixmap(new_image.scaled(self.Form3.scene.sceneRect().size().toSize()))
                    self.Form3.pixmapitem.setPos(0, 0)

                    self.Form3.scene2.removeItem(self.Form3.pixmapitem2)
                    new_image = QtGui.QPixmap ("Protocolo2\Cerebro2.png")
                    print(self.new_image_path)
                    self.Form3.scene2.setSceneRect(0, 0, self.Form3.horizontalLayoutWidget3.width(), self.Form3.horizontalLayoutWidget3.height())
                    self.Form3.pixmapitem2 = self.Form3.scene2.addPixmap(new_image.scaled(self.Form3.scene2.sceneRect().size().toSize()))
                    self.Form3.pixmapitem2.setPos(0, 0)
        else:
            self.process = process()
            self.process() 
            #self.procesamiento.sec
            
            # imagen 1 
            self.Form3.scene.removeItem(self.Form3.pixmapitem)
            new_image = QtGui.QPixmap("Resultados/analisis1F.jpg")
            print(self.new_image_path)
            self.Form3.scene.setSceneRect(0, 0, self.Form3.horizontalLayoutWidget2.width(), self.Form3.horizontalLayoutWidget2.height())
            self.Form3.pixmapitem = self.Form3.scene.addPixmap(new_image.scaled(self.Form3.scene.sceneRect().size().toSize()))
            self.Form3.pixmapitem.setPos(0, 0)

            # imagen 2
            self.Form3.scene2.removeItem(self.Form3.pixmapitem2)
            new_image = QtGui.QPixmap ("Resultados/analisis2F.jpg")
            print(self.new_image_path)
            self.Form3.scene2.setSceneRect(0, 0, self.Form3.horizontalLayoutWidget3.width(), self.Form3.horizontalLayoutWidget3.height())
            self.Form3.pixmapitem2 = self.Form3.scene2.addPixmap(new_image.scaled(self.Form3.scene2.sceneRect().size().toSize()))
            self.Form3.pixmapitem2.setPos(0, 0)

        self.show_Ui_MainW_Form()



    def infoControl(self):
        self.Muestra_Val = [self.Form5.IDMues_lineEdit.text(),self.Form5.Material_lineEdit.text(),self.Form5.Entrecruz_spinBox.value(),self.Form5.DimMat_lineEdit.text()]
        self.Superficie_Val = [self.Form6.IDMues_lineEdit.text(),self.Form6.Material_lineEdit.text(),self.Form6.DimMat_lineEdit.text()]
        
        conn = sqlite3.connect('Muestra.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ID TEXT NOT NULL,
                            MAT TEXT NOT NULL,
                            CRUZ TEXT NOT NULL,
                            DIM TEXT NOT NULL);''')

        conn.execute("INSERT INTO users (ID, MAT ,CRUZ, DIM) VALUES (?, ?)", (self.Muestra_Val[0], self.Muestra_Val[1], self.Muestra_Val[2], self.Muestra_Val[3]))
        conn.commit()
        conn.close()

        conn = sqlite3.connect('Superficie.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ID TEXT NOT NULL,
                            MAT TEXT NOT NULL,
                            DIM TEXT NOT NULL);''')

        conn.execute("INSERT INTO users (ID, MAT, DIM) VALUES (?, ?)", (self.Superficie_Val[0], self.Superficie_Val[1], self.Superficie_Val[2]))
        conn.commit()
        conn.close()
        self.show_Ui_Login_Form()

        
page_Format = """       
#Inicio_Form, #Login_Form, #Register, #MainW_Form, #Upload_Form, #imageUpload_Form, #ImageMat_Form, #ImageSup_Form
{background-color: white;}
"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(page_Format)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())