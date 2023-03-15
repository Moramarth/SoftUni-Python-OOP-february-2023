from polymorphism_and_abstraction.exercise_04_wild_farm.animals.animal import Bird
from polymorphism_and_abstraction.exercise_04_wild_farm.food import Food, Meat


class Owl(Bird):
    WEIGHT_INCREASED_PER_MEAL = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASED_PER_MEAL


class Hen(Bird):
    WEIGHT_INCREASED_PER_MEAL = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASED_PER_MEAL
