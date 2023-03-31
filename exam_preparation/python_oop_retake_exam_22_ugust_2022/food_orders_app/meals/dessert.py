from exam_preparation.python_oop_retake_exam_22_ugust_2022.food_orders_app.meals.meal import Meal


class Dessert(Meal):
    def __init__(self, name: str, price: float, quantity=None):
        super().__init__(name, price, quantity)

    @property
    def quantity_default(self):
        return 30

    @property
    def meal_type(self):
        return "Dessert"
