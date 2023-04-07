from exam_preparation.python_oop_exam_11_december_2021.christmas_races.car.car import Car


class MuscleCar(Car):
    @property
    def min_speed(self):
        return 250

    @property
    def max_speed(self):
        return 450
