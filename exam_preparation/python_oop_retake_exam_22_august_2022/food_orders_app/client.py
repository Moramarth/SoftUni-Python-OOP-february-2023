class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = list()  # stores objects of type Meal
        self.bill = 0
        self.ordered_quantities = dict()  # stores meal object as keys and their quantity as value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.startswith("0") or len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
