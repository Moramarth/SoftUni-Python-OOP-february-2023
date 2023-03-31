from exam_preparation.python_oop_retake_exam_22_ugust_2022.food_orders_app.client import Client
from exam_preparation.python_oop_retake_exam_22_ugust_2022.food_orders_app.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = list()  # stores objects of type Meal
        self.clients_list = list()  # stores objects of type Client

    def search_by_phone_number(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def register_client(self, client_phone_number: str):
        if not self.search_by_phone_number(client_phone_number):
            new_client = Client(client_phone_number)
            self.clients_list.append(new_client)
            return f"Client {client_phone_number} registered successfully."
        raise Exception("The client has already been registered!")

    def add_meals_to_menu(self, *meals: Meal):
        [self.menu.append(meal) for meal in meals if Meal in meal.__class__.__mro__]

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        is_the_menu_ready = self.show_menu()
        client = self.search_by_phone_number(client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for key in meal_names_and_quantities:
            if all(meal.name != key for meal in self.menu):
                raise Exception(f"{key} is not on the menu!")

        for key, value in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == key, self.menu))
            if meal.quantity < value:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

        for key, value in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == key, self.menu))
            client.shopping_cart.append(meal)
            client.bill += meal.price * value
            if meal not in client.ordered_quantities:
                client.ordered_quantities[meal] = 0
            client.ordered_quantities[meal] += value
            meal.quantity -= value

        return f"Client {client_phone_number} successfully ordered" \
               f" {', '.join(meal.name for meal in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.search_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        client.shopping_cart.clear()
        client.bill = 0
        for key, value in client.ordered_quantities.items():
            key.quantity += value
        client.ordered_quantities = dict()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.search_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        self.receipt_id += 1
        total_paid_money = client.bill
        client.shopping_cart.clear()
        client.bill = 0

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
