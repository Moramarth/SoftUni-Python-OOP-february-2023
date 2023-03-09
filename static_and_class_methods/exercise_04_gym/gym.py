from static_and_class_methods.exercise_04_gym.customer import Customer
from static_and_class_methods.exercise_04_gym.equipment import Equipment
from static_and_class_methods.exercise_04_gym.exercise_plan import ExercisePlan
from static_and_class_methods.exercise_04_gym.subscription import Subscription
from static_and_class_methods.exercise_04_gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = list()
        self.trainers = list()
        self.equipment = list()
        self.plans = list()
        self.subscriptions = list()

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription_instance = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda c: c.id == subscription_instance.customer_id, self.customers))
        trainer = next(filter(lambda t: t.id == subscription_instance.trainer_id, self.trainers))
        plan = next(filter(lambda p: p.id == subscription_instance.exercise_id, self.plans))
        equipment = next(filter(lambda e: e.id == plan.equipment_id, self.equipment))

        return "\n".join([str(subscription_instance), str(customer), str(trainer), str(equipment), str(plan)])
