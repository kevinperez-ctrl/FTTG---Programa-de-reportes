import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from bin.main_windows import *
  
app = QApplication(sys.argv)
dialogo = Ventana()
dialogo.show()
app.exec_()
