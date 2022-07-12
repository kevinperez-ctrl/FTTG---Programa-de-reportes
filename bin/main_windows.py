import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
import bin.src.recursos_rc
from sqlite3 import *
from bin.emision import *
from bin.consultas import *
from bin.modificar import *
from bin.confYear import *
from bin.imprimir import *
from bin.evidencias import *
from bin.operativos import *
from bin.confSBU import *
from bin.consultas_anteriores import *
from pickle import *


class Ventana(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.resize(339, 471)
		self.setWindowTitle("Sistema de Emisión y Consulta de  Sanciones")
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.setWindowOpacity(1.0)
		self.setStyleSheet("")
		self.centralwidget = QtWidgets.QWidget(self)
		self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget) 
		self.logoLabel = QtWidgets.QLabel(self.centralwidget)
		self.logoLabel.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 113, 186);") 
		self.gridLayout_2.addWidget(self.logoLabel, 0, 0, 1, 1)
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.gridLayout = QtWidgets.QGridLayout(self.frame)
		self.emitirLabel = QtWidgets.QLabel(self.frame)
		self.emitirLabel.setStyleSheet("color: rgb(0, 113, 186);\n"
"font: 12pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.emitirLabel, 0, 0, 1, 1)
		self.consultarLabel = QtWidgets.QLabel(self.frame)
		self.consultarLabel.setStyleSheet("color: rgb(0, 113, 186);\n"
"font: 12pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.consultarLabel, 1, 0, 1, 1)
		self.modificarLabel = QtWidgets.QLabel(self.frame)
		self.modificarLabel.setStyleSheet("color: rgb(0, 113, 186);\n"
"font: 12pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.modificarLabel, 2, 0, 1, 1)
		self.totalLabel = QtWidgets.QLabel(self.frame)
		self.totalLabel.setStyleSheet("color: rgb(0, 113, 186);\n"
"font: 12pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.totalLabel, 3, 0, 1, 2)
		self.resultLabel = QtWidgets.QLabel(self.frame)
		self.resultLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
		self.resultLabel.setText("")
		self.gridLayout.addWidget(self.resultLabel, 3, 2, 1, 1)
		self.emitirBoton = QtWidgets.QPushButton(self.frame)
		self.emitirBoton.setAutoFillBackground(True)
		self.emitirBoton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.emitirBoton.setAutoDefault(False)
		self.emitirBoton.setDefault(False)
		self.gridLayout.addWidget(self.emitirBoton, 0, 1, 1, 2)
		self.consultarBoton = QtWidgets.QPushButton(self.frame)
		self.consultarBoton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.consultarBoton, 1, 1, 1, 2)
		self.modifBoton = QtWidgets.QPushButton(self.frame)
		self.modifBoton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.modifBoton, 2, 1, 1, 2)
		self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
		self.frame.raise_()
		self.logoLabel.raise_()
		self.setCentralWidget(self.centralwidget)
		
		self.menubar = QtWidgets.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 21))
		self.menuInicio = QtWidgets.QMenu(self.menubar)
		self.menuConfiguraci_n = QtWidgets.QMenu(self.menubar)
		self.setMenuBar(self.menubar)
		self.actionSalir = QtWidgets.QAction(self)
		self.actionVer_Evidencias = QtWidgets.QAction(self)
		self.actionMultas_para_Operativo = QtWidgets.QAction(self)
		self.actionImprimir_Sanciones = QtWidgets.QAction(self)
		self.actionConsultar_Anterior = QtWidgets.QAction(self)
		self.actionConfigurar = QtWidgets.QAction(self)
		self.actionConfigurar_SBU = QtWidgets.QAction(self)
		self.menuInicio.addAction(self.actionVer_Evidencias)
		self.menuInicio.addAction(self.actionMultas_para_Operativo)
		self.menuInicio.addAction(self.actionImprimir_Sanciones)
		self.menuInicio.addSeparator()
		self.menuInicio.addAction(self.actionConsultar_Anterior)
		self.menuInicio.addSeparator()
		self.menuInicio.addAction(self.actionSalir)
		self.menuConfiguraci_n.addAction(self.actionConfigurar)
		self.menuConfiguraci_n.addAction(self.actionConfigurar_SBU)
		self.menubar.addAction(self.menuInicio.menuAction())
		self.menubar.addAction(self.menuConfiguraci_n.menuAction())
		
		
		
		db = connect("bin/src/secs.db")
		conector = db.cursor()
		conector.execute("SELECT * FROM sanciones")
		cantidadIngresadas = conector.fetchall()
		cantidadIngresadas = len(cantidadIngresadas)
		
		db.close()
		
		self.resultLabel.setText(str(cantidadIngresadas))
		self.setWindowTitle("Emisión y Consulta de Sanciones")
		self.logoLabel.setText("<html><head/><body><p align=\"center\">Bienvenido al </p><p align=\"center\">Sistema de Emisión </p><p align=\"center\">de Sanciones</p></body></html>")
		self.emitirLabel.setText("Emitir")
		self.consultarLabel.setText("Consultar")
		self.modificarLabel.setText("Modificar")
		self.totalLabel.setText("Total de multas registradas:")
		self.emitirBoton.setText("Emitir Sanción")
		self.emitirBoton.setShortcut("Ctrl+E")
		self.consultarBoton.setText("Consultar Sanción")
		self.consultarBoton.setShortcut("Ctrl+W")
		self.modifBoton.setText("Modificar Sanción")
		self.modifBoton.setShortcut("Ctrl+M")
		self.menuInicio.setTitle("Inicio")
		self.menuConfiguraci_n.setTitle("Configuración")
		self.actionSalir.setText("Salir")
		self.actionVer_Evidencias.setText("Ver Evidencias")
		self.actionMultas_para_Operativo.setText("Multas para Operativo")
		self.actionImprimir_Sanciones.setText("Imprimir Sanciones")
		self.actionConsultar_Anterior.setText("Consultar años anteriores")
		self.actionConfigurar.setText("Configurar Año")
		self.actionConfigurar_SBU.setText("Configurar SBU")
			
		self.setTabOrder(self.emitirBoton, self.consultarBoton)
		self.setTabOrder(self.consultarBoton, self.modifBoton)
		
		self.emitirSancion = ""
		self.emitirBoton.clicked.connect(self.emitir_sancion)
		
		
		self.consultarBoton.clicked.connect(self.consultar_sancion)
		
		
		self.actionConsultar_Anterior.triggered.connect(self.consultar_sancion_anterior)
		
		self.modifBoton.clicked.connect(self.modificar_sancion)

		self.actionSalir.triggered.connect(self.close)
		
		self.modificarYear = ConfigYear()
		self.actionConfigurar.triggered.connect(self.modificar_year)
		
		self.modificarSBU = ConfigSBU()
		self.actionConfigurar_SBU.triggered.connect(self.modificar_sbu)
		
		self.printSans = ImprimirSanciones()
		self.actionImprimir_Sanciones.triggered.connect(self.imprimir_sanciones)
		
		self.multasdeOperativo = GenerarOperativo()
		self.actionMultas_para_Operativo.triggered.connect(self.multas_operativo)
		
		self.datosEvidencia = VerEvidencias()
		self.actionVer_Evidencias.triggered.connect(self.ver_evidencias)
		
		x = time.strftime("%Y")
		year = open("bin/src/year.bin", "rb")
		y = load(year)
		year.close()
		if x == y:
			pass
		else:
			QMessageBox.question(self, "Nuevo Año", "Parece que ha iniciado un nuevo año\nNo olvide configurar el nuevo año.", QMessageBox.Ok)
		
	def emitir_sancion(self):
		db = connect("bin/src/secs.db")
		conector = db.cursor()
		
		conector.execute("SELECT numero, numeroSancion FROM sanciones WHERE cooperativa='OPERATIVO'")
		cantidadOperativo = conector.fetchall()
		cantidadOper = len(cantidadOperativo)
		listaOper = []
		for i in range(len(cantidadOperativo)):
			listaOper.append(cantidadOperativo[i][1])
		multasOper = []
		for i in range(len(listaOper)):
			multasOper.append(listaOper[i])
		texto_mostrar = "Parece que aún quedan multas en blanco (de operativos), no se olvide de llenar las siguientes multas:\n"
		for i in range(len(multasOper)):
			texto_mostrar += multasOper[i]
			texto_mostrar += "\n"
		if cantidadOper > 0:
			box = QMessageBox(self)
			box.setWindowTitle('Multas de Operativo') 
			box.setText(texto_mostrar)
			box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
			botonSi = box.button(QMessageBox.Yes)
			botonSi.setText("Si")
			box.exec_()
					
			if box.clickedButton() == botonSi:
				db.close()							
				self.emitirSancion = Emitir("COT", multasOper, multasOper)
				self.emitirSancion.exec_()
			else:
				db.close()
				db = connect("bin/src/secs.db")
				conector = db.cursor()
				conector.execute("SELECT * FROM sanciones ORDER BY numero DESC limit 1")
				lastoSancion = conector.fetchone()
				db.close()
				yearo = open("bin/src/year.bin", "rb")
				xo = load(yearo)
				yearo.close()
				if not lastoSancion:
					self.numeroSanco = "FTTG-TTMP-001-"+xo
				else:
					if lastoSancion[0] in range(9):
						self.numeroSanco = "FTTG-TTMP-00"+str(lastoSancion[0]+1)+"-"+xo
					else:
						if lastoSancion[0] in range(9,99):
							self.numeroSanco = "FTTG-TTMP-0"+str(lastoSancion[0]+1)+"-"+xo
						else:
							self.numeroSanco = "FTTG-TTMP-"+str(lastoSancion[0]+1)+"-"+xo
							
				self.emitirSancion = Emitir("COT", "", self.numeroSanco)
				self.emitirSancion.exec_()
				
		else:
			db.close()
			db = connect("bin/src/secs.db")
			conector = db.cursor()
			conector.execute("SELECT * FROM sanciones ORDER BY numero DESC limit 1")
			lastoSancion = conector.fetchone()
			yearo = open("bin/src/year.bin", "rb")
			xo = load(yearo)
			yearo.close()
			if not lastoSancion:
				self.numeroSanco = "FTTG-TTMP-001-"+xo
			else:
				if lastoSancion[0] in range(9):
					self.numeroSanco = "FTTG-TTMP-00"+str(lastoSancion[0]+1)+"-"+xo
				else:
					if lastoSancion[0] in range(9,99):
						self.numeroSanco = "FTTG-TTMP-0"+str(lastoSancion[0]+1)+"-"+xo
					else:
						self.numeroSanco = "FTTG-TTMP-"+str(lastoSancion[0]+1)+"-"+xo
						
			self.emitirSancion = Emitir("COT", "", self.numeroSanco)
			self.emitirSancion.exec_()
			
			
		
		
		
	def consultar_sancion(self):
		self.consultarSancion = Consultar("COT")
		self.consultarSancion.exec_()
		
	def consultar_sancion_anterior(self):
		self.consultarSancionAnterior = Consultar_Anterior("COT")
		self.consultarSancionAnterior.exec_()
		
	def modificar_sancion(self):
		self.modificarSancion = Modificar("COT")
		self.modificarSancion.exec_()
		
	def modificar_year(self):
		self.modificarYear.exec_()
		#FALTA GESTIONAR PARA QUE NO MODIFIQUEN
		
	def modificar_sbu(self):
		self.modificarSBU.exec_()
		#FALTA GESTIONAR PARA QUE NO MODIFIQUEN
		
	def multas_operativo(self):
		self.multasdeOperativo.exec_()
		
	def ver_evidencias(self):
		self.datosEvidencia.exec_()
		
	def imprimir_sanciones(self):
		self.printSans.exec_()
		
		
"""except Exception as e:
	print( type(e).__name__ )"""