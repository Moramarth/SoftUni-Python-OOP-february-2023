from unittest import TestCase, main
from exam_preparation.python_oop_retake_exam_22_ugust_2022.shopping_cart.shopping_cart import ShoppingCart


class ShoppingCartTests(TestCase):
    def setUp(self) -> None:
        self.shop = ShoppingCart("Shop", 100)
        self.other = ShoppingCart("Added", 100)

    def test_constructor_with_valid_data(self):
        self.assertEqual("Shop", self.shop.shop_name)
        self.assertEqual(100, self.shop.budget)
        self.assertEqual({}, self.shop.products)

    def test_shop_name_lower_first_letter(self):
        with self.assertRaises(ValueError) as context:
            self.shop.shop_name = "shop"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(context.exception))

    def test_shop_name_with_digits_in_the_string(self):
        with self.assertRaises(ValueError) as context:
            self.shop.shop_name = "Sh0p"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(context.exception))

    def test_shop_name_with_symbols_in_the_string(self):
        with self.assertRaises(ValueError) as context:
            self.shop.shop_name = "Shop^"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(context.exception))

    def test_add_to_cart_with_valid_data(self):
        result = self.shop.add_to_cart("Product", 20.25)
        expected_output = "Product product was successfully added to the cart!"
        self.assertEqual(expected_output, result)
        self.assertEqual({"Product": 20.25}, self.shop.products)

    def test_add_to_cart_with_high_price(self):
        with self.assertRaises(ValueError) as context:
            self.shop.add_to_cart("Product", 200)
        self.assertEqual("Product Product cost too much!", str(context.exception))

    def test_add_to_cart_with_minimum_invalid_price(self):
        with self.assertRaises(ValueError) as context:
            self.shop.add_to_cart("Product", 100)
        self.assertEqual("Product Product cost too much!", str(context.exception))

    def test_remove_from_cart_with_valid_data(self):
        self.shop.add_to_cart("Product", 20.25)
        self.shop.add_to_cart("Product2", 20.25)
        result = self.shop.remove_from_cart("Product")
        expected_output = "Product Product was successfully removed from the cart!"
        self.assertEqual(expected_output, result)
        self.assertEqual({"Product2": 20.25}, self.shop.products)

    def test_remove_from_cart_no_products(self):
        with self.assertRaises(ValueError) as context:
            self.shop.remove_from_cart("Product")
        self.assertEqual("No product with name Product in the cart!", str(context.exception))

    def test_buy_products_money_is_enough(self):
        self.shop.add_to_cart("Product", 20.25)
        result = self.shop.buy_products()
        expected_output = 'Products were successfully bought! Total cost: 20.25lv.'
        self.assertEqual(expected_output, result)

    def test_buy_products_not_enough_money(self):
        self.shop.add_to_cart("Product", 51)
        self.shop.add_to_cart("Product2", 50)
        with self.assertRaises(ValueError) as context:
            self.shop.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 1.00lv!", str(context.exception))

    def test_add_method_for_shopping_cart(self):
        self.shop.add_to_cart("Product", 51)
        self.other.add_to_cart("Product2", 50)
        new_shopping_cart = self.shop + self.other
        self.assertEqual("ShopAdded", new_shopping_cart.shop_name)
        self.assertEqual(200, new_shopping_cart.budget)
        self.assertEqual({"Product": 51, "Product2": 50}, new_shopping_cart.products)


if __name__ == '__main__':
    main()
