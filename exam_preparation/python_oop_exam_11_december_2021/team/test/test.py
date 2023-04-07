from unittest import TestCase, main
from exam_preparation.python_oop_exam_11_december_2021.team.project.team import Team


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("Team")
        self.other = Team("Other")

    def test_constructor(self):
        self.assertEqual("Team", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as context:
            self.team.name = "Team1"
        self.assertEqual("Team Name can contain only letters!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.team.name = "Team$"
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member(self):
        result = self.team.add_member(Person1=21, Person2=22, Person3=23)
        expected_output = f"Successfully added: Person1, Person2, Person3"
        self.assertEqual(expected_output, result)
        self.assertEqual(3, len(self.team))
        self.team.add_member(Person4=21, Person5=22, Person6=23)
        self.assertEqual(6, len(self.team))

    def test_remove_member(self):
        self.team.add_member(Person1=21, Person2=22)
        result = self.team.remove_member("Person1")
        expected_output = "Member Person1 removed"
        self.assertEqual(expected_output, result)
        self.assertEqual(1, len(self.team))
        result2 = self.team.remove_member("Person2")
        expected_output2 = "Member Person2 removed"
        self.assertEqual(expected_output2, result2)
        self.assertEqual(0, len(self.team))

    def test_remove_member_wrong_name(self):
        self.team.add_member(Person1=21, Person2=22)
        result = self.team.remove_member("Person3")
        self.assertEqual("Member with name Person3 does not exist", result)

    def test_greater_than(self):
        self.team.add_member(Person1=21, Person2=22)
        self.other.add_member(Person3=23)
        result = self.team > self.other
        self.assertEqual(True, result)
        result2 = self.other > self.team
        self.assertEqual(False, result2)

    def test_add_teams(self):
        self.team.add_member(Person1=21, Person2=22)
        self.other.add_member(Person3=23)
        self.assertEqual({"Person1": 21, "Person2": 22}, self.team.members)
        self.assertEqual({"Person3": 23}, self.other.members)
        new_team = self.team + self.other
        self.assertEqual({"Person1": 21, "Person2": 22, "Person3": 23}, new_team.members)
        self.assertEqual("TeamOther", new_team.name)
        self.assertEqual(3, len(new_team))

    def test_str(self):
        self.team.add_member(Person4=21, Person5=22, Person6=23, Person7=22)
        result = str(self.team)
        expected_output = "Team name: Team\n" \
                          "Member: Person6 - 23-years old\n" \
                          "Member: Person5 - 22-years old\n" \
                          "Member: Person7 - 22-years old\n" \
                          "Member: Person4 - 21-years old"
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
