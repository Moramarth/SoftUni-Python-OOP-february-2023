from exam_preparation.python_oop_retake_exam_22_august_2020.everland.appliances.fridge import Fridge
from exam_preparation.python_oop_retake_exam_22_august_2020.everland.appliances.laptop import Laptop
from exam_preparation.python_oop_retake_exam_22_august_2020.everland.appliances.tv import TV
from exam_preparation.python_oop_retake_exam_22_august_2020.everland.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *args):
        super().__init__(family_name, salary_one + salary_two, self.default_members_count)
        self.children = list(args)
        self.members_count = len(self.children) + self.default_members_count
        self.room_cost = self.default_room_cost
        self.appliances = self.set_appliances(self.members_count, self.types_of_appliances)
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    @property
    def default_members_count(self):
        return 2

    @property
    def default_room_cost(self):
        return 30

    @property
    def types_of_appliances(self):
        return [TV, Fridge, Laptop]
