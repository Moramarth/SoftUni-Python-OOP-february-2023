import unittest

from testing.exercise_03_hero.project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_hero = Hero("Good guy", 10, 50, 10)
        self.test_enemy = Hero("Bad guy", 5, 25, 5)

    def test_constructor_is_working_properly(self):
        self.assertEqual("Good guy", self.test_hero.username)
        self.assertEqual(10, self.test_hero.level)
        self.assertEqual(50, self.test_hero.health)
        self.assertEqual(10, self.test_hero.damage)

    def test_battle_yourself_error(self):
        with self.assertRaises(Exception) as context:
            self.test_hero.battle(self.test_hero)
        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle_with_no_health_error(self):
        self.test_hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_when_enemy_has_no_health(self):
        self.test_enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual(str(context.exception), "You cannot fight Bad guy. He needs to rest")

    def test_battle_hero_wins(self):
        result = self.test_hero.battle(self.test_enemy)
        expected_output = "You win"
        self.assertEqual(result, expected_output)
        self.assertEqual(self.test_hero.health, 30)
        self.assertEqual(self.test_hero.level, 11)
        self.assertEqual(self.test_hero.damage, 15)

    def test_battle_hero_loses(self):
        result = self.test_enemy.battle(self.test_hero)
        expected_output = "You lose"
        self.assertEqual(result, expected_output)
        self.assertEqual(self.test_hero.health, 30)
        self.assertEqual(self.test_hero.level, 11)
        self.assertEqual(self.test_hero.damage, 15)

    def test_battle_ended_as_a_draw(self):
        self.test_enemy.damage = 10
        result = self.test_hero.battle(self.test_enemy)
        expected_output = "Draw"
        self.assertEqual(result, expected_output)
        self.assertGreaterEqual(0, self.test_hero.health)
        self.assertGreaterEqual(0, self.test_enemy.health)

    def test_you_loose_but_you_are_not_dead(self):
        self.test_hero.damage = 1
        result = self.test_hero.battle(self.test_enemy)
        expected_output = "You lose"
        self.assertEqual(result, expected_output)
        self.assertGreater(self.test_hero.health, 0)

    def test_string_representation(self):
        result = str(self.test_hero)
        expected_output = f"Hero Good guy: 10 lvl\n" \
                          f"Health: 50\n" \
                          f"Damage: 10\n"
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
