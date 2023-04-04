from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = list()

    def breathe(self):
        self.oxygen -= self.take_a_breath

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @property
    @abstractmethod
    def take_a_breath(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def details(self):
        output = [
            f"Name: {self.name}",
            f"Oxygen: {self.oxygen}",
            f"Backpack items: {', '.join(self.backpack) if self.backpack else 'none'}"
        ]
        return "\n".join(output)
