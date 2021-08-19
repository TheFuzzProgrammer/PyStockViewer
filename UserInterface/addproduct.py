__author__ = "Fuzz"

from PyQt5 import QtCore, QtGui, QtWidgets
from modules.objectMaker import *


class ProductsUi(object):
    def __init__(self, dialog):
        self.label = QtWidgets.QLabel(dialog)
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_6 = QtWidgets.QLabel(dialog)
        self.name = QtWidgets.QLineEdit(dialog)
        self.brand = QtWidgets.QLineEdit(dialog)
        self.expDate = QtWidgets.QLineEdit(dialog)
        self.lot = QtWidgets.QLineEdit(dialog)
        self.weight = QtWidgets.QLineEdit(dialog)
        self.quantity = QtWidgets.QLineEdit(dialog)
        self.aceptar = QtWidgets.QPushButton(dialog)
        self.cancelar = QtWidgets.QPushButton(dialog)
        self.code = QtWidgets.QLineEdit(dialog)
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_8 = QtWidgets.QLabel(dialog)
        self.price = QtWidgets.QLineEdit(dialog)
        self.isToxic = QtWidgets.QCheckBox(dialog)
        self.liquid = QtWidgets.QCheckBox(dialog)
        self.expires = QtWidgets.QCheckBox(dialog)
        self.isFood = QtWidgets.QCheckBox(dialog)

    def products_ui(self, product_dialog):
        product_dialog.setWindowIcon(QtGui.QIcon('media/icon.png'))
        product_dialog.setObjectName("Dialog")
        product_dialog.resize(402, 489)
        self.label.setGeometry(QtCore.QRect(60, 60, 81, 21))
        self.label.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(60, 80, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_2.setObjectName("label_2")
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 121, 21))
        self.label_3.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_3.setObjectName("label_3")
        self.label_4.setGeometry(QtCore.QRect(60, 190, 111, 16))
        self.label_4.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_4.setObjectName("label_4")
        self.label_5.setGeometry(QtCore.QRect(60, 220, 101, 16))
        self.label_5.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(60, 250, 111, 21))
        self.label_6.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_6.setObjectName("label_6")
        self.name.setGeometry(QtCore.QRect(240, 60, 113, 20))
        self.name.setObjectName("name")
        self.brand.setGeometry(QtCore.QRect(240, 90, 113, 20))
        self.brand.setObjectName("brand")
        self.expDate.setEnabled(False)
        self.expDate.setGeometry(QtCore.QRect(240, 160, 113, 20))
        self.expDate.setObjectName("expDate")
        self.lot.setGeometry(QtCore.QRect(240, 190, 113, 20))
        self.lot.setObjectName("lot")
        self.weight.setGeometry(QtCore.QRect(240, 220, 113, 20))
        self.weight.setObjectName("weight")
        self.quantity.setGeometry(QtCore.QRect(240, 250, 113, 20))
        self.quantity.setObjectName("quantity")
        self.aceptar.setGeometry(QtCore.QRect(230, 440, 75, 23))
        self.aceptar.setObjectName("aceptar")
        self.cancelar.setGeometry(QtCore.QRect(310, 440, 75, 23))
        self.cancelar.setObjectName("cancelar")
        self.code.setGeometry(QtCore.QRect(240, 280, 113, 20))
        self.code.setObjectName("code")
        self.label_7.setGeometry(QtCore.QRect(60, 310, 171, 21))
        self.label_7.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_7.setObjectName("label_7")
        self.label_8.setGeometry(QtCore.QRect(60, 280, 111, 16))
        self.label_8.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_8.setObjectName("label_8")
        self.price.setGeometry(QtCore.QRect(240, 310, 113, 20))
        self.price.setObjectName("price")
        self.isToxic.setGeometry(QtCore.QRect(60, 350, 161, 16))
        self.isToxic.setStyleSheet("font: 14pt \"Tempus Sans ITC\";\n""")
        self.isToxic.setObjectName("isToxic")
        self.liquid.setGeometry(QtCore.QRect(60, 380, 111, 17))
        self.liquid.setStyleSheet("font: 14pt \"Tempus Sans ITC\";\n""")
        self.liquid.setObjectName("liquid")
        self.expires.setGeometry(QtCore.QRect(60, 130, 70, 17))
        self.expires.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.expires.setObjectName("expires")
        self.isFood.setGeometry(QtCore.QRect(230, 350, 121, 16))
        self.isFood.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.isFood.setObjectName("isFood")
        self.retranslateui(product_dialog)
        QtCore.QMetaObject.connectSlotsByName(product_dialog)

    def retranslateui(self, product_dialog):
        _translate = QtCore.QCoreApplication.translate
        product_dialog.setWindowTitle(_translate("Dialog", "Agregar producto"))
        self.label.setText(_translate("Dialog", "Nombre:"))
        self.label_2.setText(_translate("Dialog", "Marca:"))
        self.label_3.setText(_translate("Dialog", "Vencimiento:"))
        self.label_4.setText(_translate("Dialog", "Lote:"))
        self.label_5.setText(_translate("Dialog", "Peso:"))
        self.label_6.setText(_translate("Dialog", "Cantidad:"))
        self.aceptar.setText(_translate("Dialog", "Aceptar"))
        self.cancelar.setText(_translate("Dialog", "Cancelar"))
        self.label_7.setText(_translate("Dialog", "Precio"))
        self.label_8.setText(_translate("Dialog", "Codigo:"))
        self.isToxic.setText(_translate("Dialog", "Es toxico"))
        self.liquid.setText(_translate("Dialog", "Es liquido"))
        self.expires.setText(_translate("Dialog", "Expira"))
        self.isFood.setText(_translate("Dialog", "Es comida"))

    def add_new(self):
        pass


def runapp_product():
    product_dialog = QtWidgets.QDialog()
    product_interface = ProductsUi(product_dialog)
    product_interface.products_ui(product_dialog)
    return product_dialog


if __name__ == "__main__":
    print("Product add GUI FOR StockViewer module by Fuzz\nThis module only can run from application")
else:
    pass
