from inheritance.exercise_02_zoo.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)