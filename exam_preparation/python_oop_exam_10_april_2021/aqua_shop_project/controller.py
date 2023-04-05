from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.decoration.decoration_repository import DecorationRepository
from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.decoration.ornament import Ornament
from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.decoration.plant import Plant
from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.fish.freshwater_fish import FreshwaterFish
from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = list()

    @property
    def valid_aquariums(self):
        return {
            "FreshwaterAquarium": FreshwaterAquarium,
            "SaltwaterAquarium": SaltwaterAquarium,
        }

    @property
    def valid_decorations(self):
        return {
            "Ornament": Ornament,
            "Plant": Plant,
        }

    @property
    def valid_fish_types(self):
        return {
            "FreshwaterFish": FreshwaterFish,
            "SaltwaterFish": SaltwaterFish,
        }

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.valid_aquariums:
            return "Invalid aquarium type."

        self.aquariums.append(self.valid_aquariums[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.valid_decorations:
            return "Invalid decoration type."

        self.decorations_repository.add(self.valid_decorations[decoration_type]())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.attribute_collection_search(aquarium_name, "name", self.aquariums)
        if aquarium:
            decoration = self.decorations_repository.find_by_type(decoration_type)
            if decoration == "None":
                return f"There isn't a decoration of type {decoration_type}."

            self.decorations_repository.remove(decoration)
            aquarium.add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.valid_fish_types:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.attribute_collection_search(aquarium_name, "name", self.aquariums)
        if aquarium:
            fish = self.valid_fish_types[fish_type](fish_name, fish_species, price)
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.attribute_collection_search(aquarium_name, "name", self.aquariums)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.attribute_collection_search(aquarium_name, "name", self.aquariums)
        value_of_aquarium = sum(fish.price for fish in aquarium.fish)\
                            + sum(decoration.price for decoration in aquarium.decorations)
        return f"The value of Aquarium {aquarium_name} is {value_of_aquarium:.2f}."

    def report(self):
        output = list()
        for aquarium in self.aquariums:
            output.append(str(aquarium))

        return "\n".join(output)
