from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        MainForm.resize(self, 800, 600)
        # Create instances of the UI Forms
        self.ui_form1 = UIForm1()
        self.ui_form2 = UIForm2()

        # Create a stacked widget to display the UI Forms
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.ui_form1)
        self.stacked_widget.addWidget(self.ui_form2)

        # Create buttons to switch between the UI Forms
        self.button1 = QPushButton("UI Form 1", self)
        self.button1.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.ui_form1))
        self.button1.clicked.connect(self.pushbutton)
        self.button2 = QPushButton("UI Form 2", self)
        self.button2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.ui_form2))

        # Add the buttons and the stacked widget to a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.stacked_widget)

        # Set the central widget to the vertical layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def pushbutton(self):
        print("Template 1")


class UIForm1(QWidget):
    def __init__(self):
        super().__init__()
        #UIForm1.setObjectName("Inicio_Form")
        UIForm1.resize(self, 800, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 380, 228, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Continuar_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Continuar_pushButton.setObjectName("Continuar_pushButton")
        self.horizontalLayout.addWidget(self.Continuar_pushButton)
        self.Salir_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Salir_pushButton.setObjectName("Salir_pushButton")
        self.horizontalLayout.addWidget(self.Salir_pushButton)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #Inicio_Form.setWindowTitle(_translate("Inicio_Form", "Form"))
        self.Continuar_pushButton.setText(_translate("Inicio_Form", "Continuar"))
        self.Salir_pushButton.setText(_translate("Inicio_Form", "Salir"))
        # Define the UI Form 1 widgets and layout

class UIForm2(QWidget):
    def __init__(self):
        super().__init__()
        # Define the UI Form 2 widgets and layout

if __name__ == '__main__':
    app = QApplication([])
    main_form = MainForm()
    main_form.show()
    app.exec_()
