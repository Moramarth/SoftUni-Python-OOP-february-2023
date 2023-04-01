from exam_preparation.python_oop_exam_14_august_2022.horse_racings.horse_race import HorseRace
from exam_preparation.python_oop_exam_14_august_2022.horse_racings.horse_specification.appaloosa import Appaloosa
from exam_preparation.python_oop_exam_14_august_2022.horse_racings.horse_specification.thoroughbred import Thoroughbred
from exam_preparation.python_oop_exam_14_august_2022.horse_racings.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = list()  # stores instances of class Horse
        self.jockeys = list()  # stores instances of class Jockey
        self.horse_races = list()  # stores instances of class HorseRace

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.attribute_collection_search(horse_name, "name", self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = None

        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        if new_horse:
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.attribute_collection_search(jockey_name, "name", self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.attribute_collection_search(race_type, "race_type", self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.attribute_collection_search(jockey_name, "name", self.jockeys)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horses = [horse for horse in self.horses if horse.__class__.__name__ == horse_type]
        if not horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        horse = self.attribute_collection_search(False, "is_taken", reversed(horses))
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.attribute_collection_search(race_type, "race_type", self.horse_races)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.attribute_collection_search(jockey_name, "name", self.jockeys)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.attribute_collection_search(race_type, "race_type", self.horse_races)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        horses = [jockey.horse for jockey in race.jockeys]
        speed = {horse: horse.speed for horse in horses}
        max_speed = max(speed.values())
        fastest_horse = next(horse for horse in speed if speed[horse] == max_speed)
        winner = self.attribute_collection_search(fastest_horse, "horse", race.jockeys)

        return f"The winner of the {race_type} race," \
               f" with a speed of {max_speed}km/h is {winner.name}! Winner's horse: {fastest_horse.name}."
