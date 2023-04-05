from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = list()
        self.fish = list()

    @property
    @abstractmethod
    def default_capacity(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    def valid_fish_types(self):
        return "FreshwaterFish", "SaltwaterFish"

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish):
        if not len(self.fish) < self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ in self.valid_fish_types:
            if fish.can_live_in != self.__class__.__name__:
                return "Water not suitable."
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        output = [f"{self.name}:",
                  f"Fish: {' '.join(fish.name for fish in self.fish) if self.fish else 'none'}",
                  f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"
                  ]
        return "\n".join(output)
