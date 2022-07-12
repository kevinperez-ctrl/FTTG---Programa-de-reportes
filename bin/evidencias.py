import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QByteArray, QIODevice, QBuffer
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit)
import bin.src.recursos_rc
from sqlite3 import *
import cv2

class VerEvidencias(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("bin/img/favico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(self.icon)
		self.resize(936, 684)
		self.frame = QtWidgets.QFrame(self)
		self.frame.setGeometry(QtCore.QRect(10, 10, 911, 91))
		self.frame.setFrameShape(QtWidgets.QFrame.Panel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(20, 10, 236, 18))
		self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
		self.label_2 = QtWidgets.QLabel(self.frame)
		self.label_2.setGeometry(QtCore.QRect(230, 10, 69, 20))
		self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.lineEdit = QtWidgets.QLineEdit(self.frame)
		self.lineEdit.setGeometry(QtCore.QRect(310, 10, 230, 20))
		self.pushButton = QtWidgets.QPushButton(self.frame)
		self.pushButton.setGeometry(QtCore.QRect(550, 10, 141, 24))
		self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.pushButton2 = QtWidgets.QPushButton(self.frame)
		self.pushButton2.setGeometry(QtCore.QRect(690, 10, 141, 24))
		self.pushButton2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
		self.pushButton2.setText("Salir")
	
		self.pushButton.setAutoDefault(True)
		self.scrollArea = QtWidgets.QScrollArea(self)
		self.scrollArea.setGeometry(QtCore.QRect(10, 50, 911, 631))
		self.imagenLabel = QtWidgets.QLabel()
		self.imagenLabel.setGeometry(QtCore.QRect(10, 10, 891, 611))
		self.imagenLabel.setText("")
		self.scrollArea.setWidget(self.imagenLabel)

		QtCore.QMetaObject.connectSlotsByName(self)

		self.setWindowTitle("Ver Evidencias")
		self.label.setText("Ingrese el número de sanción:")
		self.label_2.setText("FTTG-TTMP")
		self.imagenLabel.setToolTip("Presione ESC para salir.")
		self.pushButton.setText("Ver")
		
		self.pushButton.clicked.connect(self.verEvidencia)
		self.pushButton2.clicked.connect(self.close)

		
	def verEvidencia(self):
		db = connect("bin/src/secs.db")
		conector = db.cursor()
		coope = "FTTG-TTMP-"+self.lineEdit.text()
		tuplaDatos = (coope,)
		conector.execute("SELECT evidencia FROM sanciones WHERE numeroSancion=?", tuplaDatos)
		resultado = conector.fetchall()
		if resultado:
			# Cargar foto a un QPixmap
			foto = QPixmap()
			foto.loadFromData(resultado[0][0], "PNG", Qt.AutoColor)
			
			# Insertar foto en el QLabel
			self.imagenLabel.setPixmap(foto)
			self.imagenLabel.setGeometry(QtCore.QRect(10, 10, foto.width(),foto.height()))
			
		else:
			self.imagenLabel.clear()
				
		db.close()
		
	def borrar(self):
		self.lineEdit.clear()
		self.imagenLabel.clear()
		
		