from exam_preparation.python_oop_exam_14_august_2022.horse_racings.horse_specification.horse import Horse


class Thoroughbred(Horse):

    @property
    def max_speed(self):
        return 140

    @property
    def speed_increased_by_training(self):
        return 3
