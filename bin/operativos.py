import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QByteArray, QIODevice, QBuffer
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
							 QLabel, QLineEdit)
import bin.src.recursos_rc
from bin.pdfOper import *
from sqlite3 import *
from bin.impresiones import *

class GenerarOperativo(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.resize(400, 149)
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
		self.pushButton_2 = QtWidgets.QPushButton(self)
		self.pushButton_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.pushButton_2.setAutoDefault(False)
		self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
		self.spinBox = QtWidgets.QSpinBox(self)
		self.spinBox.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.spinBox, 3, 0, 1, 1)
		self.label = QtWidgets.QLabel(self)
		self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

		QtCore.QMetaObject.connectSlotsByName(self)

		self.setWindowTitle("Sanciones para operativo")
		self.label_2.setText("<html><head/><body><p align=\"center\">Ingrese la cantidad de sanciones a emitir:</p></body></html>")
		self.pushButton_2.setText("Salir")
		self.pushButton.setText("Generar Sanciones")
		self.label.setText("<html><head/><body><p align=\"center\">Generar sanciones para operativo</p></body></html>")
		
		self.pushButton_2.clicked.connect(self.close)
		self.pushButton.clicked.connect(self.generarSanciones)
		
		
	def generarSanciones(self):
		lista = []
		self.db = connect("bin/src/secs.db")
		conector = self.db.cursor()
		for i in range(self.spinBox.value()):
			conector.execute("SELECT * FROM sanciones ORDER BY numero DESC limit 1")
			lastSancion = conector.fetchone()
			year = open("bin/src/year.bin", "rb")
			x = load(year)
			year.close()
			if not lastSancion:
				self.numeroSanc = "FTTG-TTMP-001-"+x
			else:
				if lastSancion[0] in range(9):
					self.numeroSanc = "FTTG-TTMP-00"+str(lastSancion[0]+1)+"-"+x
				else:
					if lastSancion[0] in range(9,99):
						self.numeroSanc = "FTTG-TTMP-0"+str(lastSancion[0]+1)+"-"+x
					else:
						self.numeroSanc = "FTTG-TTMP-"+str(lastSancion[0]+1)+"-"+x
			lista.append(self.numeroSanc)
			os.system("MD C:\\ecb\\Evidencias\\{}".format(self.numeroSanc))
			valoresSanciones = (self.numeroSanc, "OPERATIVO",)
			conector.execute("INSERT INTO sanciones VALUES (null, ?,?,null,null,null,null,null,null,null,null,null,null,null,null,null,null)", valoresSanciones)
			self.db.commit()
		pdf = GenerarPdfOperativo(lista)
		try:
			box = QtWidgets.QMessageBox(self)
			box.setWindowTitle('Imprimir Boletas') 
			box.setText("Se han generado las boletas para operativo.\n Presiona Si para imprimir las boleta.")
			box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
			botonSi = box.button(QtWidgets.QMessageBox.Yes)
			botonSi.setText("Si")
			box.exec_()
					
			if box.clickedButton() == botonSi:
				multa = "bin\\src\\Operativo.pdf"
				#imprimir = MkPrints(multa)
				os.startfile(multa, "print")
				self.db.close()
		except ProgrammingError:
			QMessageBox.critical(self, "Error", "No es posible conectar con la base de datos en estos mike :(.", QMessageBox.Ok)
			
