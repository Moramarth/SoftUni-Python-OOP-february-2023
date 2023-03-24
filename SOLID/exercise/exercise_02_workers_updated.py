"""
The saga with the workforce continues.

Test examples provided at the end of file.
"""


from abc import ABC, abstractmethod
import time


class HaveToWork(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class MustEatToLive(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        pass


class NeedsMaintenanceToFunction(ABC):
    @staticmethod
    @abstractmethod
    def maintenance():
        pass


class Worker(HaveToWork, MustEatToLive):
    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(2 secs)")
        time.sleep(2)


class SuperWorker(HaveToWork, MustEatToLive):
    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(1 secs)")
        time.sleep(1)


class Robot(HaveToWork, NeedsMaintenanceToFunction):
    @staticmethod
    def work():
        print("I'm a robot. I'm working....")

    @staticmethod
    def maintenance():
        print("Maintenance in progress.... (2 seconds)")
        time.sleep(2)


class ManagerModel(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(ManagerModel):
    def set_worker(self, worker):
        assert isinstance(worker, HaveToWork), f"`worker` must be of type {HaveToWork}"

        self.worker = worker
        time.sleep(1)

    def manage(self):
        self.worker.work()


class BreakManager(ManagerModel):
    def set_worker(self, worker):
        assert isinstance(worker, MustEatToLive), f"`worker` must be of type {MustEatToLive}"

        self.worker = worker
        time.sleep(1)

    def lunch_break(self):
        self.worker.eat()


class MaintenanceManager(ManagerModel):
    def set_worker(self, worker):
        assert isinstance(worker, NeedsMaintenanceToFunction), f"`worker` must be of type {NeedsMaintenanceToFunction}"

        self.worker = worker
        time.sleep(1)

    def scheduled_maintenance(self):
        self.worker.maintenance()


motivator = WorkManager()
chef = BreakManager()
mechanical_engineer = MaintenanceManager()

normal_worker = Worker()
super_worker = SuperWorker()
robot_worker = Robot()
workforce = [normal_worker, super_worker, robot_worker]

for worker_instance in workforce:
    try:
        motivator.set_worker(worker_instance)
        motivator.manage()
    except AssertionError as error:
        print(error)

    try:
        chef.set_worker(worker_instance)
        chef.lunch_break()
    except AssertionError as error:
        print(error)

    try:
        mechanical_engineer.set_worker(worker_instance)
        mechanical_engineer.scheduled_maintenance()
    except AssertionError as error:
        print(error)
