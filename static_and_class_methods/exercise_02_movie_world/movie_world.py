from static_and_class_methods.exercise_02_movie_world.customer import Customer
from static_and_class_methods.exercise_02_movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = list()  # stores instances of Customer class
        self.dvds = list()  # stores instances of DVD class

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        desired_dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        if not desired_dvd.is_rented:
            if customer.age < desired_dvd.age_restriction:
                return f"{customer.name} should be at least {desired_dvd.age_restriction} to rent this movie"

            customer.rented_dvds.append(desired_dvd)
            desired_dvd.is_rented = True
            return f"{customer.name} has successfully rented {desired_dvd.name}"

        if desired_dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {desired_dvd.name}"

        return "DVD is already rented"

    def return_dvd(self, customer_id, dvd_id):
        rented_dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        customer = next(filter(lambda c: c.id == customer_id, self.customers))

        if rented_dvd in customer.rented_dvds:
            customer.rented_dvds.remove(rented_dvd)
            rented_dvd.is_rented = False
            return f"{customer.name} has successfully returned {rented_dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        output = []
        for customer in self.customers:
            output.append(str(customer))

        for dvd in self.dvds:
            output.append(str(dvd))

        return "\n".join(output)


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
