from polymorphism_and_abstraction.exercise_05_animals.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Female")

    @staticmethod
    def make_sound():
        return "Meow"
