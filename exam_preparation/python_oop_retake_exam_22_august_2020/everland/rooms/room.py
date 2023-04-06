class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = list()
        self.appliances = list()
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):  # lists with children or appliances
        items = list()
        for collection in args:
            items.extend(collection)

        return sum(item.get_monthly_expense() for item in items)

    @staticmethod
    def set_appliances(members_count, types_of_appliances: list):
        result = list()
        for _ in range(members_count):
            for appliance in types_of_appliances:
                result.append(appliance())

        return result


