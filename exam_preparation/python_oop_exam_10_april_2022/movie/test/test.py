from movie.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Movie", 2000, 5.0)
        self.movie2 = Movie("Movie2", 2000, 6.0)

    def test_constructor(self):
        self.assertEqual("Movie", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(5.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as context:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(context.exception))

    def test_year_setter(self):
        with self.assertRaises(ValueError) as context:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(context.exception))

    def test_add_actor(self):
        self.movie.add_actor("Actor1")
        self.assertEqual(["Actor1"], self.movie.actors)
        self.movie.add_actor("Actor2")
        self.movie.add_actor("Actor3")
        self.assertEqual(["Actor1", "Actor2", "Actor3"], self.movie.actors)

    def test_add_actor_when_actor_exists(self):
        self.movie.actors = ["Actor1", "Actor2", "Actor3"]
        result = self.movie.add_actor("Actor1")
        self.assertEqual("Actor1 is already added in the list of actors!", result)

    def test_greater_than(self):
        result = self.movie2 > self.movie
        expected_output = f'"Movie2" is better than "Movie"'
        self.assertEqual(expected_output, result)
        result2 = self.movie > self.movie2
        self.assertEqual(expected_output, result2)

    def test_repr(self):
        self.movie.actors = ["Actor1", "Actor2", "Actor3"]
        result = self.movie.__repr__()
        expected_output = 'Name: Movie\n' \
                          'Year of Release: 2000\n' \
                          'Rating: 5.00\n' \
                          'Cast: Actor1, Actor2, Actor3'
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
