import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel, QMessageBox
import bin.src.recursos_rc
from sqlite3 import *
from pickle import *

class ConfigYear(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.resize(275, 181)
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.label = QtWidgets.QLabel(self)
		self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.lineEdit = QtWidgets.QLineEdit(self)
		self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
		self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

		QtCore.QMetaObject.connectSlotsByName(self)

		self.setWindowTitle("Modificar Año")
		self.label.setText("Ingrese el nuevo año:")
		self.pushButton.setText("Guardar")
		self.label_2.setText("<html><head/><body><p align=\"center\">Todas las sanciones saldrán </p><p align=\"center\">con el nuevo año ingresado.</p></body></html>")
		
		self.pushButton.clicked.connect(self.generar)
		
	def generar(self):		
		box = QMessageBox(self)
		box.setWindowTitle('Cambiar el año') 
		box.setText("¿Acepta guardar los cambios y generar la nueva base de datos?")
		box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		botonSi = box.button(QMessageBox.Yes)
		botonSi.setText("Si")
		box.exec_()
		if box.clickedButton() == botonSi:
			db = connect("bin/src/secs.db")
			try:
				x = open("bin/src/year.bin", "wb")
				dump(self.lineEdit.text(), x)
				x.close()
				year_anterior = int(self.lineEdit.text())
				year_anterior = year_anterior-1
				self.lineEdit.clear()
			except ValueError:
				print("Solo se puede ingresar numeros")
			conector = db.cursor()
			
			try:
				conector.execute("CREATE TABLE sanciones{} (numero integer unique, numeroSancion text, cooperativa text, disco text, fecha text, hora text, articulo text, literal text, descript text, tipoFalta text, valorFalta text, creadoPor text, ingresadoPor text, modificadoPor text, fechaModif text, evidencia BLOB, links text)".format(year_anterior))
				db.commit()
				conector.execute("INSERT INTO sanciones{} SELECT * FROM sanciones".format(year_anterior))
				db.commit()
				conector.execute("DROP TABLE sanciones")
				db.commit()
				conector.execute("CREATE TABLE sanciones (numero INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, numeroSancion text unique, cooperativa text, disco text, fecha text, hora text, articulo text, literal text, descript text, tipoFalta text, valorFalta text, creadoPor text, ingresadoPor text, modificadoPor text, fechaModif text, evidencia BLOB, links text)")
				db.commit()
				
			except OperationalError:
				QMessageBox.critical(self, "Error", "Ya existe una tabla para el año ingresado.", QMessageBox.Ok)
			
				
			