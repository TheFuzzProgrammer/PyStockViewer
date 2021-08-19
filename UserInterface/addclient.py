__author__ = "Fuzz"

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from modules.dumper import *


class ClientsUi(object):
    def __init__(self, clients_dialog):
        self.label = QtWidgets.QLabel(clients_dialog)
        self.label_2 = QtWidgets.QLabel(clients_dialog)
        self.label_3 = QtWidgets.QLabel(clients_dialog)
        self.label_4 = QtWidgets.QLabel(clients_dialog)
        self.label_5 = QtWidgets.QLabel(clients_dialog)
        self.label_6 = QtWidgets.QLabel(clients_dialog)
        self.clientName = QtWidgets.QLineEdit(clients_dialog)
        self.clientSurname = QtWidgets.QLineEdit(clients_dialog)
        self.docType = QtWidgets.QLineEdit(clients_dialog)
        self.docNum = QtWidgets.QLineEdit(clients_dialog)
        self.phoneNum = QtWidgets.QLineEdit(clients_dialog)
        self.mailAddress = QtWidgets.QLineEdit(clients_dialog)
        self.aceptar = QtWidgets.QPushButton(clients_dialog)
        self.cancelar = QtWidgets.QPushButton(clients_dialog)
        self.descuento = QtWidgets.QCheckBox(clients_dialog)
        self.agregaDescuento = QtWidgets.QPushButton(clients_dialog)

    def clients_ui(self, clients_dialog):
        clients_dialog.setWindowIcon(QtGui.QIcon('media/icon.png'))
        clients_dialog.setObjectName("Dialog")
        clients_dialog.resize(400, 489)
        self.label.setGeometry(QtCore.QRect(60, 70, 81, 21))
        self.label.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label.setObjectName("label")
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(60, 90, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(QtCore.QRect(60, 150, 81, 21))
        self.label_3.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_3.setObjectName("label_3")
        self.label_4.setGeometry(QtCore.QRect(60, 180, 111, 16))
        self.label_4.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_4.setObjectName("label_4")
        self.label_5.setGeometry(QtCore.QRect(60, 230, 81, 16))
        self.label_5.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(60, 260, 61, 21))
        self.label_6.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_6.setObjectName("label_6")
        self.clientName.setGeometry(QtCore.QRect(220, 70, 113, 20))
        self.clientName.setObjectName("clientName")
        self.clientSurname.setGeometry(QtCore.QRect(220, 100, 113, 20))
        self.clientSurname.setObjectName("clientSurname")
        self.docType.setGeometry(QtCore.QRect(220, 150, 113, 20))
        self.docType.setObjectName("docType")
        self.docNum.setGeometry(QtCore.QRect(220, 180, 113, 20))
        self.docNum.setObjectName("docNum")
        self.phoneNum.setGeometry(QtCore.QRect(220, 230, 113, 20))
        self.phoneNum.setObjectName("phoneNum")
        self.mailAddress.setGeometry(QtCore.QRect(220, 260, 113, 20))
        self.mailAddress.setObjectName("mailAddress")
        self.aceptar.setGeometry(QtCore.QRect(230, 440, 75, 23))
        self.aceptar.setObjectName("aceptar")
        self.cancelar.setGeometry(QtCore.QRect(310, 440, 75, 23))
        self.cancelar.setObjectName("cancelar")
        self.descuento.setEnabled(True)
        self.descuento.setGeometry(QtCore.QRect(60, 320, 201, 17))
        self.descuento.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.descuento.setObjectName("descuento")
        self.agregaDescuento.setEnabled(False)
        self.agregaDescuento.setGeometry(QtCore.QRect(140, 370, 111, 23))
        self.agregaDescuento.setObjectName("agregaDescuento")
        self.retranslateui(clients_dialog)
        QtCore.QMetaObject.connectSlotsByName(clients_dialog)
        self.aceptar.clicked.connect(self.add_new)

    def add_new(self):
        print("elpepe")
        client = Client(0, 0, self.clientSurname.text(), self.clientName.text(), self.docType.text(),
                        self.docNum.text(), self.phoneNum.text(), self.mailAddress.text())
        dump_object(client)

    def retranslateui(self, clients_dialog):
        _translate = QtCore.QCoreApplication.translate
        clients_dialog.setWindowTitle(_translate("Dialog", "Agregar cliente"))
        self.label.setText(_translate("Dialog", "Nombre:"))
        self.label_2.setText(_translate("Dialog", "Apellido:"))
        self.label_3.setText(_translate("Dialog", "Tipo doc:"))
        self.label_4.setText(_translate("Dialog", "Numero Doc:"))
        self.label_5.setText(_translate("Dialog", "Telefono:"))
        self.label_6.setText(_translate("Dialog", "Email:"))
        self.aceptar.setText(_translate("Dialog", "Aceptar"))
        self.cancelar.setText(_translate("Dialog", "Cancelar"))
        self.descuento.setText(_translate("Dialog", "Tiene descuentos"))
        self.agregaDescuento.setText(_translate("Dialog", "Agregar descuento"))


def runapp_client():
    clients_dialog = QtWidgets.QDialog()
    user_interface = ClientsUi(clients_dialog)
    user_interface.clients_ui(clients_dialog)
    return clients_dialog


if __name__ == "__main__":
    print("Clients add GUI FOR StockViewer by Fuzz \nThis module only can run from application")
else:
    pass