from exam_preparation.python_oop_exam_16_august_2020.paint_factory.factory.paint_factory import PaintFactory
from unittest import TestCase, main
from exam_preparation.python_oop_exam_16_august_2020.paint_factory.factory.factory import Factory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Paint", 5)

    def test_constructor(self):
        self.assertEqual("Paint", self.factory.name)
        self.assertEqual(5, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_add_ingredient(self):
        self.factory.add_ingredient("yellow", 3)
        self.assertEqual({"yellow": 3}, self.factory.ingredients)
        self.assertEqual(True, self.factory.can_add(2))
        with self.assertRaises(TypeError)as context:
            self.factory.add_ingredient("purple", 2)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(context.exception))
        self.factory.add_ingredient("white", 2)
        self.assertEqual({"yellow": 3, "white": 2}, self.factory.ingredients)
        self.assertEqual(False, self.factory.can_add(2))
        with self.assertRaises(ValueError)as context:
            self.factory.add_ingredient("white", 2)
        self.assertEqual("Not enough space in factory", str(context.exception))
        with self.assertRaises(TypeError)as context:
            self.factory.add_ingredient("purple", 2)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(context.exception))

    def test_remove_ingredient(self):
        self.factory.ingredients = {"yellow": 3, "white": 2}
        self.factory.remove_ingredient("yellow", 2)
        self.assertEqual({"yellow": 1, "white": 2}, self.factory.ingredients)
        self.factory.remove_ingredient("yellow", 1)
        self.assertEqual({"yellow": 0, "white": 2}, self.factory.ingredients)
        self.factory.remove_ingredient("white", 2)
        self.assertEqual({"yellow": 0, "white": 0}, self.factory.ingredients)
        with self.assertRaises(ValueError) as context:
            self.factory.remove_ingredient("white", 2)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))
        expected_output = "'No such ingredient in the factory'"
        with self.assertRaises(KeyError) as context:
            self.factory.remove_ingredient("purple", 2)
        self.assertEqual(expected_output, str(context.exception))

    def test_property_products(self):
        self.factory.ingredients = {"yellow": 3, "white": 2}
        result = self.factory.products
        expected_output = {"yellow": 3, "white": 2}
        self.assertEqual(expected_output, result)

    def test_repr(self):
        self.factory.ingredients = {"yellow": 3, "white": 2}
        result = str(self.factory)
        expected_output = "Factory name: Paint with capacity 5.\nyellow: 3\nwhite: 2\n"
        self.assertEqual(expected_output, result)

    def test_abstract_class(self):
        expected_output = "Can't instantiate abstract class Factory with abstract methods" \
                          " __init__, add_ingredient, remove_ingredient"
        with self.assertRaises(TypeError) as context:
            Factory("name", 5)
        self.assertEqual(expected_output, str(context.exception))


if __name__ == '__main__':
    main()
