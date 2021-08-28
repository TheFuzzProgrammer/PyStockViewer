__author__ = "Fuzz"

from PyQt5 import QtCore, QtGui, QtWidgets


class SetAdmin(object):
    def __init__(self, dialog):
        self.label = QtWidgets.QLabel(dialog)
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_4 = QtWidgets.QLabel(dialog)
        self.partner_name = QtWidgets.QLineEdit(dialog)
        self.partner_surname = QtWidgets.QLineEdit(dialog)
        self.partner_code = QtWidgets.QLineEdit(dialog)
        self.partner_doc = QtWidgets.QLineEdit(dialog)
        self.aceptar = QtWidgets.QPushButton(dialog)
        self.anular = QtWidgets.QPushButton(dialog)
        self.image_label = QtWidgets.QLabel(dialog)
        self.partner_info = QtWidgets.QLabel(dialog)

    def set_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.setWindowIcon(QtGui.QIcon('media/icon.png'))
        dialog.resize(402, 489)
        # dialog.setStyleSheet("")
        self.label.setGeometry(QtCore.QRect(60, 100, 81, 21))
        self.label.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(60, 120, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(QtCore.QRect(60, 160, 81, 21))
        self.label_3.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_3.setObjectName("label_3")
        self.label_4.setGeometry(QtCore.QRect(60, 190, 111, 21))
        self.label_4.setStyleSheet("font: 14pt \"Tempus Sans ITC\";")
        self.label_4.setObjectName("label_4")
        self.partner_name.setGeometry(QtCore.QRect(240, 100, 113, 20))
        self.partner_name.setObjectName("partner_name")
        self.partner_surname.setGeometry(QtCore.QRect(240, 130, 113, 20))
        self.partner_surname.setObjectName("partner_surname")
        self.partner_code.setGeometry(QtCore.QRect(240, 160, 113, 20))
        self.partner_code.setText("")
        self.partner_code.setObjectName("partner_code")
        self.partner_doc.setGeometry(QtCore.QRect(240, 190, 113, 20))
        self.partner_doc.setObjectName("partner_doc")
        self.aceptar.setGeometry(QtCore.QRect(230, 440, 75, 23))
        self.aceptar.setObjectName("aceptar")
        self.anular.setGeometry(QtCore.QRect(310, 440, 75, 23))
        self.anular.setObjectName("anular")
        self.image_label.setGeometry(QtCore.QRect(0, 0, 401, 91))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.partner_info.setGeometry(QtCore.QRect(0, 230, 401, 181))
        self.partner_info.setText("")
        self.partner_info.setObjectName("partner_info")
        self.translate_ui(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def translate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Asignar ADMINISTRADOR"))
        self.label.setText(_translate("Dialog", "Nombre"))
        self.label_2.setText(_translate("Dialog", "Apellido:"))
        self.label_3.setText(_translate("Dialog", "Codigo"))
        self.label_4.setText(_translate("Dialog", "Numero Doc:"))
        self.aceptar.setText(_translate("Dialog", "Aceptar"))
        self.anular.setText(_translate("Dialog", "Anular"))


def run_set_admin():
    admin_dialog = QtWidgets.QDialog()
    partners_interface = SetAdmin(admin_dialog)
    partners_interface.set_ui(admin_dialog)
    return admin_dialog
