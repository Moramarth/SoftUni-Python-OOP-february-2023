from encapsulation.exercise_04_restaurant.food.starter import Starter


class Soup(Starter):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)
