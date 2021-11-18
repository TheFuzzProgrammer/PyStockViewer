__Author__ = "Fuzz"

from UserInterface.setadmin import *
from UserInterface.addclient import *
from UserInterface.addproduct import *
from UserInterface.addpartner import *
from modules import Qtmods
from PyQt5 import QtGui


class CVMain(object):
    def __init__(self, mainui):
        self.centralwidget = QtWidgets.QWidget(mainui)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.soldTab = QtWidgets.QWidget()
        self.sold = QtWidgets.QPushButton(self.soldTab)
        self.soldnt = QtWidgets.QPushButton(self.soldTab)
        self.label = QtWidgets.QLabel(self.soldTab)
        self.productList = QtWidgets.QScrollArea(self.soldTab)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.label_3 = QtWidgets.QLabel(self.soldTab)
        self.label_2 = QtWidgets.QLabel(self.soldTab)
        self.lineEdit = Qtmods.LineEdit(self.soldTab)
        self.pushButton = QtWidgets.QPushButton(self.soldTab)
        self.radioButton = QtWidgets.QRadioButton(self.soldTab)
        self.radioButton_3 = QtWidgets.QRadioButton(self.soldTab)
        self.discount = QtWidgets.QDoubleSpinBox(self.soldTab)
        self.radioButton_2 = QtWidgets.QRadioButton(self.soldTab)
        self.stockTab = QtWidgets.QWidget()
        self.menubar = QtWidgets.QMenuBar(mainui)
        self.menuNuevo = QtWidgets.QMenu(self.menubar)
        self.menuVer = QtWidgets.QMenu(self.menubar)
        self.menuBuscar_venta = QtWidgets.QMenu(self.menuVer)
        self.menuEstadisticas = QtWidgets.QMenu(self.menuVer)
        self.menuMas_vendidos = QtWidgets.QMenu(self.menuEstadisticas)
        self.menuContabilidad = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainui)
        self.actionProducto = QtWidgets.QAction(mainui)
        self.actionEmpleado = QtWidgets.QAction(mainui)
        self.actionCliente = QtWidgets.QAction(mainui)
        self.actionAdministrador = QtWidgets.QAction(mainui)
        self.actionUltima_Venta = QtWidgets.QAction(mainui)
        self.actionPor_numero = QtWidgets.QAction(mainui)
        self.actionPor_fecha = QtWidgets.QAction(mainui)
        self.actionTotal = QtWidgets.QAction(mainui)
        self.actionCategor_a = QtWidgets.QAction(mainui)
        self.actionModificar_IVA = QtWidgets.QAction(mainui)
        self.actionEstadistica_de_vendedor = QtWidgets.QAction(mainui)
        self.actionGanancias_semanales = QtWidgets.QAction(mainui)
        self.actionReporte_mensual_global = QtWidgets.QAction(mainui)
        self.showClient = QtWidgets.QLabel(self.soldTab)
        self.client_dialog = runapp_client()
        self.partner_dialog = runapp_partners()
        self.product_dialog = runapp_product()
        self.set_admin = run_set_admin()
        self.client_cleared = False
        self.nameLabel = QtWidgets.QLabel(self.soldTab)
        self.sale = []
        self.client = None

    def setupui(self, mainui):
        mainui.setObjectName("MainWindow")
        mainui.resize(800, 600)
        mainui.setMinimumSize(QtCore.QSize(800, 600))
        mainui.setMaximumSize(QtCore.QSize(800, 600))
        mainui.setBaseSize(QtCore.QSize(800, 600))
        mainui.setStyleSheet("font: 10pt \"Segoe Print\";")
        mainui.setWindowIcon(QtGui.QIcon('media/icon.png'))
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget.setGeometry(QtCore.QRect(0, -10, 801, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.soldTab.setObjectName("soldTab")
        self.sold.setGeometry(QtCore.QRect(640, 460, 131, 21))
        self.sold.setObjectName("sold")
        self.soldnt.setGeometry(QtCore.QRect(480, 460, 131, 21))
        self.soldnt.setObjectName("soldnt")
        self.label.setGeometry(QtCore.QRect(480, 0, 201, 20))
        self.label.setObjectName("label")
        self.productList.setGeometry(QtCore.QRect(480, 30, 301, 351))
        self.productList.setWidgetResizable(True)
        self.productList.setObjectName("productList")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 299, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.productList.setWidget(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(480, 420, 141, 31))
        self.label_2.setStyleSheet("font: 20pt \"Tempus Sans ITC\";")
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(QtCore.QRect(480, 390, 71, 16))
        self.label_3.setObjectName("label_3")
        self.nameLabel.setGeometry(QtCore.QRect(40, 282, 300, 21))
        self.nameLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\" color:rgb(255, 0, 0);")
        self.nameLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.nameLabel.setObjectName("nameLabel")
        self.showClient.setGeometry(QtCore.QRect(10, 300, 441, 181))
        self.showClient.setStyleSheet("font: 10pt \"MS Shell Dlg 2\" color:rgb(255, 0, 0);")
        self.showClient.setStyleSheet("color: rgb(84, 135, 255);")
        self.showClient.setObjectName("showClient")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(40, 260, 161, 21))
        self.lineEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\" rgb(132, 132, 132);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(210, 260, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(40, 220, 151, 17))
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 20, 151, 17))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.discount.setEnabled(False)
        self.discount.setGeometry(QtCore.QRect(170, 60, 62, 22))
        self.discount.setObjectName("discount")
        self.radioButton_2.setGeometry(QtCore.QRect(60, 60, 111, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.tabWidget.addTab(self.soldTab, "")
        self.stockTab.setObjectName("stockTab")
        self.tabWidget.addTab(self.stockTab, "")
        mainui.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        self.menuNuevo.setObjectName("menuNuevo")
        self.menuVer.setObjectName("menuVer")
        self.menuBuscar_venta.setObjectName("menuBuscar_venta")
        self.menuEstadisticas.setObjectName("menuEstadisticas")
        self.menuMas_vendidos.setObjectName("menuMas_vendidos")
        self.menuContabilidad.setObjectName("menuContabilidad")
        mainui.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        mainui.setStatusBar(self.statusbar)
        self.actionProducto.setObjectName("actionProducto")
        self.actionEmpleado.setObjectName("actionEmpleado")
        self.actionAdministrador.setObjectName("actionAdministrador")
        self.actionUltima_Venta.setObjectName("actionUltima_Venta")
        self.actionPor_numero.setObjectName("actionPor_numero")
        self.actionPor_fecha.setObjectName("actionPor_fecha")
        self.actionTotal.setObjectName("actionTotal")
        self.actionCategor_a.setObjectName("actionCategor_a")
        self.actionModificar_IVA.setObjectName("actionModificar_IVA")
        self.actionEstadistica_de_vendedor.setObjectName("actionEstadistica_de_vendedor")
        self.actionGanancias_semanales.setObjectName("actionGanancias_semanales")
        self.actionReporte_mensual_global.setObjectName("actionReporte_mensual_global")
        self.menuNuevo.addAction(self.actionProducto)
        self.menuNuevo.addAction(self.actionEmpleado)
        self.menuNuevo.addAction(self.actionCliente)
        self.menuNuevo.addAction(self.actionAdministrador)
        self.menuBuscar_venta.addAction(self.actionPor_numero)
        self.menuBuscar_venta.addAction(self.actionPor_fecha)
        self.menuMas_vendidos.addAction(self.actionTotal)
        self.menuMas_vendidos.addAction(self.actionCategor_a)
        self.menuEstadisticas.addAction(self.menuMas_vendidos.menuAction())
        self.menuVer.addAction(self.actionUltima_Venta)
        self.menuVer.addAction(self.menuBuscar_venta.menuAction())
        self.menuVer.addAction(self.menuEstadisticas.menuAction())
        self.menuContabilidad.addAction(self.actionModificar_IVA)
        self.menuContabilidad.addAction(self.actionEstadistica_de_vendedor)
        self.menuContabilidad.addAction(self.actionGanancias_semanales)
        self.menuContabilidad.addAction(self.actionReporte_mensual_global)
        self.menubar.addAction(self.menuNuevo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuContabilidad.menuAction())
        self.pushButton.clicked.connect(self.search_client)
        self.translateui(mainui)
        self.tabWidget.setCurrentIndex(0)
        self.actionAdministrador.triggered.connect(self.set_partner_adimin)
        self.actionCliente.triggered.connect(self.add_client)
        self.actionEmpleado.triggered.connect(self.add_partner)
        self.actionProducto.triggered.connect(self.add_product)
        QtCore.QMetaObject.connectSlotsByName(mainui)
        self.radioButton.clicked.connect(self.is_client)
        self.radioButton_3.clicked.connect(self.not_client)
        self.radioButton_2.clicked.connect(self.has_discount)
        self.lineEdit.textEdited.connect(self.clear_client)
        self.sold.clicked.connect(self.new_sale)

    def new_sale(self):
        if self.radioButton_3.isChecked():
            print("CommonClient, no discount")
        elif self.radioButton_2.isChecked():
            print("CommonClient with discount")
        elif self.radioButton.isChecked():
            print("RegisteredClient")
        else:
            pass

    def clear_client(self):
        if not self.client_cleared:
            self.lineEdit.setText("")
            self.pushButton.setEnabled(True)
            self.client_cleared = True
            self.client = None
        else:
            pass

    def has_discount(self):
        self.discount.setEnabled(True)

    def search_client(self):
        client_number = None
        self.showClient.setText(" ")
        if self.lineEdit.text() == "":
            self.nameLabel.setText("Campo vacio!")
        else:
            try:
                client_number = int(self.lineEdit.text())
            except ValueError:
                self.nameLabel.setText("Wrong, must be a number!!!")
            finally:
                if client_number is None:
                    pass
                else:
                    self.client = get_object(self.lineEdit.text(), "Client")
                    if self.client is None:
                        self.nameLabel.setText("Client not found")
                    else:
                        self.nameLabel.setText("")
                        self.showClient.setText(self.client.show())
                    pass

    def is_client(self):
        self.radioButton_2.setEnabled(False)
        self.lineEdit.setEnabled(True)
        self.discount.setEnabled(False)
        self.client_cleared = False
        self.lineEdit.setText("Numero de cliente")

    def not_client(self):
        self.showClient.setText(" ")
        self.lineEdit.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.radioButton_2.setEnabled(True)
        self.clear_client()
        self.nameLabel.setText("  ")
        self.lineEdit.setText("Cliente común")

    def add_product(self):
        ui = ProductsUi(self.product_dialog)
        ui.products_ui(self.product_dialog)
        self.product_dialog.exec()

    def add_partner(self):
        user_interface = PartnersUi(self.partner_dialog)
        user_interface.partners_ui(self.partner_dialog)
        self.partner_dialog.exec()

    def add_client(self):
        user_interface = ClientsUi(self.client_dialog)
        user_interface.clients_ui(self.client_dialog)
        self.client_dialog.exec()

    def set_partner_adimin(self):
        user_interface = SetAdmin(self.client_dialog)
        user_interface.set_ui(self.client_dialog)
        self.set_admin.exec()

    def translateui(self, mainui):
        _translate = QtCore.QCoreApplication.translate
        mainui.setWindowTitle(_translate("MainWindow", "StockViewer"))
        self.sold.setText(_translate("MainWindow", "Realizar venta"))
        self.soldnt.setText(_translate("MainWindow", "Anular venta"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p "
                                                       "align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Productos confirmados"))
        self.label_2.setText(_translate("MainWindow", "TOTAL:"))
        self.label_3.setText(_translate("MainWindow", "Subtotal:"))
        self.lineEdit.setText(_translate("MainWindow", "Numero de cliente"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.radioButton.setText(_translate("MainWindow", "Cliente registrado"))
        self.radioButton_3.setText(_translate("MainWindow", "Cliente base"))
        self.radioButton_2.setText(_translate("MainWindow", "Descuento %"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.soldTab), _translate("MainWindow", "Venta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stockTab), _translate("MainWindow", "Stock"))
        self.menuNuevo.setTitle(_translate("MainWindow", "Nuevo"))
        self.menuVer.setTitle(_translate("MainWindow", "Ver"))
        self.menuBuscar_venta.setTitle(_translate("MainWindow", "Buscar venta"))
        self.menuEstadisticas.setTitle(_translate("MainWindow", "Estadisticas"))
        self.menuMas_vendidos.setTitle(_translate("MainWindow", "Mas vendidos"))
        self.menuContabilidad.setTitle(_translate("MainWindow", "Contabilidad"))
        self.actionProducto.setText(_translate("MainWindow", "Producto"))
        self.actionEmpleado.setText(_translate("MainWindow", "Empleado"))
        self.actionCliente.setText(_translate("MainWindow", "Cliente"))
        self.actionAdministrador.setText(_translate("MainWindow", "Administrador"))
        self.actionUltima_Venta.setText(_translate("MainWindow", "Ultima Venta"))
        self.actionPor_numero.setText(_translate("MainWindow", "Por numero"))
        self.actionPor_fecha.setText(_translate("MainWindow", "Por fecha"))
        self.actionTotal.setText(_translate("MainWindow", "Total"))
        self.actionCategor_a.setText(_translate("MainWindow", "Categoría"))
        self.actionModificar_IVA.setText(_translate("MainWindow", "Modificar IVA"))
        self.actionEstadistica_de_vendedor.setText(_translate("MainWindow", "Estadistica de vendedor"))
        self.actionGanancias_semanales.setText(_translate("MainWindow", "Ganancias semanales"))
        self.actionReporte_mensual_global.setText(_translate("MainWindow", "Reporte mensual global"))


def start_ui(style):
    import sys
    application = QtWidgets.QApplication(sys.argv)
    application.setStyleSheet(style)
    main_ui = QtWidgets.QMainWindow()
    user_interface = CVMain(main_ui)
    user_interface.setupui(main_ui)
    main_ui.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    print("GUI FOR StockViewer by Fuzz \nThis module only can run from application")
else:
    pass
