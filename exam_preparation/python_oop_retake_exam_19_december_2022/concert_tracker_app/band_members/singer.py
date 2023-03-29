from exam_preparation.python_oop_retake_exam_19_december_2022.concert_tracker_app.band_members.musician import Musician


class Singer(Musician):
    @property
    def available_skills(self):
        return [
            "sing high pitch notes",
            "sing low pitch notes",
        ]
