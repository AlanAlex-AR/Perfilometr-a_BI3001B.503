
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
    self.Form3.UpLoad_pushButton.pressed.connect(self.show_Ui_Upload_Form)
    self.Form3.Home_pushButton.pressed.connect(self.show_Ui_MainW_Form)
    #self.Form3.User_pushButton.pressed.connect()

        # Interacciones Pagina 8 Ui_Upload_Form
    self.Form8.sampleImage_pushButton.pressed.connect(self.show_Ui_ImageMat_Form)
    self.Form8.surfaceImage_pushButton.pressed.connect(self.show_Ui_ImageSup_Form)
    self.Form8.UpLoad_pushButton.pressed.connect(self.show_Ui_Upload_Form)
    self.Form8.Home_pushButton.pressed.connect(self.show_Ui_MainW_Form)
    #self.Form8.User_pushButton.pressed.connect()

        # Interacciones Pagina 5 y 6 Ui_ImageMat_Form Ui_ImageSup_Form
    self.Form5.upload_pushButton.pressed.connect(self.show_Ui_imageUpload_Form)
    self.Form6.upload_pushButton.pressed.connect(self.show_Ui_imageUpload_Form)
    self.Form5.exit_pushButton.pressed.connect(self.widget2.close)
    self.Form6.exit_pushButton.pressed.connect(self.widget2.close)
        # Interacciones Pagina 9 Ui_imageUpload_Form
    self.Form9.topUploadImage_pushButton.pressed.connect(self.open_file)
    self.Form9.sideUploadImage_pushButton.pressed.connect(self.open_file)
    self.Form9.UpLoad_pushButton.pressed.connect(self.show_Ui_Upload_Form)
    self.Form9.Home_pushButton.pressed.connect(self.show_Ui_MainW_Form)
    #self.Form9.User_pushButton.pressed.connect()
        # Interacciones Pagina 5 Ui_ImageMat_Form
    #self.Form5.upload_pushButton.pressed.connect()
 


        # Interracion pagina 6 Ui_ImageSup_Form


    