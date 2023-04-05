from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name: str,):
        super().__init__(name, self.default_capacity)

    @property
    def default_capacity(self):
        return 25
