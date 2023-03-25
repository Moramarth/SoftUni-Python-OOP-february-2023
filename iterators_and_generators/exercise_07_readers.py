"""
Create a generator function called read_next() which should receive a different number of arguments (all iterable).
On each iteration, the function should return each element from each sequence.
"""


def read_next(*args):
    for item in args:
        for element in item:
            yield element
