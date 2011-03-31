# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from sys import argv, path, exit as sys_exit
path.append('../lib/')

# Local modules:
from Interface import *

if __name__ == "__main__":
    app = QtGui.QApplication(argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys_exit(app.exec_())

