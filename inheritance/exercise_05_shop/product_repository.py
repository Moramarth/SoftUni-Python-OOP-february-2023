from inheritance.exercise_05_shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = list()

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            searched_product = list(filter(lambda x: x.name == product_name, self.products))[0]
            return searched_product
        except IndexError:
            pass

    def remove(self, product_name: str):
        try:
            searched_product = next(filter(lambda x: x.name == product_name, self.products))
            self.products.remove(searched_product)
        except StopIteration:
            pass

    def __repr__(self):
        data = list()
        for element in self.products:
            data.append(f"{element.name}: {element.quantity}")

        return "\n".join(data)
