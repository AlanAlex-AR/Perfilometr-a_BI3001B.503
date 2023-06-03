def control_Funtion(self):
            
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