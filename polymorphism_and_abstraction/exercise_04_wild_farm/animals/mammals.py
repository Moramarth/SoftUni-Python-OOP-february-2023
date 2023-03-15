from polymorphism_and_abstraction.exercise_04_wild_farm.animals.animal import Mammal
from polymorphism_and_abstraction.exercise_04_wild_farm.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASED_PER_MEAL = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASED_PER_MEAL


class Dog(Mammal):
    WEIGHT_INCREASED_PER_MEAL = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASED_PER_MEAL


class Cat(Mammal):
    WEIGHT_INCREASED_PER_MEAL = 0.30

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASED_PER_MEAL


class Tiger(Mammal):
    WEIGHT_INCREASED_PER_MEAL = 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASED_PER_MEAL
