class HorseRace:
    __VALID_RACE_TYPES = ("Winter", "Spring", "Autumn", "Summer")

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = list()  # stores instances of class Jockey

    @property
    def race_type(self):
        return self.__race_type
    
    @race_type.setter
    def race_type(self, value):
        if value not in self.__VALID_RACE_TYPES:
            raise ValueError("Race type does not exist!")
        self.__race_type = value
