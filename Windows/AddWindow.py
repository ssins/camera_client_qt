from Windows.Communicate import Communicate
from db_requests import DB_Requsets
from Camera import Camera
from Models.Ui_add import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class AddWindow(QMainWindow, Ui_AddWindow):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.setupUi(self)
        self.c = Communicate()
        self.dbr = DB_Requsets()
        self.btnCheck()

        self.box_name.textChanged.connect(self.btnCheck)
        self.box_sn.textChanged.connect(self.btnCheck)
        self.box_address.textChanged.connect(self.btnCheck)
        self.box_user_name.textChanged.connect(self.btnCheck)
        self.box_password.textChanged.connect(self.btnCheck)

    def btnCheck(self):
        if self.box_name.text() and self.box_sn.text() and self.box_address.text() and self.box_user_name.text() and self.box_password.text():
            self.btn_submit.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.btn_submit.button(QDialogButtonBox.Ok).setEnabled(False)

    def clear(self):
        self.box_action_type.setCurrentIndex(0)
        self.box_kind.setCurrentIndex(-1)
        self.box_address.setText('')
        self.box_brand.setText('')
        self.box_model.setText('')
        self.box_name.setText('')
        self.box_password.setText('')
        self.box_sn.setText('')
        self.box_user_name.setText('')

    def accept(self):
        camera = Camera(self.box_sn.text(),
                        self.box_address.text(),
                        self.box_action_type.currentIndex(),
                        self.box_user_name.text(),
                        self.box_password.text(),
                        None,
                        self.box_kind.currentText(),
                        self.box_brand.text(),
                        self.box_model.text(),
                        self.box_name.text())
        self.dbr.add_camera(camera)
        self.clear()
        self.c.add_camera_signal.emit()

    def reject(self):
        self.clear()
