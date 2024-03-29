"""
Create a generator function called possible_permutations() which should receive a list and return lists with all
possible permutations between its elements.
"""
from itertools import permutations


def possible_permutations(numbers_list):
    for element in permutations(numbers_list):
        yield list(element)
