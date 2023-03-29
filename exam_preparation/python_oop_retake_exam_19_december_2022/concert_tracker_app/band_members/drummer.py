from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.band_members.musician import Musician


class Drummer(Musician):
    @property
    def available_skills(self):
        return [
            "play the drums with drumsticks",
            "play the drums with drum brushes",
            "read sheet music",
        ]
