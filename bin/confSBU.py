import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel, QMessageBox
import bin.src.recursos_rc
from sqlite3 import *
from pickle import *

class ConfigSBU(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.resize(298, 178)
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.label = QtWidgets.QLabel(self)
		self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
		self.lineEdit = QtWidgets.QLineEdit(self)
		self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

		QtCore.QMetaObject.connectSlotsByName(self)

		self.setWindowTitle("Configurar SBU")
		self.label.setText("Ingrese el nuevo Salario Básico Unificado (SBU):")
		self.label_2.setText("<html><head/><body><p align=\"center\">Todas las sanciones saldrán </p><p align=\"center\">con el nuevo valor ingresado.</p></body></html>")
		self.pushButton.setText("Guardar")
		
		self.pushButton.clicked.connect(self.generar)
		
	def generar(self):		
		x = open("bin/src/sbu.bin", "wb")
		box = QMessageBox(self)
		box.setWindowTitle('Cambiar el SBU') 
		box.setText("¿Acepta guardar los cambios y generar los nuevos valores de las sanciones?")
		box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		botonSi = box.button(QMessageBox.Yes)
		botonSi.setText("Si")
		box.exec_()
		if box.clickedButton() == botonSi:
			dump(self.lineEdit.text(), x)
			self.lineEdit.clear()
			x.close()