class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        self.__power: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL



    def power(self) -> None:
        """

        :return: this method checks what's the power status of TV. If its "ON" it turns it "OFF". Or if it's "OFF" it turns it "ON"
        """
        self.__power = not self.__power




    def channel_up(self) -> None:
        """
        this method checks if the power is "ON" next it checks if the channel equals "MAXIMUM" it increases channel by one bringing back the "MINIMUM"
        :return:
        """
        if self.__power:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1




    def channel_down(self) -> None:
        """
        this method checks if the power is "ON" next it checks if the channel equals "MINIMUM" it decreases channel by one bringing back the "MAXIMUM"
        :return:
        """
        if self.__power:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1




    def volume_up(self) -> None:
        """
        this method checks if the power is "ON" next it checks if the volume is less than "MAX VOLUME" then it increases the current volume by one
        :return:
        """
        if self.__power:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1





    def volume_down(self) -> None:
        """
        this method checks if the power is "ON" next it checks if the volume is more than "MIN VOLUME" then it decreases the current volume by one
        :return:
        """
        if self.__power:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1



    def __str__(self):
        return f'TV status: Is on = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}'