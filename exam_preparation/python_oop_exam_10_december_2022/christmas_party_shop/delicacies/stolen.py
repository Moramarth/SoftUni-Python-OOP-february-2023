from exam_preparation.python_oop_exam_10_december_2022.christmas_party_shop.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, self.portion_size, price)

    @property
    def portion_size(self):
        return 250

    @property
    def delicacy_type(self):
        return Stolen.__name__
