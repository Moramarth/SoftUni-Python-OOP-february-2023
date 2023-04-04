from exam_preparation.python_oop_retake_exam_23_august_2021.space_station.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    _DEFAULT_OXYGEN_START = 90

    def __init__(self, name: str):
        super().__init__(name, self._DEFAULT_OXYGEN_START)

    @property
    def take_a_breath(self):
        return 15
