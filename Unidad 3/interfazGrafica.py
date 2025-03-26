import time

import serial
import keyboard
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton
from PyQt5.uic import loadUi


class interfazGrafica(QMainWindow):
    def __init__(self):
        super(interfazGrafica, self).__init__()
        loadUi("interfazBrazoRobotico.ui", self)
        self.show()

        self.arduino = serial.Serial('COM6', 9600)  # Cambia 'COM6' al puerto correcto

        keyboard.on_press_key('a', self.tecla_presionada)
        keyboard.on_press_key('s', self.tecla_presionada)
        keyboard.on_press_key('f', self.tecla_presionada)
        keyboard.on_press_key('d', self.tecla_presionada)
        keyboard.on_press_key('g', self.tecla_presionada)
        keyboard.on_press_key('h', self.tecla_presionada)
        keyboard.on_press_key('j', self.tecla_presionada)
        keyboard.on_press_key('k', self.tecla_presionada)
        keyboard.on_press_key('l', self.tecla_presionada)
        keyboard.on_press_key('p', self.tecla_presionada)
        keyboard.on_release(self.tecla_suelta)

    def tecla_presionada(self, event):
        if event.name == 'a':
            self.M1i.setChecked(True)
            self.arduino.write(b'a')
        elif event.name == 's':
            self.M1d.setChecked(True)
            self.arduino.write(b's')
        elif event.name == 'd':
            self.M2i.setChecked(True)
            self.arduino.write(b'd')
        elif event.name == 'f':
            self.M2d.setChecked(True)
            self.arduino.write(b'f')
        elif event.name == 'g':
            self.M3i.setChecked(True)
            self.arduino.write(b'g')
        elif event.name == 'h':
            self.M3d.setChecked(True)
            self.arduino.write(b'h')
        elif event.name == 'j':
            self.M4i.setChecked(True)
            self.arduino.write(b'j')
        elif event.name == 'k':
            self.M4d.setChecked(True)
            self.arduino.write(b'k')
        elif event.name == 'l':
            self.M5i.setChecked(True)
            self.arduino.write(b'l')
        elif event.name == 'p':
            self.M5d.setChecked(True)
            self.arduino.write(b'p')


    def tecla_suelta(self, event):
        if event.name == 'a':
            self.M1p.setChecked(True)
            self.arduino.write(b'q')
            print("Tecla 'a' soltada")
        elif event.name == 's':
            self.M1p.setChecked(True)
            self.arduino.write(b'q')
            print("Tecla 's' soltada")
        elif event.name == 'd':
            self.M2p.setChecked(True)
            self.arduino.write(b'e')
            print("Tecla 'd'soltada")
        elif event.name == 'f':
            self.M2p.setChecked(True)
            self.arduino.write(b'e')
            print("Tecla 'f' soltada")
        elif event.name == 'g':
            self.M3p.setChecked(True)
            self.arduino.write(b't')
            print("Tecla 'g'soltada")
        elif event.name == 'h':
            self.M3p.setChecked(True)
            self.arduino.write(b't')
            print("Tecla 'h' soltada")
        elif event.name == 'j':
            self.M4p.setChecked(True)
            self.arduino.write(b'u')
        elif event.name == 'k':
            self.M4p.setChecked(True)
            self.arduino.write(b'u')
        elif event.name == 'l':
            self.M5p.setChecked(True)
            self.arduino.write(b'o')
        elif event.name == 'p':
            self.M5p.setChecked(True)
            self.arduino.write(b'o')

if __name__ == "__main__":
    app = QApplication([])
    interfaz = interfazGrafica()
    app.exec_()
