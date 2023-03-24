"""No work, yes prison!"""

import copy


class Person:
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


# class outside of task condition scope
class Child(Person):
    """ Let's assume children get tired faster than adults, so they walk half the given distance"""
    def walk_north(self, dist):
        self.position[1] += dist // 2

    def walk_east(self, dist):
        self.position[0] += dist // 2


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


# code below for testing purpose
def try_to_move(person, movement):
    east, north = movement[0], movement[1]
    print(f"Starting location: {person.position}")
    print(f"The {person.__class__.__name__} is trying to walk to north by {north} and east by {east}.")
    try:
        person.walk_north(north)
        person.walk_east(east)
        print(f"{person.__class__.__name__} is moving...")
    except AttributeError:
        print(f"{person.__class__.__name__} is not free to move!")
    print(f"Current position of the {person.__class__.__name__}: {person.position}")
    print()


prisoner = Prisoner()
free_person = FreePerson([2, 1])
small_child = Child([2, 1])
distance = [-3, 10]  # [east, north]

try_to_move(prisoner, distance)
try_to_move(free_person, distance)
try_to_move(small_child, distance)
