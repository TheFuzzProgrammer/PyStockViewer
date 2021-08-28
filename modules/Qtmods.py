import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QApplication


class LineEdit(QLineEdit):

    def __init__(self, parent = None):

        QLineEdit.__init__(self, parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            print("Tab")

            event.accept()
        else:
            QLineEdit.keyPressEvent(self, event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = LineEdit()
    window.show()
    sys.exit(app.exec_())