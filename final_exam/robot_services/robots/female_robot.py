from final_exam.robot_services.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.default_weight_per_type)

    @property
    def default_weight_per_type(self):
        return 7

    @property
    def weight_gain_after_eating(self):
        return 1

    @property
    def type_of_robot(self):
        return "Female"
