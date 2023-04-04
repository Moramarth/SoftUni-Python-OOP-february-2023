from exam_preparation.python_oop_exam_15_august_2021.bakery.baked_food.bread import Bread
from exam_preparation.python_oop_exam_15_august_2021.bakery.baked_food.cake import Cake
from exam_preparation.python_oop_exam_15_august_2021.bakery.drink.tea import Tea
from exam_preparation.python_oop_exam_15_august_2021.bakery.drink.water import Water
from exam_preparation.python_oop_exam_15_august_2021.bakery.table.inside_table import InsideTable
from exam_preparation.python_oop_exam_15_august_2021.bakery.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = list()
        self.drinks_menu = list()
        self.tables_repository = list()
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def valid_food_types(self):
        return {
            "Bread": Bread,
            "Cake": Cake,
        }

    @property
    def valid_drink_types(self):
        return {
            "Tea": Tea,
            "Water": Water,
        }

    @property
    def valid_table_types(self):
        return {
            "InsideTable": InsideTable,
            "OutsideTable": OutsideTable,
        }

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    def add_food(self, food_type: str, name: str, price: float):
        if self.attribute_collection_search(name, "name", self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.valid_food_types:
            self.food_menu.append(self.valid_food_types[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if self.attribute_collection_search(name, "name", self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.valid_drink_types:
            self.drinks_menu.append(self.valid_drink_types[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.attribute_collection_search(table_number, "table_number", self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.valid_table_types:
            self.tables_repository.append(self.valid_table_types[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        available_tables = [table for table in self.tables_repository
                            if not table.is_reserved and table.capacity >= number_of_people]

        if not available_tables:
            return f"No available table for {number_of_people} people"

        table = available_tables[0]
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.attribute_collection_search(table_number, "table_number", self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"

        not_in_the_menu = list()
        current_order = list()

        for name in food_names:
            for food in self.food_menu:
                if food.name == name:
                    table.order_food(food)
                    current_order.append(food)
                    break
            else:
                not_in_the_menu.append(name)

        order = [f"Table {table_number} ordered:"]
        for food in current_order:
            order.append(str(food))
        order.append(f"{self.name} does not have in the menu:")
        for food_name in not_in_the_menu:
            order.append(food_name)
        return "\n".join(order)

    def order_drink(self, table_number: int, *drinks_names: str):
        table = self.attribute_collection_search(table_number, "table_number", self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"

        not_in_the_menu = list()
        current_order = list()
        for name in drinks_names:
            for drink in self.drinks_menu:
                if drink.name == name:
                    table.order_drink(drink)
                    current_order.append(drink)
                    break
            else:
                not_in_the_menu.append(name)

        order = [f"Table {table_number} ordered:"]
        for drink in current_order:
            order.append(str(drink))
        order.append(f"{self.name} does not have in the menu:")
        for drink_name in not_in_the_menu:
            order.append(drink_name)
        return "\n".join(order)

    def leave_table(self, table_number: int):
        table = self.attribute_collection_search(table_number, "table_number", self.tables_repository)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        free_tables = [table for table in self.tables_repository if not table.is_reserved]
        info = list()
        for table in free_tables:
            info.append(table.free_table_info())
        return "\n".join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
