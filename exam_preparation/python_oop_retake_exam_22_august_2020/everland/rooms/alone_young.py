from exam_preparation.python_oop_retake_exam_22_august_2020.everland.appliances.tv import TV
from exam_preparation.python_oop_retake_exam_22_august_2020.everland.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.default_members_count)
        self.room_cost = self.default_room_cost
        self.appliances = self.set_appliances(self.default_members_count, self.types_of_appliances)
        self.expenses = self.calculate_expenses(self.appliances)

    @property
    def types_of_appliances(self):
        return [TV]

    @property
    def default_members_count(self):
        return 1

    @property
    def default_room_cost(self):
        return 10
