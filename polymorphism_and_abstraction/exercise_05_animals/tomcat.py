from polymorphism_and_abstraction.exercise_05_animals.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Male")

    @staticmethod
    def make_sound():
        return "Hiss"
