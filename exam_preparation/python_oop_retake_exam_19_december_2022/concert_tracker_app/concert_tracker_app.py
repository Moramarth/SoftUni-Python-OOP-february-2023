from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.band import Band
from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.band_members.drummer import Drummer
from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.band_members.guitarist import Guitarist
from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.band_members.singer import Singer
from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = list()
        self.musicians = list()
        self.concerts = list()

    def musician_name_already_exists(self, name):
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type == "Guitarist":
            self.musician_name_already_exists(name)
            musician = Guitarist(name, age)

        elif musician_type == "Drummer":
            self.musician_name_already_exists(name)
            musician = Drummer(name, age)

        elif musician_type == "Singer":
            self.musician_name_already_exists(name)
            musician = Singer(name, age)

        else:
            raise ValueError("Invalid musician type!")

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    @staticmethod
    def existing_name_validator(value, collection):
        for item in collection:
            if item.name == value:
                return item

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.existing_name_validator(musician_name, self.musicians)
        band = self.existing_name_validator(band_name, self.bands)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.existing_name_validator(band_name, self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = self.existing_name_validator(musician_name, band.members)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        type_set = {Drummer, Guitarist, Singer}
        band = self.existing_name_validator(band_name, self.bands)
        current_band_members = set()
        for member in band.members:
            current_band_members.add(member.__class__)

        if type_set != current_band_members:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        members_skills = set()
        for member in band.members:
            for skill in member.skills:
                members_skills.add(skill)
        needed_skills = set()

        if concert.genre == "Rock":
            needed_skills = {"play rock", "sing high pitch notes", "play the drums with drumsticks"}
        elif concert.genre == "Metal":
            needed_skills = {"play the drums with drumsticks", "sing low pitch notes", "play metal"}
        elif concert.genre == "Jazz":
            needed_skills = {"play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes",
                             "play jazz"}

        if not needed_skills.issubset(members_skills):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
