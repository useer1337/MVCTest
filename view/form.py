# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovalalexander/PycharmProjects/ExampleMVC/view/form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 104)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(8, 10, 325, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_c = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_c.setObjectName("lineEdit_c")
        self.horizontalLayout.addWidget(self.lineEdit_c)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_d = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.horizontalLayout.addWidget(self.lineEdit_d)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_equels = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_equels.setObjectName("lineEdit_equels")
        self.horizontalLayout.addWidget(self.lineEdit_equels)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 321, 27))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_result = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_result.setObjectName("pushButton_result")
        self.verticalLayout.addWidget(self.pushButton_result)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "="))
        self.pushButton_result.setText(_translate("MainWindow", "PushButton"))
