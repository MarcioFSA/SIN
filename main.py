from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from view.principal import Ui_MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setWindowIcon(QtGui.QIcon('Logo.png'))
    ui = Ui_MainWindow()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec())

