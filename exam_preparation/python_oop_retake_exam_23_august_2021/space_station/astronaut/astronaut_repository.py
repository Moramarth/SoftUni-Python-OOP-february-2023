from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = list()

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
