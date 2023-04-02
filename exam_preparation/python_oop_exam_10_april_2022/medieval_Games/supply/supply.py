from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    def details(self):
        return f"{self.supply_type}: {self.name}, {self.energy}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value is None:
            value = self.energy_units
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")

        self.__energy = value

    @property
    def supply_type(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def energy_units(self):
        pass

    def __repr__(self):
        return f"{self.supply_type}: {self.name}, {self.energy}"
