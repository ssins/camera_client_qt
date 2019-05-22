from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):
    # token
    login_signal = pyqtSignal(str)
    # add camera
    add_camera_signal = pyqtSignal()

