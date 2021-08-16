__author__ = "Fuzz"

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


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

    def clients_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(400, 489)
        self.label.setGeometry(QtCore.QRect(20, 100, 41, 21))
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(20, 120, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(QtCore.QRect(20, 150, 41, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5.setGeometry(QtCore.QRect(20, 210, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(20, 240, 47, 13))
        self.label_6.setObjectName("label_6")
        self.clientName.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.clientName.setObjectName("clientName")
        self.clientSurname.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.clientSurname.setObjectName("clientSurname")
        self.docType.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.docType.setObjectName("docType")
        self.docNum.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.docNum.setObjectName("docNum")
        self.phoneNum.setGeometry(QtCore.QRect(120, 210, 113, 20))
        self.phoneNum.setObjectName("phoneNum")
        self.mailAddress.setGeometry(QtCore.QRect(120, 230, 113, 20))
        self.mailAddress.setObjectName("mailAddress")
        self.aceptar.setGeometry(QtCore.QRect(310, 450, 75, 23))
        self.aceptar.setObjectName("aceptar")
        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Agregar cliente"))
        self.label.setText(_translate("Dialog", "Nombre"))
        self.label_2.setText(_translate("Dialog", "Apellido"))
        self.label_3.setText(_translate("Dialog", "Tipo doc"))
        self.label_4.setText(_translate("Dialog", "Numero Doc"))
        self.label_5.setText(_translate("Dialog", "Telefono"))
        self.label_6.setText(_translate("Dialog", "Email"))
        self.aceptar.setText(_translate("Dialog", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = ClientsUi(dialog)
    ui.clients_ui(dialog)
    dialog.show()
    sys.exit(app.exec_())
