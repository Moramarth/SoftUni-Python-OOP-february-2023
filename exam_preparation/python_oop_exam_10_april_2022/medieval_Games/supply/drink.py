from medieval_Games.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str):
        super().__init__(name, 15)

    @property
    def energy_units(self):
        return 15
