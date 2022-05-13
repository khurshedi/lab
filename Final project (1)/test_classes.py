from classes import *
from main import *



class Test():

    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_power(self):
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0, Brightness = 0'

    def test_channel_up(self):
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0, Brightness = 0'

    def test_channel_down(self):
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0, Brightness = 0'

    def test_volume_up(self):
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1, Brightness = 0'
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2, Brightness = 0'

    def test_volume_down(self):
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0, Brightness = 0'

    def test_channel_1(self):
        self.tv.channel_1()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.channel_1()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0, Brightness = 0'

    def test_channel_2(self):
        self.tv.channel_2()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.channel_2()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0, Brightness = 0'

    def test_channel_3(self):
        self.tv.channel_3()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.channel_3()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0, Brightness = 0'

    def test_brightness_up(self):
        self.tv.brightness_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.brightness_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0, Brightness = 1'

    def test_brightness_down(self):
        self.tv.brightness_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0, Brightness = 0'
        self.tv.power()
        self.tv.brightness_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0, Brightness = 0'

if __name__ == '__main__':
    main()
