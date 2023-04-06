from exam_preparation.python_oop_retake_exam_22_august_2020.everland.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self):
        super().__init__(self.default_cost_for_type)

    @property
    def default_cost_for_type(self):
        return 0.7
