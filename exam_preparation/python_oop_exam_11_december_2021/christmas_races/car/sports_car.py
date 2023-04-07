from exam_preparation.python_oop_exam_11_december_2021.christmas_races.car.car import Car


class SportsCar(Car):
    @property
    def min_speed(self):
        return 400

    @property
    def max_speed(self):
        return 600
