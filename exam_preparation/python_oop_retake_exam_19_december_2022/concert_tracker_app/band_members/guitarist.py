from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.band_members.musician import Musician


class Guitarist(Musician):
    @property
    def available_skills(self):
        return [
            "play metal",
            "play rock",
            "play jazz",
        ]
