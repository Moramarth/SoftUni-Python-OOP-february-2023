from abc import ABC, abstractmethod

from polymorphism_and_abstraction.exercise_04_wild_farm.food import Food


class Animal(ABC):
    WEIGHT_INCREASED_PER_MEAL = 0

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: int, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}," \
               f" {self.weight}," \
               f" {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}," \
               f" {self.weight}," \
               f" {self.living_region}, {self.food_eaten}]"
