# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 340)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(512, 512))
        MainWindow.setStyleSheet("QPushButton, QComboBox {\n"
"    background-color: #03F003;\n"
"    color: black;\n"
"    \n"
"    \n"
"}\n"
"\n"
"menubar, toolbar {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #white\n"
"    background: #011001;\n"
"    font: bold 14px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(110, 20, 141, 41))
        self.select_button.setObjectName("select_button")
        self.analyze_button = QtWidgets.QPushButton(self.centralwidget)
        self.analyze_button.setGeometry(QtCore.QRect(130, 230, 101, 41))
        self.analyze_button.setObjectName("analyze_button")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 130, 141, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 91, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setGeometry(QtCore.QRect(10, 70, 291, 51))
        self.path_label.setWordWrap(True)
        self.path_label.setObjectName("path_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CheckI"))
        self.select_button.setText(_translate("MainWindow", "Select File.."))
        self.analyze_button.setText(_translate("MainWindow", "Analyze"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Breast Cancer"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pneumonia"))
        self.label.setText(_translate("MainWindow", "Analyze for"))
        self.path_label.setText(_translate("MainWindow", "File: "))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
