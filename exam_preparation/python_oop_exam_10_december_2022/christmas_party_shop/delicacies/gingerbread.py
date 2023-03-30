from exam_preparation.python_oop_exam_10_december_2022.christmas_party_shop.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, self.portion_size, price)

    @property
    def portion_size(self):
        return 200

    @property
    def delicacy_type(self):
        return Gingerbread.__name__
