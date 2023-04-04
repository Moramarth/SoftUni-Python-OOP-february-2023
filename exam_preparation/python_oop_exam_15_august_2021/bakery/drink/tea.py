from exam_preparation.python_oop_exam_15_august_2021.bakery.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.default_cost, brand)

    @property
    def default_cost(self):
        return 2.50
