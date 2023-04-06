from unittest import TestCase, main
from exam_preparation.python_oop_retake_exam_22_august_2020.student_report_card.student_report_card import \
    StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.card = StudentReportCard("Student", 10)

    def test_constructor(self):
        self.assertEqual("Student", self.card.student_name)
        self.assertEqual(10, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_student_name_setter(self):
        with self.assertRaises(ValueError) as context:
            self.card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_school_year_setter(self):
        with self.assertRaises(ValueError) as context:
            self.card.school_year = 2023
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))
        self.card.school_year = 1
        self.assertEqual(1, self.card.school_year)
        self.card.school_year = 12
        self.assertEqual(12, self.card.school_year)

    def test_add_grade(self):
        self.card.add_grade("Subject1", 5.50)
        self.card.add_grade("Subject2", 6.00)
        self.assertEqual({"Subject1": [5.50], "Subject2": [6.00]}, self.card.grades_by_subject)
        self.card.add_grade("Subject1", 4.75)
        self.card.add_grade("Subject2", 4.40)
        self.assertEqual({"Subject1": [5.50, 4.75], "Subject2": [6.00, 4.40]}, self.card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.card.add_grade("Subject1", 5.50)
        self.card.add_grade("Subject2", 6.00)
        self.card.add_grade("Subject1", 4.75)
        self.card.add_grade("Subject2", 4.40)
        result = self.card.average_grade_by_subject()
        expected_output = "Subject1: 5.12\nSubject2: 5.20"
        self.assertEqual(expected_output, result)

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError) as context:
            self.card.average_grade_for_all_subjects()
        self.assertEqual("division by zero", str(context.exception))

        with self.assertRaises(ZeroDivisionError) as context:
            str(self.card)
        self.assertEqual("division by zero", str(context.exception))

    def test_average_grade_for_all(self):
        self.card.add_grade("Subject1", 5.50)
        self.card.add_grade("Subject2", 6.00)
        self.card.add_grade("Subject1", 4.75)
        self.card.add_grade("Subject2", 4.40)
        result = self.card.average_grade_for_all_subjects()
        expected_output = "Average Grade: 5.16"
        self.assertEqual(expected_output, result)

    def test_repr(self):
        self.card.grades_by_subject = {"Subject1": [5.50, 4.75], "Subject2": [6.00, 4.40]}
        result = str(self.card)
        expected_output = "Name: Student\n" \
                          "Year: 10\n" \
                          "----------\n" \
                          "Subject1: 5.12\n" \
                          "Subject2: 5.20\n" \
                          "----------\n" \
                          "Average Grade: 5.16"
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
