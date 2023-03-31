from exam_preparation.python_oop_exam_10_december_2022.christmas_party_shop.booths.open_booth import OpenBooth
from exam_preparation.python_oop_exam_10_december_2022.christmas_party_shop.booths.private_booth import PrivateBooth
from exam_preparation.python_oop_exam_10_december_2022.christmas_party_shop.delicacies.gingerbread import Gingerbread
from exam_preparation.python_oop_exam_10_december_2022.christmas_party_shop.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = list()
        self.delicacies = list()
        self.income = 0

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.attribute_collection_search(name, "name", self.delicacies):
            raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            new_delicacy = Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            new_delicacy = Stolen(name, price)
        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if self.attribute_collection_search(booth_number, "booth_number", self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            new_booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            new_booth = PrivateBooth(booth_number, capacity)
        else:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.attribute_collection_search(booth_number, "booth_number", self.booths)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.attribute_collection_search(delicacy_name, "name", self.delicacies)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.attribute_collection_search(booth_number, "booth_number", self.booths)
        bill = booth.price_for_reservation + sum(delicacy.price for delicacy in booth.delicacy_orders)
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        self.income += bill
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
