import sys
from os import getcwd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QByteArray, QIODevice, QBuffer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel 
import bin.src.recursos_rc
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtWidgets import (QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu, QActionGroup, QAction, QMessageBox)
from sqlite3 import *
import time
from bin.pdfgen import *
from pickle import *
import os

class Modificar(QDialog):
	def __init__(self, user):
		QDialog.__init__(self)
		self.resize(447, 557)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.user = user
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.setObjectName("gridLayout")
		self.label_2 = QtWidgets.QLabel(self)
		self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
		self.boletaEntry = QtWidgets.QLineEdit(self)
		self.gridLayout.addWidget(self.boletaEntry, 0, 2, 1, 1)
		self.buscarBoton = QtWidgets.QPushButton(self)
		self.gridLayout.addWidget(self.buscarBoton, 0, 3, 1, 1)
		self.label = QtWidgets.QLabel(self)
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.frame = QtWidgets.QFrame(self)
		self.frame.setEnabled(False)
		self.frame.setStyleSheet("border-color: rgb(255, 170, 0);")
		self.frame.setFrameShape(QtWidgets.QFrame.Box)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setLineWidth(1)
		self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
		self.litLabel = QtWidgets.QLabel(self.frame)
		self.litLabel.setObjectName("litLabel")
		self.gridLayout_2.addWidget(self.litLabel, 6, 0, 1, 1)
		self.litEntry = QtWidgets.QLineEdit(self.frame)
		self.gridLayout_2.addWidget(self.litEntry, 6, 1, 1, 4)
		self.horaEntry = QtWidgets.QLineEdit(self.frame)
		self.gridLayout_2.addWidget(self.horaEntry, 3, 1, 1, 4)
		self.horaEntry.setEnabled(False)
		self.horaCheck = QtWidgets.QCheckBox(self.frame)
		self.horaCheck.setText("")
		self.horaCheck.setObjectName("horaCheck")
		self.gridLayout_2.addWidget(self.horaCheck, 3, 6, 1, 3)
		self.artEntry = QtWidgets.QLineEdit(self.frame)
		self.gridLayout_2.addWidget(self.artEntry, 5, 1, 1, 4)
		self.artLabel = QtWidgets.QLabel(self.frame)
		self.artLabel.setObjectName("artLabel")
		self.gridLayout_2.addWidget(self.artLabel, 5, 0, 1, 1)
		self.discoLabel = QtWidgets.QLabel(self.frame)
		self.discoLabel.setObjectName("discoLabel")
		self.gridLayout_2.addWidget(self.discoLabel, 1, 0, 1, 1)
		self.fechaLabel = QtWidgets.QLabel(self.frame)
		self.fechaLabel.setObjectName("fechaLabel")
		self.gridLayout_2.addWidget(self.fechaLabel, 2, 0, 1, 1)
		self.horaLabel = QtWidgets.QLabel(self.frame)
		self.horaLabel.setObjectName("horaLabel")
		self.gridLayout_2.addWidget(self.horaLabel, 3, 0, 1, 1)
		self.discoEntry = QtWidgets.QLineEdit(self.frame)
		self.gridLayout_2.addWidget(self.discoEntry, 1, 1, 1, 4)
		self.coopLabel = QtWidgets.QLabel(self.frame)
		self.coopLabel.setObjectName("coopLabel")
		self.gridLayout_2.addWidget(self.coopLabel, 0, 0, 1, 1)
		self.coopCombo = QtWidgets.QComboBox(self.frame)
		self.gridLayout_2.addWidget(self.coopCombo, 0, 1, 1, 5)
		self.coopCombo.addItem("")
		self.coopCombo.setItemText(0, "")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.coopCombo.addItem("")
		self.fechaEntry = QtWidgets.QLineEdit(self.frame)
		self.fechaEntry.setEnabled(False)
		self.gridLayout_2.addWidget(self.fechaEntry, 2, 1, 1, 4)
		self.fechaCheck = QtWidgets.QCheckBox(self.frame)
		self.fechaCheck.setText("")
		self.fechaCheck.setObjectName("fechaCheck")
		self.gridLayout_2.addWidget(self.fechaCheck, 2, 5, 1, 3)
		self.nombreLabel = QtWidgets.QLabel(self.frame)
		self.nombreLabel.setObjectName("nombreLabel")
		self.gridLayout_2.addWidget(self.nombreLabel, 4, 0, 1, 3)
		self.pushButton = QtWidgets.QPushButton(self.frame)
		self.gridLayout_2.addWidget(self.pushButton, 11, 3, 1, 1)
		self.nombreEntry = QtWidgets.QLineEdit(self.frame)
		self.gridLayout_2.addWidget(self.nombreEntry, 4, 3, 1, 5)
		self.anularBoton = QtWidgets.QPushButton(self.frame)
		self.anularBoton.setEnabled(False)
		self.gridLayout_2.addWidget(self.anularBoton, 12, 7, 1, 2)
		self.totLabel = QtWidgets.QLabel(self.frame)
		self.totLabel.setObjectName("totLabel")
		self.gridLayout_2.addWidget(self.totLabel, 9, 0, 1, 2)
		self.desLabel = QtWidgets.QLabel(self.frame)
		self.desLabel.setObjectName("desLabel")
		self.gridLayout_2.addWidget(self.desLabel, 7, 0, 1, 1)
		self.tipLabel = QtWidgets.QLabel(self.frame)
		self.tipLabel.setObjectName("tipLabel")
		self.gridLayout_2.addWidget(self.tipLabel, 8, 0, 1, 1)
		self.guardarBoton = QtWidgets.QPushButton(self.frame)
		self.guardarBoton.setObjectName("guardarBoton")
		self.gridLayout_2.addWidget(self.guardarBoton, 12, 0, 1, 3)
		self.tipCombo = QtWidgets.QComboBox(self.frame)
		self.tipCombo.addItem("")
		self.tipCombo.setItemText(0, "")
		self.tipCombo.addItem("")
		self.tipCombo.addItem("")
		self.tipCombo.addItem("")
		self.gridLayout_2.addWidget(self.tipCombo, 8, 1, 1, 6)
		self.elabLabel = QtWidgets.QLabel(self.frame)
		self.elabLabel.setObjectName("elabLabel")
		self.gridLayout_2.addWidget(self.elabLabel, 10, 0, 1, 2)
		self.anularCheck = QtWidgets.QCheckBox(self.frame)
		self.anularCheck.setText("")
		self.anularCheck.setObjectName("anularCheck")
		self.gridLayout_2.addWidget(self.anularCheck, 12, 9, 1, 2)
		self.valorLabel = QtWidgets.QLabel(self.frame)
		self.valorLabel.setText("")
		self.valorLabel.setObjectName("valorLabel")
		self.gridLayout_2.addWidget(self.valorLabel, 9, 2, 1, 2)
		self.desEntry = QtWidgets.QTextEdit(self.frame)
		self.gridLayout_2.addWidget(self.desEntry, 7, 1, 1, 8)
		self.evidenciaLabel = QtWidgets.QLabel(self.frame)
		self.evidenciaLabel.setObjectName("evidenciaLabel")
		self.gridLayout_2.addWidget(self.evidenciaLabel, 11, 0, 1, 1)
		self.otrosButton = QtWidgets.QPushButton(self.frame)
		self.otrosButton.setText("Otros")
		self.gridLayout_2.addWidget(self.otrosButton, 11, 4, 1, 1)
		self.rutaLabel = QtWidgets.QLabel(self.frame)
		self.rutaLabel.setText("")
		self.gridLayout_2.addWidget(self.rutaLabel, 11, 7, 1, 4)
		self.elabCombo = QtWidgets.QComboBox(self.frame)
		self.elabCombo.addItem("")
		self.elabCombo.setItemText(0, "")
		self.elabCombo.addItem("")
		self.elabCombo.addItem("")
		self.elabCombo.addItem("")
		self.gridLayout_2.addWidget(self.elabCombo, 10, 3, 1, 4)
		self.gridLayout.addWidget(self.frame, 1, 0, 1, 4)

		QtCore.QMetaObject.connectSlotsByName(self)
		self.setTabOrder(self.boletaEntry, self.buscarBoton)
		self.setTabOrder(self.buscarBoton, self.coopCombo)
		self.setTabOrder(self.coopCombo, self.discoEntry)
		self.setTabOrder(self.discoEntry, self.fechaEntry)
		self.setTabOrder(self.fechaEntry, self.horaEntry)
		self.setTabOrder(self.horaEntry, self.nombreEntry)
		self.setTabOrder(self.nombreEntry, self.artEntry)
		self.setTabOrder(self.artEntry, self.litEntry)
		self.setTabOrder(self.litEntry, self.desEntry)
		self.setTabOrder(self.desEntry, self.tipCombo)
		self.setTabOrder(self.tipCombo, self.elabCombo)
		self.setTabOrder(self.elabCombo, self.guardarBoton)
		self.setTabOrder(self.guardarBoton, self.anularBoton)

		self.setWindowTitle("Modificar Sanciones")
		self.label_2.setText("FTTG-TTMP")
		self.buscarBoton.setText("Buscar")
		self.label.setText("Numero de Sanción:")
		self.litLabel.setText("Literal:")
		self.artLabel.setText("Artículo:")
		self.discoLabel.setText("Disco:")
		self.fechaLabel.setText("Fecha:")
		self.horaLabel.setText("Hora:")
		self.coopLabel.setText("Cooperativa:")
		self.nombreLabel.setText("Nombre del infractor:")
		self.pushButton.setText("Imagenes")
		self.anularBoton.setText("Anular")
		self.totLabel.setText("Total a pagar:")
		self.desLabel.setText("Descripción:")
		self.tipLabel.setText("Tipo de Falta:")
		self.guardarBoton.setText("Guardar")
		self.elabLabel.setText("Elaborado Por: ")
		self.evidenciaLabel.setText("Evidencias: ")
		self.coopCombo.setItemText(1,"7 de Noviembre")
		self.coopCombo.setItemText(2,"24 de Septiembre")
		self.coopCombo.setItemText(3,"Carlos Alberto Aray")
		self.coopCombo.setItemText(4,"Coactur")
		self.coopCombo.setItemText(5,"Costa Azul")
		self.coopCombo.setItemText(6,"FIFA")
		self.coopCombo.setItemText(7,"Jipijapa")
		self.coopCombo.setItemText(8,"Liberpesa")
		self.coopCombo.setItemText(9, "Libertad Peninsular CLP")
		self.coopCombo.setItemText(10,"Mi Piedacita")
		self.coopCombo.setItemText(11,"Pedro Carbo")
		self.coopCombo.setItemText(12,"Posorja CTP")
		self.coopCombo.setItemText(13,"Poza Honda")
		self.coopCombo.setItemText(14,"Reina del Camino")
		self.coopCombo.setItemText(15,"Rutas Balzareñas")
		self.coopCombo.setItemText(16,"Rutas Empalmeñas")
		self.coopCombo.setItemText(17,"Rutas Portovejenses")
		self.coopCombo.setItemText(18,"Rutas Vinceñas")
		self.coopCombo.setItemText(19,"Santa Lucía")
		self.coopCombo.setItemText(20,"Santa Rosa de Colimes")
		self.coopCombo.setItemText(21,"Señor de los Milagros")
		self.coopCombo.setItemText(22,"Sucre")
		self.coopCombo.setItemText(23,"TIA")
		self.coopCombo.setItemText(24,"Villamil")
		self.tipCombo.setItemText(1,"Leve 5% SBU")
		self.tipCombo.setItemText(2,"Leve 10% SBU")
		self.tipCombo.setItemText(3,"Grave 20% SBU")
		self.elabCombo.setItemText(1,"Cercado Washington")
		self.elabCombo.setItemText(2,"Tigua Alex")
		self.elabCombo.setItemText(3,"Velez Jose")
		
		self.buscarBoton.clicked.connect(self.buscar)
		self.fechaCheck.stateChanged.connect(self.verificar2)
		self.horaCheck.stateChanged.connect(self.verificar3)
		self.anularCheck.stateChanged.connect(self.verificar11)
		self.pushButton.clicked.connect(self.seleccionar_imagen)
		self.guardarBoton.clicked.connect(self.guardar_registro)
		self.tipCombo.currentIndexChanged['int'].connect(self.changeValue)
		self.anularBoton.clicked.connect(self.anular_sancion)
		self.otrosButton.clicked.connect(self.showDialog)
		
	def buscar(self):
		self.db = connect("bin/src/secs.db")
		cursor = self.db.cursor()
		self.boleta = "FTTG-TTMP-"+self.boletaEntry.text()
		tupladatos = (self.boleta,)
		cursor.execute("SELECT * FROM sanciones WHERE numeroSancion=?", tupladatos)
		datos = cursor.fetchone()
		
		if datos:
			self.frame.setEnabled(True)
			self.coopCombo.setItemText(0,datos[2])
			self.discoEntry.setText(datos[3])
			self.fechaEntry.setText(datos[4])
			self.horaEntry.setText(datos[5])
			self.artEntry.setText(datos[6])
			self.litEntry.setText(datos[7])
			self.desEntry.setText(datos[8])
			self.tipCombo.setItemText(0,datos[9])
			self.valorLabel.setText(datos[10])
			self.elabCombo.setItemText(0,datos[11])
			self.nombreEntry.setText(datos[14])
			self.rutaLabel.setText(datos[16])
		else:
			QMessageBox.question(self, "No existe sanción", "No hay alguna sanción registrada para ese número de boleta.", QMessageBox.Ok)
			self.frame.setEnabled(False)
	
	def verificar2(self):	
		if self.fechaCheck.isChecked:
			self.fechaEntry.setEnabled(True)
		else:
			self.fechaEntry.setEnabled(False)
	
	def verificar3(self):
		if self.horaCheck.isChecked:
			self.horaEntry.setEnabled(True)
		else:
			self.horaEntry.setEnabled(False)
			
	def verificar11(self):
		if self.anularCheck.isChecked:
			self.anularBoton.setEnabled(True)
		else:
			self.anularBoton.setEnabled(False)
			
	def seleccionar_imagen(self):
		try:
			imagen, extension = QtWidgets.QFileDialog.getOpenFileName(self, "Seleccionar imagen", getcwd(),
															"Archivos de imagen (*.png *.jpg)",
															options=QtWidgets.QFileDialog.Options())
			  
			if imagen:
				# Adaptar imagen
				pixmapImagen = QPixmap(imagen)
				self.imagenBD = pixmapImagen
				
			if self.imagenBD:
				self.bArray = QByteArray()
				bufer = QBuffer(self.bArray)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				self.imagenBD.save(bufer, "PNG")
				self.checkEv.setChecked(True)
			else:
				self.bArray = ""
		except AttributeError:
			pass
			
	def guardar_registro(self):
		try:
			db = connect("bin/src/secs.db")
			conector = db.cursor()
			self.numeroSanc = self.boleta
			self.cooperativaSanc = self.coopCombo.currentText().upper()
			os.system("MD C:\\ecb\\Evidencias\\{}".format(self.numeroSanc))
			self.discSanc = self.discoEntry.text().upper()
			if self.discSanc[:4] == "BOLE":
				self.discSanc = "BOLETERÍA"
			self.fechSanc = self.fechaEntry.text()
			self.horaSanc = self.horaEntry.text()
			self.artSanc = self.artEntry.text().upper()
			self.litSanc = self.litEntry.text().upper()
			self.descripSanc = self.desEntry.toPlainText().upper()
			self.tipoSanc = self.tipCombo.currentText().upper()
			self.valorSanc = self.valorLabel.text().upper()
			self.creadoSanc = self.elabCombo.currentText().upper()
			self.ingresadoSanc = self.user.upper()
			self.boletero = self.nombreEntry.text().upper()
			if self.rutaLabel.text() == "":
				self.link = ""
			else:
				self.link = "C:\\ecb\\Evidencias\\{}".format(self.numeroSanc)
				
			valoresSanciones = (self.numeroSanc, self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero, self.bArray, self.link)
			valoresSanciones = (self.numeroSanc, self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero, self.bArray, self.link)
			conector.execute("UPDATE sanciones SET numeroSancion = ?, cooperativa = ?, disco = ?,fecha = ?, hora = ?, articulo = ?, literal = ?, descript = ?, tipoFalta = ?, valorFalta = ?, creadoPor = ?, modificadoPor = ?, fechaModif = ?, evidencia = ?, links = ? WHERE numeroSancion ='{}'".format(self.numeroSanc), valoresSanciones)
			pdf = GenerarPdf(valoresSanciones)
			db.commit()
			self.fname2 = self.rutaLabel.text()
			if self.fname2 != "":
				root = '"'
				for i in range(len(self.fname2)):
					if self.fname2[i] == "/":
						root += "\\"
					else:
						root += self.fname2[i]
				root += '"'
				origen = '"C:\\ecb\\Evidencias\\{}"'.format(self.numeroSanc)
				copiar = 'copy {} {}'.format(root, origen)
				os.system(copiar)
			#COPIADO DE ARCHIVOS
			del(self.bArray)
			box = QMessageBox(self)
			box.setWindowTitle('Registro Finalizado') 
			box.setText("Los datos se modificaron correctamente.\nSe ha modificado la Boleta de Sanción N°:\n%s\n Presiona Si para imprimir la boleta." %self.numeroSanc)
			box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
			botonSi = box.button(QMessageBox.Yes)
			botonSi.setText("Si")
			box.exec_()
			
			if box.clickedButton() == botonSi:
				multa = "Multas Generadas\\"+self.numeroSanc+".pdf"
				os.startfile(multa, "print")
				db.close()
				self.borrarCampos()
			else:
				db.close()
				self.borrarCampos()
		except AttributeError:
			alert = QMessageBox()
			alert.setWindowTitle("Sin Evidencia")
			alert.setText("Se modificará el registro sin modificar la evidencia de la sanción.")	
			alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
			alertSi = alert.button(QMessageBox.Yes)
			alertSi.setText("Si")
			alert.exec_()
			if alert.clickedButton() == alertSi:
				self.bArray = ""
				valoresSanciones = (self.numeroSanc, self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero, self.link)
				conector.execute("UPDATE sanciones SET numeroSancion = ?, cooperativa = ?, disco = ?,fecha = ?, hora = ?, articulo = ?, literal = ?, descript = ?, tipoFalta = ?, valorFalta = ?, creadoPor = ?, modificadoPor = ?, fechaModif = ?, links = ? WHERE numeroSancion ='{}'".format(self.numeroSanc), valoresSanciones)
				pdf = GenerarPdf(valoresSanciones)
				db.commit()
				self.fname2 = self.rutaLabel.text()
				if self.fname2 != "":
					root = '"'
					for i in range(len(self.fname2)):
						if self.fname2[i] == "/":
							root += "\\"
						else:
							root += self.fname2[i]
					root += '"'
					origen = '"C:\\ecb\\Evidencias\\{}"'.format(self.numeroSanc)
					copiar = 'copy {} {}'.format(root, origen)
					print(copiar)
					os.system(copiar)
				#COPIADO DE ARCHIVOS
				del(self.bArray)
				box = QMessageBox(self)
				box.setWindowTitle('Registro Finalizado') 
				box.setText("Los datos se modificaron correctamente.\nSe ha modificado la Boleta de Sanción N°:\n%s\n Presiona Si para imprimir la boleta." %self.numeroSanc)
				box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
				botonSi = box.button(QMessageBox.Yes)
				botonSi.setText("Si")
				box.exec_()
				
				if box.clickedButton() == botonSi:
					multa = "Multas Generadas\\"+self.numeroSanc+".pdf"
					os.startfile(multa, "print")
					db.close()
					self.borrarCampos()
				else:
					db.close()
					self.borrarCampos()
				
			
	def changeValue(self):
		try:
			valor = self.tipCombo.currentText()
			info = open("bin/src/sbu.bin", "rb")
			sbu = load(info)
			info.close()
			sbu = int(sbu)
			if valor == "Leve 5% SBU":
				total = round((sbu * 5 / 100), 2)
				self.valorLabel.setText(str(total))
				self.valorLabel.setStyleSheet("background-color: rgb(85, 255, 0);\n"
				"font: 11pt \"MS Shell Dlg 2\";\n"
				"color: rgb(255, 255, 255);")
			else:
				if valor == "Leve 10% SBU":
					total = round((sbu * 10 / 100), 2)
					self.valorLabel.setText(str(total)+"0")
					self.valorLabel.setStyleSheet("background-color: rgb(85, 85, 255);\n"
					"font: 11pt \"MS Shell Dlg 2\";\n"
					"color: rgb(255, 255, 255);")
				else:
					if valor == "Grave 20% SBU":
						total = round((sbu * 20 / 100), 2)
						self.valorLabel.setText(str(total)+"0")
						self.valorLabel.setStyleSheet("background-color: rgb(255, 0,0);\n"
						"font: 11pt \"MS Shell Dlg 2\";\n"
						"color: rgb(255, 255, 255);")
					else:
						self.valorLabel.setText("")
						self.valorLabel.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		except ValueError:
			QMessageBox.critical(self, "Error", "No es posible configurar los valores de las sanciones. Verifique y configure el SBU.", QMessageBox.Ok)
	
	def anular_sancion(self):
		try:
			db = connect("bin/src/secs.db")
			conector = db.cursor()
			self.numeroSanc = self.boleta
			self.descripSanc = "Anulado"
			valoresSanciones = (self.numeroSanc, self.descripSanc)
			conector.execute("UPDATE sanciones SET numeroSancion = ?, descript = ? WHERE numeroSancion = '{}'".format(self.numeroSanc), valoresSanciones)
			db.commit()
			#pdf = GenerarPdf(valoresSanciones)
			box = QMessageBox(self)
			box.setWindowTitle('Anulación Finalizada') 
			box.setText("Se ha anulado la Boleta de Sanción N°:\n%s" %self.numeroSanc)
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_()
				
			multa = "Multas Generadas\\"+self.numeroSanc+".pdf"
			os.system("del {}".format(multa))
			db.close()
			
		except AttributeError:
			alert = QMessageBox()
			alert.setWindowTitle("Error")
			alert.setText("No sabemos porqué, pero por algo ha de ser.")	
			alert.exec_()
			
	def showDialog(self):

		fname, _  = QtWidgets.QFileDialog.getOpenFileName(self, 'Buscar Archivo', QDir.homePath(), "All Files (*);;Text Files (*.txt)")

		if fname:
			self.rutaLabel.setText(fname)
			
	def borrarCampos(self):
		self.frame.setEnabled(False)
		self.coopCombo.setItemText(0," ")
		self.coopCombo.setCurrentIndex(0)
		self.discoEntry.clear()
		self.fechaEntry.clear()
		self.horaEntry.clear()
		self.artEntry.clear()
		self.litEntry.clear()
		self.desEntry.clear()
		self.tipCombo.setItemText(0,"")
		self.tipCombo.setCurrentIndex(0)
		self.valorLabel.clear()
		self.valorLabel.setStyleSheet(
				"font: 11pt \"MS Shell Dlg 2\";\n"
				"color: black;")
		self.elabCombo.setItemText(0,"")
		self.elabCombo.setCurrentIndex(0)
		self.nombreEntry.clear()
		self.rutaLabel.clear()
		self.boletaEntry.clear()
		