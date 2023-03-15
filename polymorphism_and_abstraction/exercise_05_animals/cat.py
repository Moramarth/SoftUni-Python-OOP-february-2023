from polymorphism_and_abstraction.exercise_05_animals.animal import Animal


class Cat(Animal):
    @staticmethod
    def make_sound():
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"