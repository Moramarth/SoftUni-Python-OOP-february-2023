from exam_preparation.python_oop_exam_10_april_2022.medieval_games.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str):
        super().__init__(name, self.energy_units)

    @property
    def energy_units(self):
        return 15
