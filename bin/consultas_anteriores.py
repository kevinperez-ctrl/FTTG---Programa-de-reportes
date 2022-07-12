import sys
import os
from os import getcwd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QByteArray, QIODevice, QBuffer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu, QActionGroup, QAction, QMessageBox
import bin.src.recursos_rc
from sqlite3 import *
from bin.pdfgen import *
import time

class Consultar_Anterior(QDialog):
	def __init__(self, user):
		QDialog.__init__(self)
		self.resize(700, 387)
		self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.yearLabel = QtWidgets.QLabel(self)
		self.yearLabel.setObjectName("yearLabel")
		self.gridLayout.addWidget(self.yearLabel, 0, 0, 1, 1)
		self.yearEntry = QtWidgets.QLineEdit(self)
		self.yearEntry.setObjectName("yearEntry")
		self.gridLayout.addWidget(self.yearEntry, 0, 1, 1, 2)
		self.busquedaLabel = QtWidgets.QLabel(self)
		self.gridLayout.addWidget(self.busquedaLabel, 1, 0, 1, 1)
		self.tipobusCombo = QtWidgets.QComboBox(self)
		self.tipobusCombo.addItem("")
		self.tipobusCombo.addItem("")
		self.tipobusCombo.addItem("")
		self.gridLayout.addWidget(self.tipobusCombo, 1, 1, 1, 2)
		self.buscarButton = QPushButton(self)
		self.gridLayout.addWidget(self.buscarButton, 1, 3, 1, 1)
		self.coopLabel = QtWidgets.QLabel(self)
		self.gridLayout.addWidget(self.coopLabel, 3, 0, 1, 1)
		self.coopCombo = QtWidgets.QComboBox(self)
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
		self.coopCombo.addItem("")
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
		self.coopCombo.setItemText(25,"Operativo")
		self.gridLayout.addWidget(self.coopCombo, 3, 1, 1, 2)
		self.discEntry = QtWidgets.QSpinBox(self)
		self.discEntry.setMaximum(300)
		self.gridLayout.addWidget(self.discEntry, 3, 3, 1, 1)
		self.discEntry.setEnabled(True)
		self.columButton = QtWidgets.QPushButton(self)
		self.gridLayout.addWidget(self.columButton, 5, 0, 1, 1)
		self.registrosLabel = QtWidgets.QLabel(self)
		self.gridLayout.addWidget(self.registrosLabel, 5, 2, 1, 1)
		self.resultadoLabel = QtWidgets.QLabel(self) 
		self.gridLayout.addWidget(self.resultadoLabel, 5, 3, 1, 1)
		self.tabla = QtWidgets.QTableWidget(self)
		self.gridLayout.addWidget(self.tabla, 6, 0, 1, 7)
		self.boleteria = QtWidgets.QComboBox(self)
		self.boleteria.addItem("")
		self.boleteria.setItemText(0, "")
		self.boleteria.addItem("")
		self.boleteria.setItemText(1, "BOLETERÍA")
		self.gridLayout.addWidget(self.boleteria, 3, 4, 1, 1)
		#CREACION DE LA TABLA
		self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tabla.setDragDropOverwriteMode(False)
		self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tabla.setTextElideMode(Qt.ElideRight)
		self.tabla.setWordWrap(False)
		self.tabla.setSortingEnabled(False)
		self.tabla.setColumnCount(13)
		self.tabla.setRowCount(0)
		self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.tabla.horizontalHeader().setHighlightSections(False)
		self.tabla.horizontalHeader().setStretchLastSection(True)
		self.tabla.verticalHeader().setVisible(False)
		self.tabla.setAlternatingRowColors(True)
		self.tabla.verticalHeader().setDefaultSectionSize(20)
		nombreColumnas = ("Numero de Sanción","Cooperativa", "Disco", "Fecha", "Hora", "Articulo", "Literal", "Descripcion", "Infractor", "Tipo de Falta", "Valor a Pagar", "Elaborado Por", "Evidencias")
		self.tabla.setHorizontalHeaderLabels(nombreColumnas)
		self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
		self.tabla.customContextMenuRequested.connect(self.menuContextual)
		for indice, ancho in enumerate((120, 120, 120, 110, 150), start=0):
			self.tabla.setColumnWidth(indice, ancho)

		menu = QMenu()
		for indice, columna in enumerate(nombreColumnas, start=0):
			accion = QAction(columna, menu)
			accion.setCheckable(True)
			accion.setChecked(True)
			accion.setData(indice)

			menu.addAction(accion)
		self.columButton.setMenu(menu)
		
		
		#EVENTOS
		self.buscarButton.clicked.connect(self.datosTabla)
		self.tabla.itemDoubleClicked.connect(self.infoCelda)
		menu.triggered.connect(self.mostrarOcultar)
		self.tipobusCombo.currentIndexChanged['int'].connect(self.change_value)
		
		
		QtCore.QMetaObject.connectSlotsByName(self)
		
		self.setWindowTitle("Consulta de Sanciones")
		self.busquedaLabel.setText("Realizar busqueda por:")
		self.tipobusCombo.setItemText(0, "Cooperativa")
		self.tipobusCombo.setItemText(1, "Fecha de emisión")
		self.tipobusCombo.setItemText(2, "Número de Boleta")
		self.coopLabel.setText("Cooperativa: ")
		self.columButton.setText("Motrar/Ocultar Columnas")
		self.registrosLabel.setText("Total de registros encontrados:")
		self.buscarButton.setText("Buscar")
		self.yearLabel.setText("Año de busqueda: ")
		
	def infoCelda(self, celda):
		box = QMessageBox(self)
		box.setWindowTitle('Información') 
		if celda.text()[:4] == 'FTTG':
			box.setText("{}\nPresione si para imprimir la sanción".format(celda.text()))
			box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
			botonSi = box.button(QMessageBox.Yes)
			botonSi.setText("Si")
			box.exec_()
			
			try:
				if box.clickedButton() == botonSi:
					self.db = connect("bin/src/secs.db")
					conector = self.db.cursor()
					tuplaDatos = (celda.text(),)
					conector.execute("SELECT numeroSancion, cooperativa, disco, fecha, hora, articulo, literal, descript, tipoFalta, valorFalta, creadoPor FROM sanciones{} WHERE numeroSancion=?".format(self.yearEntry), tuplaDatos)				
					datos_nuevo = conector.fetchone()
					datos_nuevo = list(datos_nuevo)
					for i in range(len(datos_nuevo)):
						if datos_nuevo[i] == None:
							datos_nuevo[i] = " "
					pdf = GenerarPdf(datos_nuevo)
					
					multa = "Multas Generadas\\"+celda.text()+".pdf"
					os.startfile(multa, "print")
				else:
					pass
			except FileNotFoundError:
				QMessageBox.question(self, "Información", "No se ha generado alguna multa con este número:\n {}".format(celda.text()), QMessageBox.Ok)
		else:
			#Abrir link		
			if celda.text()[:6] == 'C:\\ecb' :
				box.setText("{}\nPresione si para ver la evidencia.\n Recuerde que debe tener una aplicación externa para reproducir la evidencia.".format(celda.text()))
				print(celda.text())
				box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
				botonSi = box.button(QMessageBox.Yes)
				botonSi.setText("Si")
				box.exec_()
				
				if box.clickedButton() == botonSi:
				#try:
					os.system("start {}".format(celda.text()))
				#except FileNotFoundError:
				#	QMessageBox.question(self, "Información", "No se ha generado alguna multa con este número:\n {}".format(celda.text()), QMessageBox.Ok)
			else:
				if celda.text()[:3] == "..\\" or celda.text()[:3] == "ANA" or celda.text()[:5] == 'C:\\Us':
					box.setText("{}\nPresione si para ver la evidencia.\n Recuerde que debe tener una aplicación externa para reproducir la evidencia.".format(celda.text()))
					box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
					botonSi = box.button(QMessageBox.Yes)
					botonSi.setText("Si")
					box.exec_()
					
					if box.clickedButton() == botonSi:
						ruta = "C:\\ecb\\Evidencias\\Anteriores"
						os.system("start {}".format(ruta))
				
				else:
					box.setText("{}".format(celda.text()))
					box.exec_()
		


	def datosTabla(self):
		try:
			self.guardar_datos()
			self.resize(1310,390)
				
		except OperationalError:
			QMessageBox.question(self, "Información", "No hay datos que correspondan al siguiente año: {}".format(self.yearEntry.text()), QMessageBox.Ok)
			
		finally:
			self.db.close()	
	
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
		
	def change_value(self):
		valor = self.tipobusCombo.currentText()
		if valor == "Cooperativa":
			self.discEntry.setEnabled(True)
			del(self.coopCombo)
			self.coopCombo = QtWidgets.QComboBox(self)
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
			self.coopCombo.addItem("")
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
			self.coopCombo.setItemText(25,"Operativo")
			self.gridLayout.addWidget(self.coopCombo, 3, 1, 1, 2)
		else:
			if valor == "Fecha de emisión":
				self.discEntry.setEnabled(False)
				self.coopLabel.setText("Fecha de Emisión: ")
				del(self.coopCombo)
				self.coopCombo = QtWidgets.QDateEdit(self)
				self.gridLayout.addWidget(self.coopCombo, 3, 1, 1, 2)
				self.coopCombo.setDateTime(QtCore.QDateTime.currentDateTime())
				self.coopCombo.setCalendarPopup(True)
			else:
				if valor == "Número de Boleta":
					self.discEntry.setEnabled(False)
					self.coopLabel.setText("Número de Sanción: ")
					del(self.coopCombo)
					self.coopCombo = QtWidgets.QLineEdit(self)
					self.gridLayout.addWidget(self.coopCombo, 3, 1, 1, 2)
								
	
	def guardar_datos(self):
		self.db = connect("bin/src/secs.db")
		conector = self.db.cursor()
		if self.tipobusCombo.currentText() == "Cooperativa":
			coope = self.coopCombo.currentText().upper()
			if self.boleteria.currentText() == "BOLETERÍA":
				disc = "BOLETERÍA"
			else:
				if self.discEntry.value() in range(1,10):
					if coope == "REINA DEL CAMINO":
						disc = "00"+str(self.discEntry.value())
					else:
						disc = "0"+str(self.discEntry.value())
				else:
					if self.discEntry.value() in range(10,100):
						if coope == "REINA DEL CAMINO":
							disc = "0"+str(self.discEntry.value())
						else:
							disc = str(self.discEntry.value())
					else:
						disc = str(self.discEntry.value())
			
			if disc == "0" and self.boleteria.currentText() == "":
				tuplaDatos = (coope,)
				conector.execute("SELECT * FROM sanciones{} WHERE cooperativa=? ORDER BY numero DESC".format(self.yearEntry.text()), tuplaDatos)
					
				datos_new = conector.fetchall()
				datos = []
				self.datos_final = []
				for i in range(len(datos_new)):
					for y in range(len(datos_new[i])):
						datos.append(datos_new[i][y])
					datos = tuple(datos)
					self.datos_final.append(datos)
					datos = []
			else:
				if disc == "BOLETERÍA":
					tuplaDatos = (coope,)
					conector.execute("SELECT * FROM sanciones{} WHERE cooperativa=? and disco='BOLETERÍA' ORDER BY numero DESC".format(self.yearEntry.text()), tuplaDatos)
						
					datos_new = conector.fetchall()
					datos = []
					self.datos_final = []
					for i in range(len(datos_new)):
						for y in range(len(datos_new[i])):
							datos.append(datos_new[i][y])
						datos = tuple(datos)
						self.datos_final.append(datos)
						datos = []
				else:
					tuplaDatos = (coope, disc)
					conector.execute("SELECT * FROM sanciones{} WHERE cooperativa=? and disco=? ORDER BY numero DESC".format(self.yearEntry.text()), tuplaDatos)
							
					datos_new = conector.fetchall()
					datos = []
					self.datos_final = []
					for i in range(len(datos_new)):
						for y in range(len(datos_new[i])):
							datos.append(datos_new[i][y])
						datos = tuple(datos)
						self.datos_final.append(datos)
						datos = []
		else:
			if self.tipobusCombo.currentText() == "Fecha de emisión":
				coope = self.coopCombo.date()
				coope = str(coope.toPyDate())
				tuplaDatos = (coope,)
				conector.execute("SELECT * FROM sanciones{} WHERE fecha=? ORDER BY numero DESC".format(self.yearEntry.text()), tuplaDatos)
					
				datos_new = conector.fetchall()
				datos = []
				self.datos_final = []
				for i in range(len(datos_new)):
					for y in range(len(datos_new[i])):
						datos.append(datos_new[i][y])
					datos = tuple(datos)
					self.datos_final.append(datos)
					datos = []
			else:
				if self.tipobusCombo.currentText() == "Número de Boleta":
					coope = "FTTG-TTMP-"+self.coopCombo.text()
					tuplaDatos = (coope,)
					conector.execute("SELECT * FROM sanciones{} WHERE numeroSancion=? ORDER BY numero DESC".format(self.yearEntry.text()), tuplaDatos)
						
					datos_new = conector.fetchall()
					datos = []
					self.datos_final = []
					for i in range(len(datos_new)):
						for y in range(len(datos_new[i])):
							datos.append(datos_new[i][y])
						datos = tuple(datos)
						self.datos_final.append(datos)
						datos = []				
			
			
		self.tabla.clearContents()			
			
		self.resultadoLabel.setText(str(len(self.datos_final)))
		row = 0
		for endian in self.datos_final:
			self.tabla.setRowCount(row + 1)
					
			idDato = QTableWidgetItem(endian[1])
			idDato.setTextAlignment(Qt.AlignHCenter)
			dato1 = QTableWidgetItem(endian[2])
			dato1.setTextAlignment(Qt.AlignHCenter)
			dato2 = QTableWidgetItem(endian[3])
			dato2.setTextAlignment(Qt.AlignHCenter)
			dato3 = QTableWidgetItem(endian[4])
			dato3.setTextAlignment(Qt.AlignHCenter)
			dato4 = QTableWidgetItem(endian[5])
			dato4.setTextAlignment(Qt.AlignHCenter)
			dato5 = QTableWidgetItem(endian[6])
			dato5.setTextAlignment(Qt.AlignHCenter)
			dato6 = QTableWidgetItem(endian[7])
			dato6.setTextAlignment(Qt.AlignHCenter)
			dato7 = QTableWidgetItem(endian[8])
			dato7.setTextAlignment(Qt.AlignHCenter)
			dato8 = QTableWidgetItem(endian[14])
			dato8.setTextAlignment(Qt.AlignHCenter)
			dato9 = QTableWidgetItem(endian[9])
			dato9.setTextAlignment(Qt.AlignHCenter)
			dato10 = QTableWidgetItem(endian[10])
			dato10.setTextAlignment(Qt.AlignHCenter)
			dato11 = QTableWidgetItem(endian[11])
			dato11.setTextAlignment(Qt.AlignHCenter)
			dato12 = QTableWidgetItem(endian[16])
			dato12.setTextAlignment(Qt.AlignHCenter)
			

					
			self.tabla.setItem(row, 0, idDato)
			self.tabla.setItem(row, 1, dato1)
			self.tabla.setItem(row, 2, dato2)
			self.tabla.setItem(row, 3, dato3)
			self.tabla.setItem(row, 4, dato4)
			self.tabla.setItem(row, 5, dato5)
			self.tabla.setItem(row, 6, dato6)
			self.tabla.setItem(row, 7, dato7)
			self.tabla.setItem(row, 8, dato8)
			self.tabla.setItem(row, 9, dato9)
			self.tabla.setItem(row, 10, dato10)
			self.tabla.setItem(row, 11, dato11)
			self.tabla.setItem(row, 12, dato12)
	
					

			row += 1
					