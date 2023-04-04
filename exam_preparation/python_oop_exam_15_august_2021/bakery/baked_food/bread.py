from exam_preparation.python_oop_exam_15_august_2021.bakery.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name: str, price: float):
        super().__init__(name, self.portion_size, price)

    @property
    def portion_size(self):
        return 200
