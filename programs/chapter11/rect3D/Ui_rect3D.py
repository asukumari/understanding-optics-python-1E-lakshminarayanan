# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_rect3D.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(896, 617)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplwidget3D = MPL_WIDGET_3D(self.centralWidget)
        self.mplwidget3D.setObjectName("mplwidget3D")
        self.horizontalLayout.addWidget(self.mplwidget3D)
        MainWindow.setCentralWidget(self.centralWidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_lamda = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_lamda.setObjectName("label_lamda")
        self.verticalLayout.addWidget(self.label_lamda)
        self.SpinBox_lambda = QtWidgets.QSpinBox(self.dockWidgetContents_3)
        self.SpinBox_lambda.setMinimum(400)
        self.SpinBox_lambda.setMaximum(900)
        self.SpinBox_lambda.setSingleStep(10)
        self.SpinBox_lambda.setProperty("value", 560)
        self.SpinBox_lambda.setObjectName("SpinBox_lambda")
        self.verticalLayout.addWidget(self.SpinBox_lambda)
        self.slider_lambda = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_lambda.setMinimum(400)
        self.slider_lambda.setMaximum(900)
        self.slider_lambda.setSingleStep(10)
        self.slider_lambda.setProperty("value", 560)
        self.slider_lambda.setOrientation(QtCore.Qt.Horizontal)
        self.slider_lambda.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_lambda.setTickInterval(50)
        self.slider_lambda.setObjectName("slider_lambda")
        self.verticalLayout.addWidget(self.slider_lambda)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_b = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_b.setObjectName("label_b")
        self.verticalLayout.addWidget(self.label_b)
        self.SpinBox_b = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_b.setDecimals(1)
        self.SpinBox_b.setMinimum(0.1)
        self.SpinBox_b.setSingleStep(1.0)
        self.SpinBox_b.setProperty("value", 4.0)
        self.SpinBox_b.setObjectName("SpinBox_b")
        self.verticalLayout.addWidget(self.SpinBox_b)
        self.slider_b = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_b.setMinimum(1)
        self.slider_b.setMaximum(100)
        self.slider_b.setProperty("value", 4)
        self.slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.slider_b.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_b.setTickInterval(10)
        self.slider_b.setObjectName("slider_b")
        self.verticalLayout.addWidget(self.slider_b)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_h = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_h.setObjectName("label_h")
        self.verticalLayout.addWidget(self.label_h)
        self.SpinBox_h = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_h.setDecimals(1)
        self.SpinBox_h.setMinimum(0.1)
        self.SpinBox_h.setProperty("value", 4.0)
        self.SpinBox_h.setObjectName("SpinBox_h")
        self.verticalLayout.addWidget(self.SpinBox_h)
        self.slider_h = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_h.setMinimum(1)
        self.slider_h.setMaximum(100)
        self.slider_h.setProperty("value", 4)
        self.slider_h.setOrientation(QtCore.Qt.Horizontal)
        self.slider_h.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_h.setTickInterval(10)
        self.slider_h.setObjectName("slider_h")
        self.verticalLayout.addWidget(self.slider_h)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_a = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_a.setObjectName("label_a")
        self.verticalLayout.addWidget(self.label_a)
        self.SpinBox_a = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_a.setDecimals(1)
        self.SpinBox_a.setMinimum(0.1)
        self.SpinBox_a.setSingleStep(1.0)
        self.SpinBox_a.setProperty("value", 15.0)
        self.SpinBox_a.setObjectName("SpinBox_a")
        self.verticalLayout.addWidget(self.SpinBox_a)
        self.slider_a = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_a.setMinimum(1)
        self.slider_a.setMaximum(100)
        self.slider_a.setProperty("value", 15)
        self.slider_a.setOrientation(QtCore.Qt.Horizontal)
        self.slider_a.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_a.setTickInterval(10)
        self.slider_a.setObjectName("slider_a")
        self.verticalLayout.addWidget(self.slider_a)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_f2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_f2.setObjectName("label_f2")
        self.verticalLayout.addWidget(self.label_f2)
        self.SpinBox_f2 = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_f2.setDecimals(1)
        self.SpinBox_f2.setMinimum(0.1)
        self.SpinBox_f2.setMaximum(50.0)
        self.SpinBox_f2.setProperty("value", 2.0)
        self.SpinBox_f2.setObjectName("SpinBox_f2")
        self.verticalLayout.addWidget(self.SpinBox_f2)
        self.slider_f2 = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_f2.setMinimum(1)
        self.slider_f2.setMaximum(50)
        self.slider_f2.setProperty("value", 2)
        self.slider_f2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_f2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_f2.setTickInterval(10)
        self.slider_f2.setObjectName("slider_f2")
        self.verticalLayout.addWidget(self.slider_f2)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_dx = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.lineEdit_dx.setStyleSheet("color: rgb(0, 170, 0);")
        self.lineEdit_dx.setObjectName("lineEdit_dx")
        self.verticalLayout.addWidget(self.lineEdit_dx)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_dy = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.lineEdit_dy.setStyleSheet("color: rgb(0, 170, 0);")
        self.lineEdit_dy.setObjectName("lineEdit_dy")
        self.verticalLayout.addWidget(self.lineEdit_dy)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diffraction  Rectangular aperture"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Setting"))
        self.label_lamda.setText(_translate("MainWindow", "Wave length(10e-9 m)"))
        self.SpinBox_lambda.setStatusTip(_translate("MainWindow", "Change the wave length of monochromatic light"))
        self.slider_lambda.setStatusTip(_translate("MainWindow", "Change the wave length of monochromatic light"))
        self.label_b.setText(_translate("MainWindow", "b(10e-5 m)"))
        self.SpinBox_b.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.slider_b.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.label_h.setText(_translate("MainWindow", "h(10e-5 m)"))
        self.SpinBox_h.setStatusTip(_translate("MainWindow", "change the height of the recatangular aperture"))
        self.slider_h.setStatusTip(_translate("MainWindow", "change the height of the recatangular aperture"))
        self.label_a.setText(_translate("MainWindow", "a(10e-2 m)"))
        self.SpinBox_a.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.slider_a.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.label_f2.setText(_translate("MainWindow", "f2(m)"))
        self.SpinBox_f2.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))
        self.slider_f2.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#aa0000;\">central maximum: Δx(cm)</span></p></body></html>"))
        self.lineEdit_dx.setStatusTip(_translate("MainWindow", "The width of the central maximum along (Ox)"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#aa0000;\">central maximum: Δy(cm)</span></p></body></html>"))
        self.lineEdit_dy.setStatusTip(_translate("MainWindow", "The width of the central maximum along (Oy)"))

from mplwidget import MPL_WIDGET_3D
