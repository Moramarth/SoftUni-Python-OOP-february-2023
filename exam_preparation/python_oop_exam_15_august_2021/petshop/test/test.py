from unittest import TestCase, main
from exam_preparation.python_oop_exam_15_august_2021.petshop.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Shop")

    def test_constructor(self):
        self.assertEqual("Shop", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.shop.add_food("food", -2)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_valid_data(self):
        result = self.shop.add_food("food", 5)
        expected_output = "Successfully added 5.00 grams of food."
        self.assertEqual(expected_output, result)
        self.assertEqual({"food": 5}, self.shop.food)
        result2 = self.shop.add_food("food", 5)
        expected_output2 = "Successfully added 5.00 grams of food."
        self.assertEqual(expected_output2, result2)
        self.assertEqual({"food": 10}, self.shop.food)
        result3 = self.shop.add_food("food2", 5)
        expected_output3 = "Successfully added 5.00 grams of food2."
        self.assertEqual(expected_output3, result3)
        self.assertEqual({"food": 10, "food2": 5}, self.shop.food)

    def test_add_pet_valid_data(self):
        result = self.shop.add_pet("Pet")
        expected_output = "Successfully added Pet."
        self.assertEqual(expected_output, result)
        self.assertEqual(["Pet"], self.shop.pets)
        result2 = self.shop.add_pet("Pet2")
        expected_output2 = "Successfully added Pet2."
        self.assertEqual(expected_output2, result2)
        self.assertEqual(["Pet", "Pet2"], self.shop.pets)

    def test_add_pet_name_error(self):
        self.shop.add_pet("Pet")
        with self.assertRaises(Exception) as context:
            self.shop.add_pet("Pet")
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_feed_pet_no_name_in_list_error(self):
        self.shop.add_food("food", 5)
        with self.assertRaises(Exception) as context:
            self.shop.feed_pet("food", "Pet")
        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_pet_no_food_error(self):
        self.shop.add_pet("Pet")
        result = self.shop.feed_pet("food", "Pet")
        expected_output = "You do not have food"
        self.assertEqual(expected_output, result)

    def test_feed_pet_low_food(self):
        self.shop.add_food("food", 5)
        self.assertEqual(5, self.shop.food["food"])
        self.shop.add_pet("Pet")
        result = self.shop.feed_pet("food", "Pet")
        expected_output = "Adding food..."
        self.assertEqual(expected_output, result)
        self.assertEqual(1005, self.shop.food["food"])

        result2 = self.shop.feed_pet("food", "Pet")
        expected_output2 = "Pet was successfully fed"
        self.assertEqual(expected_output2, result2)
        self.assertEqual(905, self.shop.food["food"])

    def test_repr(self):
        self.shop.add_pet("Pet")
        self.shop.add_pet("Pet2")
        self.shop.add_pet("Pet3")
        result = str(self.shop)
        expected_output = 'Shop Shop:\nPets: Pet, Pet2, Pet3'
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
