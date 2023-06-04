
def control_Funtion(self):
            
        # Interacciónes Pagina 1 Ui_Inicio_Form
    self.Form1.Start_pushButton.pressed.connect(self.show_Ui_Login_Form)
         # Interacciónes Pagina 2 Ui_Login_Form
    self.Form2.SignIn_pushButton.pressed.connect(self.SignIn_Autenticate)
    self.Form2.SignUp_pushButton.pressed.connect(self.show_Ui_Register_Form)
    self.Form2.SignInGoogle_pushButton.pressed.connect(self.SignInGFA)
    self.Form2.SignInFacebook_pushButton.pressed.connect(self.SignInGFA)
    self.Form2.SignInApple_pushButton.pressed.connect(self.SignInGFA)
        # Interacciones Pagina 7 Ui_Register_Form
    self.Form7.return_pushButton.pressed.connect(self.show_Ui_Login_Form)
    self.Form7.SignUp_pushButton.pressed.connect(self.SignUp_register)
    self.Form7.signIn_pushButton.pressed.connect(self.show_Ui_Login_Form)
        # Interacciones Pagina 3 Ui_MainW_Form

        # Interacciones Pagina 4 Ui_ImageType_Form
    self.Form4.ImagenMues_pushButton.pressed.connect(self.show_Ui_ImageMat_Form)
    self.Form4.ImagenSuperficie_pushButton.pressed.connect(self.show_Ui_ImageSup_Form)
            # Interaccion Pagina 5 Ui_ImageMat_Form
    self.Form5.pushButton_2.pressed.connect(self.open_file)
    self.Form5.pushButton.pressed.connect(self.widget2.close)
        # Interracion pagina 6 Ui_ImageSup_Form
    self.Form6.pushButton_2.pressed.connect(self.open_file)
    self.Form6.pushButton.pressed.connect(self.widget2.close)


    