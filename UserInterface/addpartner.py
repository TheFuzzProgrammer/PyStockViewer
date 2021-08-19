__Author__ = "Fuzz"

from PyQt5 import QtCore, QtGui, QtWidgets
from modules.dumper import *


class PartnersUi(object):
    def __init__(self, partners_dialog):
        self.label = QtWidgets.QLabel(partners_dialog)
        self.label_2 = QtWidgets.QLabel(partners_dialog)
        self.label_3 = QtWidgets.QLabel(partners_dialog)
        self.label_4 = QtWidgets.QLabel(partners_dialog)
        self.label_5 = QtWidgets.QLabel(partners_dialog)
        self.label_6 = QtWidgets.QLabel(partners_dialog)
        self.clientName = QtWidgets.QLineEdit(partners_dialog)
        self.clientSurname = QtWidgets.QLineEdit(partners_dialog)
        self.docType = QtWidgets.QLineEdit(partners_dialog)
        self.docNum = QtWidgets.QLineEdit(partners_dialog)
        self.phoneNum = QtWidgets.QLineEdit(partners_dialog)
        self.mailAddress = QtWidgets.QLineEdit(partners_dialog)
        self.aceptar = QtWidgets.QPushButton(partners_dialog)
        self.cancelar = QtWidgets.QPushButton(partners_dialog)
        self.passWord = QtWidgets.QLineEdit(partners_dialog)
        self.label_7 = QtWidgets.QLabel(partners_dialog)
        self.label_8 = QtWidgets.QLabel(partners_dialog)
        self.dateBirth = QtWidgets.QLineEdit(partners_dialog)

    def partners_ui(self, partners_dialog):
        partners_dialog.setWindowIcon(QtGui.QIcon('media/icon.png'))
        partners_dialog.setObjectName("Dialog")
        partners_dialog.resize(402, 489)
        self.label.setGeometry(QtCore.QRect(60, 100, 81, 21))
        self.label.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(60, 120, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(QtCore.QRect(60, 160, 81, 21))
        self.label_3.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_3.setObjectName("label_3")
        self.label_4.setGeometry(QtCore.QRect(60, 190, 111, 16))
        self.label_4.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_4.setObjectName("label_4")
        self.label_5.setGeometry(QtCore.QRect(60, 220, 81, 16))
        self.label_5.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(60, 250, 61, 21))
        self.label_6.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_6.setObjectName("label_6")
        self.clientName.setGeometry(QtCore.QRect(240, 100, 113, 20))
        self.clientName.setObjectName("clientName")
        self.clientSurname.setGeometry(QtCore.QRect(240, 130, 113, 20))
        self.clientSurname.setObjectName("clientSurname")
        self.docType.setGeometry(QtCore.QRect(240, 160, 113, 20))
        self.docType.setObjectName("docType")
        self.docNum.setGeometry(QtCore.QRect(240, 190, 113, 20))
        self.docNum.setObjectName("docNum")
        self.phoneNum.setGeometry(QtCore.QRect(240, 220, 113, 20))
        self.phoneNum.setObjectName("phoneNum")
        self.mailAddress.setGeometry(QtCore.QRect(240, 250, 113, 20))
        self.mailAddress.setObjectName("mailAddress")
        self.aceptar.setGeometry(QtCore.QRect(230, 440, 75, 23))
        self.aceptar.setObjectName("aceptar")
        self.cancelar.setGeometry(QtCore.QRect(310, 440, 75, 23))
        self.cancelar.setObjectName("cancelar")
        self.passWord.setGeometry(QtCore.QRect(240, 280, 113, 20))
        self.passWord.setObjectName("passWord")
        self.label_7.setGeometry(QtCore.QRect(60, 310, 171, 21))
        self.label_7.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_7.setObjectName("label_7")
        self.label_8.setGeometry(QtCore.QRect(60, 280, 111, 16))
        self.label_8.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_8.setObjectName("label_8")
        self.dateBirth.setGeometry(QtCore.QRect(240, 310, 113, 20))
        self.dateBirth.setObjectName("dateBirth")
        self.retranslate_ui(partners_dialog)
        QtCore.QMetaObject.connectSlotsByName(partners_dialog)
        self.aceptar.clicked.connect(self.add_new)

    def add_new(self):
        client = Employed(0, 0, self.clientSurname.text(), self.clientName.text(), self.docType.text(),
                          self.docNum.text(), self.phoneNum.text(), self.mailAddress.text())
        dump_object(client)

    def retranslate_ui(self, partners_dialog):
        _translate = QtCore.QCoreApplication.translate
        partners_dialog.setWindowTitle(_translate("Dialog", "Agregar empleado"))
        self.label.setText(_translate("Dialog", "Nombre:"))
        self.label_2.setText(_translate("Dialog", "Apellido:"))
        self.label_3.setText(_translate("Dialog", "Tipo doc:"))
        self.label_4.setText(_translate("Dialog", "Numero Doc:"))
        self.label_5.setText(_translate("Dialog", "Telefono:"))
        self.label_6.setText(_translate("Dialog", "Email:"))
        self.aceptar.setText(_translate("Dialog", "Aceptar"))
        self.cancelar.setText(_translate("Dialog", "Cancelar"))
        self.label_7.setText(_translate("Dialog", "Fecha de nacimiento:"))
        self.label_8.setText(_translate("Dialog", "Contraseña:"))


def runapp_partners():
    partners_dialog = QtWidgets.QDialog()
    partners_interface = PartnersUi(partners_dialog)
    partners_interface.partners_ui(partners_dialog)
    return partners_dialog
