"""
Hello, thank you for the code review.

Test examples provided at the end of file.
"""

from abc import ABC, abstractmethod


class WorkerModel(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(WorkerModel):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(WorkerModel):
    @staticmethod
    def work():
        print("I work very hard!!!")


class LazyWorker(WorkerModel):
    @staticmethod
    def work():
        print("I work because my manager is here")


class NotAWorker:
    @staticmethod
    def not_working():
        print("What is work?")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, WorkerModel), f'`worker` must be of type {WorkerModel}'

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


def manager_is_managing(manager_instance, worker_instance):
    try:
        manager_instance.set_worker(worker_instance)
        manager_instance.manage()
    except AssertionError as error:
        print("Manager cannot handle non workers!", error)


manager = Manager()
normal_worker = Worker()
super_worker = SuperWorker()
lazy_worker = LazyWorker()
not_a_worker = NotAWorker()

manager_is_managing(manager, normal_worker)
manager_is_managing(manager, super_worker)
manager_is_managing(manager, lazy_worker)
manager_is_managing(manager, not_a_worker)
