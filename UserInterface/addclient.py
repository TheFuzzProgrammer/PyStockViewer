__author__ = "Fuzz"

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys


class ClientsUi(object):
    def __init__(self, dialog):
        self.label = QtWidgets.QLabel(dialog)
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_6 = QtWidgets.QLabel(dialog)
        self.clientName = QtWidgets.QLineEdit(dialog)
        self.clientSurname = QtWidgets.QLineEdit(dialog)
        self.docType = QtWidgets.QLineEdit(dialog)
        self.docNum = QtWidgets.QLineEdit(dialog)
        self.phoneNum = QtWidgets.QLineEdit(dialog)
        self.mailAddress = QtWidgets.QLineEdit(dialog)
        self.aceptar = QtWidgets.QPushButton(dialog)
        self.cancelar = QtWidgets.QPushButton(dialog)
        self.descuento = QtWidgets.QCheckBox(dialog)
        self.agregaDescuento = QtWidgets.QPushButton(dialog)

    def clients_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(400, 489)
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

        self.retranslateui(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Agregar cliente"))
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
    dialog = QtWidgets.QDialog()
    ui = ClientsUi(dialog)
    ui.clients_ui(dialog)
    return dialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = ClientsUi(dialog)
    ui.clients_ui(dialog)
    dialog.show()
    sys.exit(app.exec_())
