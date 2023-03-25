"""
Create a generator function called get_primes() which should receive a list of integer numbers and return a list
containing only the prime numbers from the initial list.
"""
from math import sqrt


def get_primes(numbers_list):
    for number in numbers_list:
        if number < 2:
            continue
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                break
        else:
            yield number
