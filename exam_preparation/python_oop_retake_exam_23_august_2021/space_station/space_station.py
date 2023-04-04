from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.astronaut.astronaut_repository import \
    AstronautRepository
from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.astronaut.biologist import Biologist
from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.astronaut.geodesist import Geodesist
from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.astronaut.meteorologist import Meteorologist
from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.planet.planet import Planet
from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.planet.planet_repository import \
    PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self._number_of_successful_missions = 0
        self._number_of_not_completed_missions = 0

    @property
    def valid_astronaut_types(self):
        return {
            "Biologist": Biologist,
            "Geodesist": Geodesist,
            "Meteorologist": Meteorologist,
        }

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.valid_astronaut_types:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.add(self.valid_astronaut_types[astronaut_type](name))

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        available_astronauts = [astronaut for astronaut in self.astronaut_repository.astronauts
                                if astronaut.oxygen > 30]
        if not available_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_for_mission = sorted(available_astronauts, key=lambda a: -a.oxygen)[:5]

        participated_in_mission = 0
        for astronaut in astronauts_for_mission:
            if not planet.items:
                self._number_of_successful_missions += 1
                self.planet_repository.remove(planet)
                return f"Planet: {planet_name} was explored. {participated_in_mission}" \
                       f" astronauts participated in collecting items."

            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

            participated_in_mission += 1

        self._number_of_not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        output = [
            f"{self._number_of_successful_missions} successful missions!",
            f"{self._number_of_not_completed_missions} missions were not completed!",
            f"Astronauts' info:"
        ]
        for astronaut in self.astronaut_repository.astronauts:
            output.append(astronaut.details())

        return "\n".join(output)
