from Windows.Communicate import Communicate
from db_requests import DB_Requsets
from Models.Ui_login import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.c = Communicate()
        self.dbr = DB_Requsets()

    def accept(self):
        token = self.dbr.login(self.box_name.text(),self.box_password.text())
        if token:
            self.c.login_signal.emit(token)
            self.close()
        else:
            self.box_name.setText('')
            self.box_password.setText('')
            self.box_name.setPlaceholderText('登录失败')

    def reject(self):
        self.close()