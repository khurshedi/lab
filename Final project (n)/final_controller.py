from PyQt5.QtWidgets import *
from finalp import Ui_MainWindow


# from classes import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.power2 = False
        self.channel2 = 0
        self.volume2 = 0
        self.brightness2 = 0

        self.channel_upX.clicked.connect(lambda: self.channel_up())
        self.channel_downX.clicked.connect(lambda: self.channel_down())
        self.powerX.clicked.connect(lambda: self.power())
        self.volume_upX.clicked.connect(lambda: self.volume_up())
        self.volume_downX.clicked.connect(lambda: self.volume_down())
        self.brightness_upX.clicked.connect(lambda: self.brightness_up())
        self.brightness_downX.clicked.connect(lambda: self.brightness_down())
        self.oneX.clicked.connect(lambda: self.one())
        self.twoX.clicked.connect(lambda: self.two())
        self.threeX.clicked.connect(lambda: self.three())

    def channel_up(self):
        if self.power2:
            if self.channel2 == 3:
                self.channel2 = 0
            else:
                self.channel2 += 1
        self.lineEdit.setText(
            f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def channel_down(self):
        if self.power2:
            if self.channel2 == 0:
                self.channel2 = 3
            else:
                self.channel2 -= 1
            self.lineEdit.setText(
                f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def power(self):
        self.power2 = not self.power2
        self.lineEdit.setText(
            f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def volume_up(self):

        if self.power2:
            if self.volume2 < 2:
                self.volume2 += 1
                self.lineEdit.setText(
                    f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def volume_down(self):
        if self.power2:
            if self.volume2 > 0:
                self.volume2 -= 1
                self.lineEdit.setText(
                    f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def brightness_up(self):
        if self.power2:
            if self.brightness2 < 5:
                self.brightness2 += 1
                self.lineEdit.setText(
                    f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def brightness_down(self):
        if self.power2:
            if self.brightness2 > 0:
                self.brightness2 -= 1
                self.lineEdit.setText(
                    f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def one(self):
        if self.power2:
            self.channel2 = 1
            self.lineEdit.setText(
                f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def two(self):
        if self.power2:
            self.channel2 = 2
            self.lineEdit.setText(
                f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')

    def three(self):
        if self.power2:
            self.channel2 = 3
            self.lineEdit.setText(
                f'TV status: Is on = {self.power2}, Channel = {self.channel2}, Volume = {self.volume2}, Brightness = {self.brightness2}')
