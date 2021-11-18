__author__ = 'Fuzz'

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):

    def __init__(self, parent = None):

        QLineEdit.__init__(self, parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            event.accept()
        else:
            QLineEdit.keyPressEvent(self, event)


if __name__ == "__main__":
    pass