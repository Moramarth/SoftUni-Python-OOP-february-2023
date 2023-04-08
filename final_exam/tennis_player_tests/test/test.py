from unittest import TestCase, main
from final_exam.tennis_player_tests.tennis_player import TennisPlayer


class TennisPlayerTests(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Player", 20, 25)
        self.player_two = TennisPlayer("Player2", 25, 20)
        self.player_three = TennisPlayer("Player3", 25, 20)

    def test_constructor(self):
        self.assertEqual("Player", self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(25, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as context:
            self.player.name = ""
        self.assertEqual("Name should be more than 2 symbols!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.player.name = "PP"
        self.assertEqual("Name should be more than 2 symbols!", str(context.exception))

    def test_age_setter(self):
        with self.assertRaises(ValueError) as context:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(context.exception))

    def test_add_new_win(self):
        self.player.add_new_win("Tournament1")
        self.assertEqual(["Tournament1"], self.player.wins)
        self.player.add_new_win("Tournament2")
        self.assertEqual(["Tournament1", "Tournament2"], self.player.wins)

    def test_add_new_win_error(self):
        self.player.add_new_win("Tournament1")
        self.player.add_new_win("Tournament2")
        result = self.player.add_new_win("Tournament1")
        expected_output = "Tournament1 has been already added to the list of wins!"
        self.assertEqual(expected_output, result)

    def test_less_than_method(self):
        result = self.player < self.player_two
        expected_output = 'Player is a better player than Player2'
        self.assertEqual(expected_output, result)

        result2 = self.player_two < self.player
        expected_output2 = 'Player is a top seeded player and he/she is better than Player2'
        self.assertEqual(expected_output2, result2)

        result3 = self.player_two < self.player_three
        expected_output3 = "Player2 is a better player than Player3"
        self.assertEqual(expected_output3, result3)

    def test_str_method(self):
        result = str(self.player)
        expected_output = f"Tennis Player: Player\n" \
                           f"Age: 20\n" \
                           f"Points: 25.0\n" \
                           f"Tournaments won: "
        self.assertEqual(expected_output, result)

        self.player.add_new_win("Tournament1")
        self.player.add_new_win("Tournament2")
        result2 = str(self.player)
        expected_output2 = f"Tennis Player: Player\n" \
                           f"Age: 20\n" \
                           f"Points: 25.0\n" \
                           f"Tournaments won: Tournament1, Tournament2"
        self.assertEqual(expected_output2, result2)

if __name__ == '__main__':
    main()