# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\admin\Documents\works\camera\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(302, 128)
        self.btn_submit = QtWidgets.QDialogButtonBox(LoginWindow)
        self.btn_submit.setGeometry(QtCore.QRect(120, 90, 171, 32))
        self.btn_submit.setOrientation(QtCore.Qt.Horizontal)
        self.btn_submit.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_submit.setObjectName("btn_submit")
        self.label = QtWidgets.QLabel(LoginWindow)
        self.label.setGeometry(QtCore.QRect(40, 30, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 31, 16))
        self.label_2.setObjectName("label_2")
        self.box_name = QtWidgets.QLineEdit(LoginWindow)
        self.box_name.setGeometry(QtCore.QRect(80, 30, 181, 20))
        self.box_name.setInputMask("")
        self.box_name.setObjectName("box_name")
        self.box_password = QtWidgets.QLineEdit(LoginWindow)
        self.box_password.setGeometry(QtCore.QRect(80, 60, 181, 20))
        self.box_password.setInputMask("")
        self.box_password.setObjectName("box_password")

        self.retranslateUi(LoginWindow)
        self.btn_submit.accepted.connect(LoginWindow.accept)
        self.btn_submit.rejected.connect(LoginWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "登录"))
        self.label.setText(_translate("LoginWindow", "用户名"))
        self.label_2.setText(_translate("LoginWindow", "密码"))
        self.box_name.setPlaceholderText(_translate("LoginWindow", "必填项"))
        self.box_password.setPlaceholderText(_translate("LoginWindow", "必填项"))

