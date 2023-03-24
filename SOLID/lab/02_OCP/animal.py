"""
Refactor the provided code, so you do not need to make any changes
in it when you want to add new species to the animals' list
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Chicken(Animal):
    def make_sound(self):
        return "Cluck"


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]

for animal in animals:
    print(animal.make_sound())
