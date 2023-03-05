class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price) -> str:
        if price <= self.__budget:
            if self.__animal_capacity > len(self.animals):
                self.__budget -= price
                self.animals.append(animal)
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough space for animal"

        return f"Not enough budget"

    def hire_worker(self, worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        money_owned_to_workers = sum([worker.salary for worker in self.workers])
        if money_owned_to_workers <= self.__budget:
            self.__budget -= money_owned_to_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed_for_animals = sum([animal.money_for_care for animal in self.animals])
        if money_needed_for_animals <= self.__budget:
            self.__budget -= money_needed_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        output = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]

        for lion in lions:
            output.append(lion.__repr__())

        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        output.append(f"----- {len(tigers)} Tigers:")

        for tiger in tigers:
            output.append(tiger.__repr__())

        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        output.append(f"----- {len(cheetahs)} Cheetahs:")

        for cheetah in cheetahs:
            output.append(cheetah.__repr__())

        return "\n".join(output)

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        output = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]

        for keeper in keepers:
            output.append(keeper.__repr__())

        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        output.append(f"----- {len(caretakers)} Caretakers:")

        for caretaker in caretakers:
            output.append(caretaker.__repr__())

        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        output.append(f"----- {len(vets)} Vets:")

        for vet in vets:
            output.append(vet.__repr__())

        return "\n".join(output)
