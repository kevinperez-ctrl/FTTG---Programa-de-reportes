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


class Emitir(QDialog):
	def __init__(self, user, lista_boletas, numeroSancionNueva):
		QDialog.__init__(self)
		self.resize(570, 530)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.user = user
		self.lista_boletas = lista_boletas
		self.numeroVentana = numeroSancionNueva
	#ESTABLECER ELEMENTOS
		self.totalPagarLabel = QtWidgets.QLabel(self)
		self.totalPagarLabel.setGeometry(QtCore.QRect(259, 224, 64, 16))
		self.literalLabel = QtWidgets.QLabel(self)
		self.literalLabel.setGeometry(QtCore.QRect(290, 66, 29, 20))
		self.tipofaltaLabel = QtWidgets.QLabel(self)
		self.tipofaltaLabel.setGeometry(QtCore.QRect(10, 224, 60, 16))
		self.evidenciaLabel = QtWidgets.QLabel(self)
		self.evidenciaLabel.setGeometry(QtCore.QRect(260, 260, 101, 16))
		self.evidenciaLabel.setText("Agregar evidencia: ")
		self.ingresarButton = QtWidgets.QPushButton(self)
		self.ingresarButton.setGeometry(QtCore.QRect(360, 260, 75, 23))
		self.ingresarButton.setToolTip("Solo archivos jpg o png")
		self.ingresarButton.setText("Imagenes")
		self.ingresarButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.checkEv = QtWidgets.QCheckBox(self)
		self.checkEv.setGeometry(QtCore.QRect(520, 260, 21, 21))
		self.checkEv.setEnabled(False)
		self.checkEv.setChecked(False)
		self.descriptEdit = QtWidgets.QPlainTextEdit(self)
		self.descriptEdit.setGeometry(QtCore.QRect(11, 118, 551, 51))
		self.discoEdit = QtWidgets.QLineEdit(self)
		self.discoEdit.setGeometry(QtCore.QRect(320, 40, 133, 20))
		self.literalEdit = QtWidgets.QLineEdit(self)
		self.literalEdit.setGeometry(QtCore.QRect(320, 70, 133, 20))
		self.fechaEdit = QtWidgets.QDateEdit(self)
		self.fechaEdit.setGeometry(QtCore.QRect(84, 11, 191, 20))
		self.fechaEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.fechaEdit.setCalendarPopup(True)
		self.articuloLabel = QtWidgets.QLabel(self)
		self.articuloLabel.setGeometry(QtCore.QRect(10, 70, 36, 16))
		self.tipoCombo = QtWidgets.QComboBox(self)
		self.tipoCombo.setGeometry(QtCore.QRect(83, 224, 103, 20))
		self.tipoCombo.addItem("")
		self.tipoCombo.setItemText(0, "")
		self.tipoCombo.addItem("")
		self.tipoCombo.addItem("")
		self.tipoCombo.addItem("")
		self.artEdit = QtWidgets.QLineEdit(self)
		self.artEdit.setGeometry(QtCore.QRect(92, 70, 121, 20))
		self.horaEdit = QtWidgets.QTimeEdit(self)
		self.horaEdit.setGeometry(QtCore.QRect(320, 10, 133, 20))
		self.horaEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.descripLabel = QtWidgets.QLabel(self)
		self.descripLabel.setGeometry(QtCore.QRect(11, 99, 54, 16)) 
		self.coopCombo = QtWidgets.QComboBox(self)
		self.coopCombo.setGeometry(QtCore.QRect(84, 37, 191, 21))
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
		self.fechaLabel = QtWidgets.QLabel(self)
		self.fechaLabel.setGeometry(QtCore.QRect(11, 11, 29, 16))
		self.cooperativaLabel = QtWidgets.QLabel(self)
		self.cooperativaLabel.setGeometry(QtCore.QRect(11, 37, 59, 16))
		self.elaboradoCombo = QtWidgets.QComboBox(self)
		self.elaboradoCombo.setGeometry(QtCore.QRect(80, 260, 126, 20))
		self.elaboradoCombo.addItem("")
		self.elaboradoCombo.setItemText(0, "")
		self.elaboradoCombo.addItem("")
		self.elaboradoCombo.addItem("")
		self.elaboradoCombo.addItem("")
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(290, 10, 23, 16))
		self.elaboradoLabel = QtWidgets.QLabel(self)
		self.elaboradoLabel.setGeometry(QtCore.QRect(10, 260, 67, 16))
		self.discoLabel = QtWidgets.QLabel(self)
		self.discoLabel.setGeometry(QtCore.QRect(290, 40, 25, 16)) 
		self.valorLabel = QtWidgets.QLabel(self)
		self.valorLabel.setGeometry(QtCore.QRect(340, 220, 51, 21))
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(490, 60, 31, 31))
		self.pushButton.setText("")
		self.icon1 = QtGui.QIcon()
		self.icon1.addPixmap(QtGui.QPixmap("bin/img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pushButton.setIcon(self.icon1)
		self.pushButton.setAutoDefault(True)
		self.pushButton.setIconSize(QtCore.QSize(200, 200))
		self.anteLabel = QtWidgets.QLabel(self)
		self.anteLabel.setGeometry(QtCore.QRect(470, 40, 101, 20))
		self.infrac = QtWidgets.QLabel(self)
		self.infrac.setGeometry(QtCore.QRect(10, 180, 111, 16))
		self.infrac.setText("Nombre del infractor: ")
		self.nombreInfrac = QtWidgets.QLineEdit(self)
		self.nombreInfrac.setGeometry(QtCore.QRect(120, 180, 441, 20))
		self.guardarButton = QtWidgets.QPushButton(self)
		self.guardarButton.setGeometry(QtCore.QRect(200, 300, 75, 23))
		self.guardarButton.setText("Guardar")
		self.guardarButton.setEnabled(False)
		self.borrarButton = QtWidgets.QPushButton(self)
		self.borrarButton.setGeometry(QtCore.QRect(280, 300, 75, 23))
		self.borrarButton.setText("Borrar")
		self.videosButton = QtWidgets.QPushButton(self)
		self.videosButton.setGeometry(QtCore.QRect(440, 260, 75, 23))
		self.videosButton.setText("Otros")
		self.videosButton.setAutoDefault(False)
		self.rutaLabel = QtWidgets.QLabel(self)
		self.rutaLabel.setGeometry(QtCore.QRect(440, 290, 121, 20))
		self.rutaLabel.setText("")
		self.tabla = QtWidgets.QTableWidget(self)
		self.tabla.setGeometry(QtCore.QRect(10, 380, 551, 141))
		self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tabla.setDragDropOverwriteMode(False)
		self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tabla.setTextElideMode(Qt.ElideRight)
		self.tabla.setWordWrap(False)
		self.tabla.setSortingEnabled(False)
		self.tabla.setColumnCount(6)
		self.tabla.setRowCount(0)
		self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.tabla.horizontalHeader().setHighlightSections(False)
		self.tabla.horizontalHeader().setStretchLastSection(True)
		self.tabla.verticalHeader().setVisible(False)
		self.tabla.setAlternatingRowColors(True)
		self.tabla.verticalHeader().setDefaultSectionSize(20)
		nombreColumnas = ("Sanción","Cooperativa", "Disco", "Fecha", "Hora", "Descripcion")
		self.tabla.setHorizontalHeaderLabels(nombreColumnas)
		self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
		self.tabla.customContextMenuRequested.connect(self.menuContextual)
		for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
			self.tabla.setColumnWidth(indice, ancho)

		menu = QMenu()
		for indice, columna in enumerate(nombreColumnas, start=0):
			accion = QAction(columna, menu)
			accion.setCheckable(True)
			accion.setChecked(True)
			accion.setData(indice)

			menu.addAction(accion)

		botonMostrarOcultar = QPushButton("Motrar/ocultar columnas", self)
		botonMostrarOcultar.setMenu(menu)
		botonMostrarOcultar.setGeometry(QtCore.QRect(10, 350, 171, 23))

	#manego de signals y slots
		self.pushButton.clicked.connect(self.datosTabla)
		self.tabla.itemDoubleClicked.connect(self.infoCelda)
		menu.triggered.connect(self.mostrarOcultar)
		self.tipoCombo.currentIndexChanged['int'].connect(self.changeValue)
		self.guardarButton.clicked.connect(self.guardar_registro)
		self.borrarButton.clicked.connect(self.borrar_campos)
		self.elaboradoCombo.currentIndexChanged['int'].connect(self.habilitar_guardado)
		self.ingresarButton.clicked.connect(self.seleccionar_imagen)
		self.videosButton.clicked.connect(self.showDialog)
		
		
	#Agregar valores a los elementos
		QtCore.QMetaObject.connectSlotsByName(self)
		if type(self.numeroVentana) == list: 
			self.setWindowTitle("Emitir Sanción:                         {}".format(self.lista_boletas[0]))
		else:
			self.setWindowTitle("Emitir Sanción:                         {}".format(self.numeroVentana))
		self.totalPagarLabel.setText("Total a pagar")
		self.literalLabel.setText("Literal")
		self.tipofaltaLabel.setText("Tipo de falta")
		self.articuloLabel.setText("Articulo")
		self.tipoCombo.setItemText(1,"Leve 5% SBU")
		self.tipoCombo.setItemText(2,"Leve 10% SBU")
		self.tipoCombo.setItemText(3,"Grave 20% SBU")
		self.descripLabel.setText("Descripcion")
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
		self.fechaLabel.setText("Fecha")
		self.cooperativaLabel.setText("Cooperativa")
		self.elaboradoCombo.setItemText(1,"Cercado Washington")
		self.elaboradoCombo.setItemText(2,"Tigua Alex")
		self.elaboradoCombo.setItemText(3,"Velez Jose")
		self.label.setText("Hora")
		self.elaboradoLabel.setText("Elaborado por")
		self.discoLabel.setText("Disco")
		self.valorLabel.setText("")
		self.anteLabel.setText("Ver antecedentes")
		
	#Orden de los tabs
		self.setTabOrder(self.coopCombo, self.discoEdit)
		self.setTabOrder(self.discoEdit, self.artEdit)
		self.setTabOrder(self.artEdit, self.literalEdit)
		self.setTabOrder(self.literalEdit, self.descriptEdit)
		self.setTabOrder(self.descriptEdit, self.tipoCombo)
		self.setTabOrder(self.tipoCombo, self.elaboradoCombo)
		self.setTabOrder(self.elaboradoCombo, self.guardarButton)
		self.setTabOrder(self.guardarButton, self.borrarButton)
	
	#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
	
		
		
		#funciones
	
	def infoCelda(self, celda):
		QMessageBox.question(self, "Información", "{}".format(celda.text()), QMessageBox.Ok)

	def datosTabla(self):
		try:
			coope = self.coopCombo.currentText().upper()
			disc = self.discoEdit.text()
			tuplaDatos = (coope, disc)
			db = connect("bin/src/secs.db")
			conector = db.cursor()
			conector.execute("SELECT numeroSancion, cooperativa, disco, fecha, hora, descript FROM sanciones WHERE cooperativa=? and disco=? ORDER BY numero DESC", tuplaDatos)
			
			datos = conector.fetchall()
			self.tabla.clearContents()

			row = 0
			for endian in datos:
				self.tabla.setRowCount(row + 1)
					
				idDato = QTableWidgetItem(endian[0])
				idDato.setTextAlignment(4)
				QTableWidgetItem(endian[1]).setTextAlignment(Qt.AlignHCenter)
				dato1 = QTableWidgetItem(endian[1])
				dato1.setTextAlignment(Qt.AlignHCenter)
				dato2 = QTableWidgetItem(endian[2])
				dato2.setTextAlignment(Qt.AlignHCenter)
				dato3 = QTableWidgetItem(endian[3])
				dato3.setTextAlignment(Qt.AlignHCenter)
				dato4 = QTableWidgetItem(endian[4])
				dato4.setTextAlignment(Qt.AlignHCenter)
				dato5 = QTableWidgetItem(endian[5])
				dato5.setTextAlignment(Qt.AlignHCenter)
				
				self.tabla.setItem(row, 0, idDato)
				self.tabla.setItem(row, 1, dato1)
				self.tabla.setItem(row, 2, dato2)
				self.tabla.setItem(row, 3, dato3)
				self.tabla.setItem(row, 4, dato4)
				self.tabla.setItem(row, 5, dato5)

				row += 1
				
		except Exception as e:
			print( type(e).__name__ )
		finally:
			db.close()	
		
		
		
	def changeValue(self):
		try:
			valor = self.tipoCombo.currentText()
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
			
			
	def mostrarOcultar(self, accion):
		columna = accion.data()
			
		if accion.isChecked():
			self.tabla.setColumnHidden(columna, False)
		else:
			self.tabla.setColumnHidden(columna, True)

	def eliminarFila(self):
		filaSeleccionada = self.tabla.selectedItems()
		if filaSeleccionada:
			fila = filaSeleccionada[0].row()
			self.tabla.removeRow(fila)

			self.tabla.clearSelection()
		else:
			QMessageBox.critical(self, "Eliminar fila", "Seleccione una fila.	",
								 QMessageBox.Ok)

	def limpiarTabla(self):
		self.tabla.clearContents()
		self.tabla.setRowCount(0)

	def menuContextual(self, posicion):
		indices = self.tabla.selectedIndexes()

		if indices:
			menu = QMenu()

			itemsGrupo = QActionGroup(self)
			itemsGrupo.setExclusive(True)
				
			menu.addAction(QAction("Copiar todo", itemsGrupo))

			columnas = [self.tabla.horizontalHeaderItem(columna).text()
			for columna in range(self.tabla.columnCount())
			if not self.tabla.isColumnHidden(columna)]

			copiarIndividual = menu.addMenu("Copiar individual") 
			for indice, item in enumerate(columnas, start=0):
				accion = QAction(item, itemsGrupo)
				accion.setData(indice)
					
				copiarIndividual.addAction(accion)

			itemsGrupo.triggered.connect(self.copiarTableWidgetItem)
				
			menu.exec_(self.tabla.viewport().mapToGlobal(posicion))

	def copiarTableWidgetItem(self, accion):
		filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]
				
		if accion.text() == "Copiar todo":
			filaSeleccionada = tuple(filaSeleccionada)
		else:
			filaSeleccionada = filaSeleccionada[accion.data()]

		print(filaSeleccionada)

		return
		
	def guardar_registro(self):
		if self.lista_boletas != "":
			try:
				db = connect("bin/src/secs.db")
				conector = db.cursor()
				self.numeroSanc = self.lista_boletas
				self.cooperativaSanc = self.coopCombo.currentText().upper()
				self.discSanc = self.discoEdit.text().upper()
				if self.discSanc[:4] == "BOLE":
					self.discSanc = "BOLETERÍA"
				self.fechSanc = self.fechaEdit.date()
				self.fechSanc = str(self.fechSanc.toPyDate())
				horas = self.horaEdit.time().hour()
				minutos = self.horaEdit.time().minute()
				for i in range(10):
					if str(horas) == str(i):
						horas = str(horas)
						horas = "0"+horas
					if str(minutos) == str(i):
						minutos = str(minutos)
						minutos = "0"+minutos
							
				self.horaSanc = str(horas)+":"+str(minutos)
				self.artSanc = self.artEdit.text()
				self.litSanc = self.literalEdit.text().upper()
				self.descripSanc = self.descriptEdit.toPlainText().upper()
				self.boletero = self.nombreInfrac.text().upper()
				self.tipoSanc = self.tipoCombo.currentText()
				self.valorSanc = self.valorLabel.text()
				self.creadoSanc = self.elaboradoCombo.currentText().upper()
				self.ingresadoSanc = self.user.upper()
				if self.rutaLabel.text() == "":
					os.system("MD C:\\ecb\\Evidencias\\{}".format(self.numeroSanc[0]))
					self.link = ""
				else:
					os.system("MD C:\\ecb\\Evidencias\\{}".format(self.numeroSanc[0]))
					self.link = "C:\\ecb\\Evidencias\\{}".format(self.numeroSanc[0])
				valoresSanciones = (self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero, self.bArray, self.link)
				conector.execute("UPDATE sanciones SET cooperativa = ?, disco = ?,fecha = ?, hora = ?, articulo = ?, literal = ?, descript = ?, tipoFalta = ?, valorFalta = ?, creadoPor = ?, modificadoPor = ?, fechaModif = ?, evidencia = ?, links = ? WHERE numeroSancion ='{}'".format(self.numeroSanc[0]), valoresSanciones)				
				valoresSanciones = (self.numeroSanc[0], self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero, self.bArray, self.link)
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
					origen = '"C:\\ecb\\Evidencias\\{}"'.format(self.numeroSanc[0])
					copiar = 'copy {} {}'.format(root, origen)
					os.system(copiar)
				#COPIADO DE ARCHIVOS
				del(self.bArray)
				box = QMessageBox(self)
				box.setWindowTitle('Registro Finalizado') 
				box.setText("Los datos se registraron correctamente.\nSe ha creado la Boleta de Sanción N°:\n%s\n Presiona Si para imprimir la boleta." %self.numeroSanc[0])
				box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
				botonSi = box.button(QMessageBox.Yes)
				botonSi.setText("Si")
				box.exec_()
				
				if box.clickedButton() == botonSi:
					multa = "Multas Generadas\\"+self.numeroSanc[0]+".pdf"
					os.startfile(multa, "print")
					self.numeroSanc.remove(self.numeroSanc[0])
					self.borrar_campos()
					db.close()
					if len(self.lista_boletas) > 0:
						self.setWindowTitle("Emitir Sanción:                         {}".format(self.lista_boletas[0]))
					else:
						self.setWindowTitle("Emitir Sanción: ")
						QMessageBox.question(self, "Finalizado", "Se han llenado todas las multas en blanco.", QMessageBox.Ok)
						self.close()
				else:
					self.numeroSanc.remove(self.numeroSanc[0])
					self.borrar_campos()
					db.close()
					if len(self.lista_boletas) > 0:
						self.setWindowTitle("Emitir Sanción:                         {}".format(self.lista_boletas[0]))
					else:
						self.setWindowTitle("Emitir Sanción: ")
						QMessageBox.question(self, "Finalizado", "Se han llenado todas las multas en blanco.", QMessageBox.Ok)
						self.close()
				
			except AttributeError:
				alert = QMessageBox(self)
				alert.setWindowTitle("Sin Evidencia")
				alert.setText("Se guardará el registro sin registrar evidencia de la sanción.\n ¿Aceptar?")
				alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
				alertSi = alert.button(QMessageBox.Yes)
				alertSi.setText("Si")
				alert.exec_()
				if alert.clickedButton() == alertSi:
					self.bArray = ""
					valoresSanciones = (self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero,self.link)
					conector.execute("UPDATE sanciones SET cooperativa = ?, disco = ?,fecha = ?, hora = ?, articulo = ?, literal = ?, descript = ?, tipoFalta = ?, valorFalta = ?, creadoPor = ?, modificadoPor = ?, fechaModif = ?, links = ? WHERE numeroSancion ='{}'".format(self.numeroSanc[0]), valoresSanciones)
					valoresSanciones = (self.numeroSanc[0], self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero,self.link)
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
						origen = '"C:\\ecb\\Evidencias\\{}"'.format(self.numeroSanc[0])
						copiar = 'copy {} {}'.format(root, origen)
						os.system(copiar)
					#COPIADO DE ARCHIVOS
					del(self.bArray)
					box = QMessageBox()
					box.setWindowTitle('Registro Finalizado') 
					box.setText("Los datos se registraron correctamente.\nSe ha creado la Boleta de Sanción N°:\n%s\n Presiona Si para imprimir la boleta." %self.numeroSanc[0])
					box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
					botonSi = box.button(QMessageBox.Yes)
					botonSi.setText("Si")
					box.exec_()
					
					if box.clickedButton() == botonSi:
						multa = "Multas Generadas\\"+self.numeroSanc[0]+".pdf"
						os.startfile(multa, "print")
						self.numeroSanc.remove(self.numeroSanc[0])
						self.borrar_campos()
						db.close()
						if len(self.lista_boletas) > 0:
							self.setWindowTitle("Emitir Sanción:                         {}".format(self.lista_boletas[0]))
						else:
							self.setWindowTitle("Emitir Sanción: ")
							QMessageBox.question(self, "Finalizado", "Se han llenado todas las multas en blanco.", QMessageBox.Ok)
							self.close()
					else:
						self.numeroSanc.remove(self.numeroSanc[0])
						self.borrar_campos()
						db.close()	
						if len(self.lista_boletas) > 0:
							self.setWindowTitle("Emitir Sanción:                         {}".format(self.lista_boletas[0]))
						else:
							self.setWindowTitle("Emitir Sanción: ")
							QMessageBox.question(self, "Finalizado", "Se han llenado todas las multas en blanco.", QMessageBox.Ok)		######
							self.close()
		else:
			try:
				db = connect("bin/src/secs.db")
				conector = db.cursor()
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
				self.cooperativaSanc = self.coopCombo.currentText().upper()
				self.discSanc = self.discoEdit.text().upper()
				if self.discSanc[:4] == "BOLE":
					self.discSanc = "BOLETERÍA"
				self.fechSanc = self.fechaEdit.date()
				self.fechSanc = str(self.fechSanc.toPyDate())
				horas = self.horaEdit.time().hour()
				minutos = self.horaEdit.time().minute()
				for i in range(10):
					if str(horas) == str(i):
						horas = str(horas)
						horas = "0"+horas
					if str(minutos) == str(i):
						minutos = str(minutos)
						minutos = "0"+minutos
							
				self.horaSanc = str(horas)+":"+str(minutos)
				self.artSanc = self.artEdit.text()
				self.litSanc = self.literalEdit.text().upper()
				self.boletero = self.nombreInfrac.text().upper()
				self.descripSanc = self.descriptEdit.toPlainText().upper()
				self.tipoSanc = self.tipoCombo.currentText()
				self.valorSanc = self.valorLabel.text()
				self.creadoSanc = self.elaboradoCombo.currentText().upper()
				self.ingresadoSanc = self.user.upper()
				if self.rutaLabel.text() == "":
					os.system("MD C:\\ecb\\Evidencias\\{}".format(self.numeroSanc))
					self.link = ""
				else:
					os.system("MD C:\\ecb\\Evidencias\\{}".format(self.numeroSanc))
					self.link = "C:\\ecb\\Evidencias\\{}".format(self.numeroSanc)
				valoresSanciones = (self.numeroSanc, self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc, self.boletero, self.bArray, self.link)
				if not lastSancion:
					conector.execute("INSERT INTO sanciones VALUES (1, ?,?,?,?,?,?,?,?,?,?,?,?,null,?,?,?)", valoresSanciones)
				else:
					conector.execute("INSERT INTO sanciones VALUES (null, ?,?,?,?,?,?,?,?,?,?,?,?,null,?,?,?)", valoresSanciones)
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
				box.setText("Los datos se registraron correctamente.\nSe ha creado la Boleta de Sanción N°:\n%s\n Presiona Si para imprimir la boleta." %self.numeroSanc)
				box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
				botonSi = box.button(QMessageBox.Yes)
				botonSi.setText("Si")
				box.exec_()
				
				if box.clickedButton() == botonSi:
					multa = "Multas Generadas\\"+self.numeroSanc+".pdf"
					os.startfile(multa, "print")
					self.borrar_campos()
					db.close()
					numeroNuevo = int(self.numeroVentana[10:13]) + 1
					if numeroNuevo in range(10):
						sancionNueva = "FTTG-TTMP-"+"00"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
					elif numeroNuevo in range(10,100):
						sancionNueva = "FTTG-TTMP-"+"0"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
					else:
						sancionNueva = "FTTG-TTMP-"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
					self.numeroVentana = sancionNueva
					self.setWindowTitle("Emitir Sanción:                         {}".format(self.numeroVentana))
				else:
					self.borrar_campos()
					db.close()
					numeroNuevo = int(self.numeroVentana[10:13]) + 1
					if numeroNuevo in range(10):
						sancionNueva = "FTTG-TTMP-"+"00"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
					elif numeroNuevo in range(10,100):
						sancionNueva = "FTTG-TTMP-"+"0"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
					else:
						sancionNueva = "FTTG-TTMP-"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
					self.numeroVentana = sancionNueva
					self.setWindowTitle("Emitir Sanción:                         {}".format(self.numeroVentana))
				
			except AttributeError:
				alert = QMessageBox(self)
				alert.setWindowTitle("Sin Evidencia")
				alert.setText("Se guardará el registro sin registrar evidencia de la sanción.\n ¿Aceptar?")
				alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
				alertSi = alert.button(QMessageBox.Yes)
				alertSi.setText("Si")
				alert.exec_()
				if alert.clickedButton() == alertSi:
					self.bArray = ""
					valoresSanciones = (self.numeroSanc, self.cooperativaSanc, self.discSanc, self.fechSanc, self.horaSanc, self.artSanc, self.litSanc, self.descripSanc, self.tipoSanc, self.valorSanc, self.creadoSanc, self.ingresadoSanc,self.boletero,self.link)
					if not lastSancion:
						conector.execute("INSERT INTO sanciones VALUES (1, ?,?,?,?,?,?,?,?,?,?,?,?,null,?,null,?)", valoresSanciones)
					else:
						conector.execute("INSERT INTO sanciones VALUES (null, ?,?,?,?,?,?,?,?,?,?,?,?,null,?,null,?)", valoresSanciones)
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
					box = QMessageBox()
					box.setWindowTitle('Registro Finalizado') 
					box.setText("Los datos se registraron correctamente.\nSe ha creado la Boleta de Sanción N°:\n%s\n Presiona Si para imprimir la boleta." %self.numeroSanc)
					box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
					botonSi = box.button(QMessageBox.Yes)
					botonSi.setText("Si")
					box.exec_()
					
					if box.clickedButton() == botonSi:
						multa = "Multas Generadas\\"+self.numeroSanc+".pdf"
						os.startfile(multa, "print")
						self.borrar_campos()
						db.close()
						numeroNuevo = int(self.numeroVentana[10:13]) + 1
						if numeroNuevo in range(10):
							sancionNueva = "FTTG-TTMP-"+"00"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
						elif numeroNuevo in range(10,100):
							sancionNueva = "FTTG-TTMP-"+"0"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
						else:
							sancionNueva = "FTTG-TTMP-"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
						self.numeroVentana = sancionNueva
						self.setWindowTitle("Emitir Sanción:                         {}".format(self.numeroVentana))
					else:
						self.borrar_campos()
						db.close()
						numeroNuevo = int(self.numeroVentana[10:13]) + 1
						if numeroNuevo in range(10):
							sancionNueva = "FTTG-TTMP-"+"00"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
						elif numeroNuevo in range(10,100):
							sancionNueva = "FTTG-TTMP-"+"0"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
						else:
							sancionNueva = "FTTG-TTMP-"+str(numeroNuevo)+"-"+self.numeroVentana[14:18]
						self.numeroVentana = sancionNueva
						self.setWindowTitle("Emitir Sanción:                         {}".format(self.numeroVentana))
			
				
			
	def borrar_campos(self):
		self.discoEdit.clear()
		self.coopCombo.setCurrentIndex(0)
		self.artEdit.clear()
		self.literalEdit.clear()
		self.descriptEdit.clear()
		self.tipoCombo.setCurrentIndex(0)
		self.valorLabel.clear()
		self.elaboradoCombo.setCurrentIndex(0)
		self.guardarButton.setEnabled(False)
		self.tabla.clearContents()
		self.fechaEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.horaEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.checkEv.setChecked(False)
		self.rutaLabel.clear()
		self.nombreInfrac.clear()
		try:
			if self.bArray:
				del(self.bArray)
		except AttributeError:
			pass

	def habilitar_guardado(self):
		self.guardarButton.setEnabled(True)
		
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
			
	def showDialog(self):

		fname, _  = QtWidgets.QFileDialog.getOpenFileName(self, 'Buscar Archivo', QDir.homePath(), "All Files (*);;Text Files (*.txt)")

		if fname:
			self.rutaLabel.setText(fname)
		