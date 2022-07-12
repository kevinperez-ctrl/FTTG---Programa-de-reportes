import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
import bin.src.recursos_rc
from sqlite3 import *
from bin.pdfgen import *

class ImprimirSanciones(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.resize(254, 157)
		self.formLayout = QtWidgets.QFormLayout(self)
		self.formLayout.setObjectName("formLayout")
		self.label = QtWidgets.QLabel(self)
		self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		self.label.setObjectName("label")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.label_2.setObjectName("label_2")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setObjectName("lineEdit")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.pushButton.setAutoDefault(False)
		self.pushButton.setObjectName("pushButton")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self)
		self.pushButton_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.pushButton_2.setObjectName("pushButton_2")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton_2)
		self.pushButton_3 = QtWidgets.QPushButton(self)
		self.pushButton_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.pushButton_3.setObjectName("pushButton_3")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton_3)

		QtCore.QMetaObject.connectSlotsByName(self)

		self.setWindowTitle("Imprimir Sanciones")
		self.label.setText("Ingrese el número de sanción:")
		self.label_2.setText("FTTG-TTMP")
		self.pushButton.setText("Borrar")
		self.pushButton_2.setText("Imprimir")
		self.pushButton_3.setText("Salir")
		
		self.pushButton.clicked.connect(self.lineEdit.clear)
		self.pushButton_2.clicked.connect(self.realizar_impresion)
		self.pushButton_3.clicked.connect(self.close)
		
	def realizar_impresion(self):
		x = "FTTG-TTMP-"+self.lineEdit.text()
		self.db = connect("bin/src/secs.db")
		conector = self.db.cursor()
		tuplaDatos = (x,)
		conector.execute("SELECT numeroSancion, cooperativa, disco, fecha, hora, articulo, literal, descript, tipoFalta, valorFalta, creadoPor FROM sanciones WHERE numeroSancion=?", tuplaDatos)				
		datos_nuevo = conector.fetchone()
		self.db.close()
		try:
			datos_nuevo = list(datos_nuevo)
			for i in range(len(datos_nuevo)):
				if datos_nuevo[i] == None:
					datos_nuevo[i] = " "
			pdf = GenerarPdf(datos_nuevo)
		except TypeError:
			pass
		except AttributeError:
			QtWidgets.QMessageBox.question(self, "Información", "No se ha generado alguna multa con este número:\n {}".format(x), QtWidgets.QMessageBox.Ok)
		
		try:
			
			multa = "Multas Generadas\\"+x+".pdf"
			os.startfile(multa, "print")
		
		except FileNotFoundError:
			QtWidgets.QMessageBox.question(self, "Información", "No se ha generado alguna multa con este número:\n {}".format(x), QtWidgets.QMessageBox.Ok)