from exam_preparation.python_oop_retake_exam_18_april_2022.movie_app.movie_specification.movie import Movie


class Fantasy(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction=None):
        if age_restriction is None:
            super().__init__(title, year, owner, self.age_restriction_by_genre)
        else:
            super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction_by_genre(self):
        return 6
