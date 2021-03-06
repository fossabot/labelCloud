import sys

from PyQt5 import QtWidgets

from modules.control.controler import Controler
from modules.view.gui import GUI


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Setup Model-View-Control structure
    control = Controler()
    view = GUI(control)
    app.installEventFilter(view)

    view.show()

    sys.exit(app.exec_())
