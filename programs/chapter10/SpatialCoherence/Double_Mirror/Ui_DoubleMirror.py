# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DoubleMirror.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 600)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SpinBox_D3 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D3.setSuffix("")
        self.SpinBox_D3.setDecimals(3)
        self.SpinBox_D3.setMaximum(1.0)
        self.SpinBox_D3.setSingleStep(0.005)
        self.SpinBox_D3.setProperty("value", 0.13)
        self.SpinBox_D3.setObjectName("SpinBox_D3")
        self.gridLayout_2.addWidget(self.SpinBox_D3, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.SpinBox_D1 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D1.setSuffix("")
        self.SpinBox_D1.setDecimals(3)
        self.SpinBox_D1.setMinimum(0.0)
        self.SpinBox_D1.setMaximum(1.0)
        self.SpinBox_D1.setSingleStep(0.005)
        self.SpinBox_D1.setProperty("value", 0.0)
        self.SpinBox_D1.setObjectName("SpinBox_D1")
        self.gridLayout_2.addWidget(self.SpinBox_D1, 0, 2, 1, 1)
        self.SpinBox_D2 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D2.setDecimals(3)
        self.SpinBox_D2.setMaximum(1.0)
        self.SpinBox_D2.setSingleStep(0.005)
        self.SpinBox_D2.setProperty("value", 0.09)
        self.SpinBox_D2.setObjectName("SpinBox_D2")
        self.gridLayout_2.addWidget(self.SpinBox_D2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 6, 1, 1)
        self.SpinBox_Lambda = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda.setMinimum(200.0)
        self.SpinBox_Lambda.setMaximum(1000.0)
        self.SpinBox_Lambda.setProperty("value", 550.0)
        self.SpinBox_Lambda.setObjectName("SpinBox_Lambda")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda, 0, 7, 1, 1)
        self.SpinBox_D = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D.setDecimals(3)
        self.SpinBox_D.setMaximum(10.0)
        self.SpinBox_D.setSingleStep(0.01)
        self.SpinBox_D.setProperty("value", 1.0)
        self.SpinBox_D.setObjectName("SpinBox_D")
        self.gridLayout_2.addWidget(self.SpinBox_D, 1, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 9, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 9, 1, 1)
        self.lineEdit_D1 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_D1.setObjectName("lineEdit_D1")
        self.gridLayout_2.addWidget(self.lineEdit_D1, 0, 10, 1, 1)
        self.lineEdit_D2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_D2.setObjectName("lineEdit_D2")
        self.gridLayout_2.addWidget(self.lineEdit_D2, 1, 10, 1, 1)
        self.lineEdit_D3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_D3.setObjectName("lineEdit_D3")
        self.gridLayout_2.addWidget(self.lineEdit_D3, 2, 10, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 8, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 11, 1, 1)
        self.SpinBox_a = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_a.setDecimals(3)
        self.SpinBox_a.setMaximum(10.0)
        self.SpinBox_a.setSingleStep(0.005)
        self.SpinBox_a.setProperty("value", 1.0)
        self.SpinBox_a.setObjectName("SpinBox_a")
        self.gridLayout_2.addWidget(self.SpinBox_a, 2, 7, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 9, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplwidget = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.mplwidget.setObjectName("mplwidget")
        self.verticalLayout.addWidget(self.mplwidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DoubleMirror"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Distance source 1 (mm)</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Screen distance D(m)"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Distance source 2 (mm)</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Distance source 3 (mm)"))
        self.label_7.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#e90803;\">Contraste 1</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#f3070b;\">Contraste 3</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Mirrors distance a(mm)"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ed090b;\">Contraste 2</span></p></body></html>"))

from mplwidget import MPL_WIDGET_2D
