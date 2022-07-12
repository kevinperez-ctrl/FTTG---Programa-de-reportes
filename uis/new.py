# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultas.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(771, 416)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setWhatsThis("")
        Dialog.setAccessibleDescription("")
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 5, 0, 1, 8)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setMaximum(300)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 3, 1, 1)
        self.boleteria = QtWidgets.QCheckBox(Dialog)
        self.boleteria.setObjectName("boleteria")
        self.gridLayout.addWidget(self.boleteria, 2, 4, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.pushButton_2.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Total de registros encontrados:"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.comboBox.setItemText(0, _translate("Dialog", "Cooperativa"))
        self.comboBox.setItemText(1, _translate("Dialog", "Cooperativa y Disco"))
        self.comboBox.setItemText(2, _translate("Dialog", "Fecha de emisión"))
        self.comboBox.setItemText(3, _translate("Dialog", "Número de Boleta"))
        self.comboBox.setItemText(4, _translate("Dialog", "Supervisor"))
        self.comboBox.setItemText(5, _translate("Dialog", "Usuario Registrado"))
        self.label.setText(_translate("Dialog", "Realizar busqueda por:"))
        self.label_2.setText(_translate("Dialog", "Cooperativa: "))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.boleteria.setText(_translate("Dialog", "Boletería"))

import recursos_rc
