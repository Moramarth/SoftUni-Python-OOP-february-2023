from exam_preparation.python_oop_exam_10_april_2022.medieval_games.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy=None):
        super().__init__(name, energy)

    @property
    def energy_units(self):
        return 25
