# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

# Local modules:
import DXFTableCreator as tabcreator
import DXFSections as dxfsecs

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        #Dialog.setObjectName("Dialog")
        Dialog.resize                     (400, 200)
        Dialog.setMinimumSize(QtCore.QSize(400, 200))
        Dialog.setMaximumSize(QtCore.QSize(400, 200))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/cad.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        # Text Label -> Maybe unnecessary
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(15, 5, 350, 90))
        self.label.setMouseTracking(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        # Cancel button
        self.button_Cancel = QtGui.QPushButton(Dialog)
        self.button_Cancel.setGeometry(QtCore.QRect(205, 110, 185, 80))
        self.button_Cancel.setObjectName("button_Cancelar")

        # Convert button
        self.button_Convert = QtGui.QPushButton(Dialog)
        self.button_Convert.setGeometry(QtCore.QRect(10, 110, 185, 80))
        self.button_Convert.setObjectName("button_OK")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.button_Cancel, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        QtCore.QObject.connect(self.button_Convert,QtCore.SIGNAL("clicked()"), self.choose_file)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog",
        "DXF2TXT Converter", None, QtGui.QApplication.UnicodeUTF8))

        self.label.setText(QtGui.QApplication.translate("Dialog",
        "Clique \"Converter\" e escolha o arquivo DXF a ser convertido para TXT.\
        \n\nClique \"Cancelar\" para sair do programa.",
        None, QtGui.QApplication.UnicodeUTF8))

        self.button_Cancel.setText(QtGui.QApplication.translate("Dialog",
        "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

        self.button_Convert.setText(QtGui.QApplication.translate("Dialog",
        "Converter", None, QtGui.QApplication.UnicodeUTF8))

    def choose_file(self):
        self.filePath = QtGui.QFileDialog.getOpenFileName(None, 'Open file','.','DXF File (*.dxf)')
        if self.filePath:
            self.myDxfFile = open(str(self.filePath.toUtf8()),'r')
            self.convert()


    def convert(self):
            EntitiesList = dxfsecs.ENTITIES(self.myDxfFile)
            MyTab = tabcreator.TextTable(EntitiesList.subSections['TEXT'])
            MyTab.printto(self.myDxfFile.name)



