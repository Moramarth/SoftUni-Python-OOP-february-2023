from exam_preparation.python_oop_exam_10_april_2021.aqua_shop_project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    def __init__(self):
        super().__init__(self.default_comfort, self.default_price)

    @property
    def default_comfort(self):
        return 5

    @property
    def default_price(self):
        return 10
