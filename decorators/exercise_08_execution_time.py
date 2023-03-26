""" Create a decorator called exec_time. It should calculate how much time a function needs to be executed. """
from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()

        return end_time - start_time
    return wrapper
