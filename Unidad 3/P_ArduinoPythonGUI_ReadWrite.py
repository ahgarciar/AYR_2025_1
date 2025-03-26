import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

import serial as tarjeta

qtCreatorFile = "P_ArduinoPythonGUI_ReadWrite.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.arduino = None

        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.bandera = 0
        self.datos = []

        self.btn_control_led.clicked.connect(self.control)


    def control(self):
        texto = self.btn_control_led.text()
        if texto == "PRENDER":
            self.btn_control_led.setText("APAGAR")
            self.arduino.write("1".encode())
        else:
            self.btn_control_led.setText("PRENDER")
            self.arduino.write("0".encode())

    # Área de los Slots
    def lecturas(self):
        if self.arduino.isOpen():
            if self.arduino.inWaiting(): #if Serial.available()>0
                cadena = self.arduino.readline().decode().strip()
                if cadena != "":
                    self.datos.append(cadena)
                    if self.bandera == 0:
                        print(cadena)

    def accion(self):
        texto = self.btn_accion.text()
        #com = "COM" + self.txt_com.text() #windows
        com = self.txt_com.text()
        if texto == "CONECTAR":
            self.arduino = tarjeta.Serial(com, baudrate=9600, timeout= 1)
            self.segundoPlano.start(100) #ms
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
        elif texto == "DESCONECTAR":
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
        elif texto == "RECONECTAR":
            self.arduino.open()
            self.segundoPlano.start(100) #ms
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

