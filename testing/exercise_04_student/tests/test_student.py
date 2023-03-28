import unittest

from testing.exercise_04_student.project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_student = Student("Proval Provalyanov")

    def test_constructor(self):
        self.assertEqual("Proval Provalyanov", self.test_student.name)
        self.assertEqual({}, self.test_student.courses)

    def test_enroll_course_without_notes(self):
        result = self.test_student.enroll("Course", ["a", "b", "c", "c"], "N")
        expected_output = "Course has been added."
        self.assertEqual(expected_output, result)
        self.assertEqual([], self.test_student.courses["Course"])

    def test_enroll_course_with_adding_notes(self):
        result = self.test_student.enroll("Course", ["a", "b", "c", "c"], "Y")
        expected_output = "Course and course notes have been added."
        self.assertEqual(expected_output, result)
        self.assertEqual(["a", "b", "c", "c"], self.test_student.courses["Course"])

    def test_enroll_course_with_adding_notes_default_add_notes(self):
        result = self.test_student.enroll("Course", ["a", "b", "c", "c"])
        expected_output = "Course and course notes have been added."
        self.assertEqual(expected_output, result)
        self.assertEqual(["a", "b", "c", "c"], self.test_student.courses["Course"])

    def test_enroll_the_same_course(self):
        self.test_student.enroll("Course", ["a", "b", "c", "c"], "Y")
        result = self.test_student.enroll("Course", ["a", "b", "c", "c"])
        expected_output = "Course already added. Notes have been updated."
        self.assertEqual(expected_output, result)
        self.assertEqual(['a', 'b', 'c', 'c', 'a', 'b', 'c', 'c'], self.test_student.courses["Course"])

    def test_add_notes_no_course_error(self):
        with self.assertRaises(Exception) as context:
            self.test_student.add_notes("Course", ["a", "b", "c", "c"])
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_add_notes_to_existing_course(self):
        self.test_student.enroll("Course", ["a", "b", "c", "c"], "Y")
        result = self.test_student.add_notes("Course", "a")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["a", "b", "c", "c", "a"], self.test_student.courses["Course"])

    def test_leave_invalid_course_error(self):
        with self.assertRaises(Exception) as context:
            self.test_student.leave_course("Course")
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))

    def test_leave_course_that_was_enrolled(self):
        self.test_student.enroll("Course", ["a", "b", "c", "c"], "Y")
        result = self.test_student.leave_course("Course")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.test_student.courses)


if __name__ == '__main__':
    unittest.main()
