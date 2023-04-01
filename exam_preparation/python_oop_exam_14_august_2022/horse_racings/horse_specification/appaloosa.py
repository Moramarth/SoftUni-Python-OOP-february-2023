from exam_preparation.python_oop_exam_14_august_2022.horse_racings.horse_specification.horse import Horse


class Appaloosa(Horse):

    @property
    def max_speed(self):
        return 120

    @property
    def speed_increased_by_training(self):
        return 2
