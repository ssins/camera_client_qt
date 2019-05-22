from Ui_camera import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from video import Video
from Windows.LoginWindow import LoginWindow
from Windows.AddWindow import AddWindow
from db_requests import DB_Requsets
from Camera import Camera
from video import Video


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.dbr = DB_Requsets()
        self.cameras = []

        self.slm = QStringListModel()
        self.select_list_multi = []
        self.show_selected_list()
        self.select_camera = None

        self.list_camera.clicked.connect(self.camera_info)
        #self.list_camera.doubleClicked.connect(self.camera_select)
        self.menu_add.triggered.connect(self.set_add)
        self.menu_login.triggered.connect(self.login)
        self.tab_action.currentChanged.connect(self.show_selected_list)
        self.btn_rtmp1.clicked.connect(self.show_rtmp1)
        self.btn_rtmp2.clicked.connect(self.show_rtmp2)

    def login(self):
        if self.dbr.token:
            self.dbr.logout()
            self.menu_login.setText('登录')
        else:
            loginWindow = LoginWindow(self)
            loginWindow.c.login_signal.connect(self.login_callback)
            loginWindow.show()

    def login_callback(self, token):
        self.dbr.token = token
        self.menu_login.setText('登出')
        self.cameras = self.dbr.get_camera_list()
        self.select_list_multi = [False] * len(self.cameras)
        self.show_selected_list()

    def set_add(self):
        if self.dbr.token:
            addWindow = AddWindow(self)
            addWindow.dbr.token = self.dbr.token
            addWindow.c.add_camera_signal.connect(self.add_camera_callback)
            addWindow.show()
            return
        self.login()
    
    def add_camera_callback(self):
        self.cameras = self.dbr.get_camera_list()
        self.select_list_multi = [False] * len(self.cameras)
        self.show_selected_list()

    def camera_info(self, idx):
        self.select_camera = self.cameras[self.list_camera.currentIndex(
        ).row()]
        self.box_sn.setText(self.select_camera.sn)
        self.box_address.setText(self.select_camera.address)
        self.box_brand.setText(self.select_camera.brand)
        self.box_model.setText(self.select_camera.model)
        self.box_name.setText(self.select_camera.name)
        self.box_password.setText(self.select_camera.password)
        self.box_user_name.setText(self.select_camera.user_name)
        self.box_action_type.setText(self.select_camera.action_type)
        self.box_kind.setText(self.select_camera.kind)
        self.camera_select(idx)

    def camera_select(self, idx):
        if self.tab_action.currentIndex():
            self.select_list_multi[idx.row(
            )] = not self.select_list_multi[idx.row()]
        self.show_selected_list()

    def show_rtmp(self, idx):
        if self.select_camera and self.select_camera.address:
            address = Video.create_address(0, self.select_camera.address)
            Video().open_rtmp(address)

    def show_rtmp1(self):
        self.show_rtmp(0)

    def show_rtmp2(self):
        self.show_rtmp(1)

    def show_selected_list(self):
        self.list_show = []
        idx = self.list_camera.currentIndex()
        for camera in self.cameras:
            self.list_show.append(camera.get_simple_info())
        if self.tab_action.currentIndex():
            for i, state in enumerate(self.select_list_multi):
                if state:
                    self.list_show[i] = self.list_show[i] + '(selected)'
                else:
                    self.list_show[i] = self.list_show[i]
        else:
            if idx.row() >= 0:
                self.list_show[idx.row()] = self.list_show[idx.row()] + '(selected)'
        self.slm.setStringList(self.list_show)
        self.list_camera.setModel(self.slm)
        self.list_camera.setCurrentIndex(idx)
