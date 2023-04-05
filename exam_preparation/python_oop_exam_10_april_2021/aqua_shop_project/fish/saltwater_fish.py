from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.default_fish_size, price)

    @property
    def can_live_in(self):
        return "SaltwaterAquarium"

    @property
    def default_fish_size(self):
        return 5

    @property
    def increase_size_when_eats(self):
        return 2