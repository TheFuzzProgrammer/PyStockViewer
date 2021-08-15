import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('UserInterface/main.ui', self)
        self.setWindowIcon(QtGui.QIcon('media/icon.png'))
        self.setWindowTitle("Stock viewer")


def start():
    app = QApplication(sys.argv)
    _window = Window()
    _window.show()
    app.exec_()


if __name__ == "__main__":
    print("GUI FOR StockViewer by Fuzz \nThis module only can run from application")
else:
    pass
