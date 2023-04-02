class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None  # stores an instance of class Car
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")
        self.__name = value
