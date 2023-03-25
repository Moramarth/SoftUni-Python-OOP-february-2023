"""
Create a generator function called get_primes() which should receive a list of integer numbers and return a list
containing only the prime numbers from the initial list.
"""
from math import sqrt


def get_primes(numbers_list):
    primes_list = list()
    numbers_list = [num for num in numbers_list if num > 1]
    for number in numbers_list:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                break
        else:
            primes_list.append(number)

    for prime in primes_list:
        yield prime
