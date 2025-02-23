"""Demo file to illustrate PythonTA's checks for forbidden code usage.
"""
from __future__ import annotations
from math import floor


def calculate_average(a: int, b: int) -> int:
    """Return the average of a and b, rounded down to the nearest integer.

    You may NOT use any functions from the "math" module.
    """
    return floor((a + b) / 2)


def calculate_sum(numbers1: list[int], numbers2: list[int]) -> int:
    """Return the sum of the numbers in both given lists.

    You may NOT use any loops (but instead use an appropriate built-in function).
    """
    current_sum = 0
    for number in numbers1 + numbers2:
        current_sum += number
    return current_sum


def add_one(x: int) -> int:
    """Return x + 1.

    Remember to remove all print statements before submitting your work.
    """
    print(f'This is x: {x}')
    return x + 1


# By default, no top-level code is allowed outside of "if name == main" blocks,
# except imports and constant definitions (identified by ALL_CAPS names).
calculate_sum([1, 2, 3], [4, 5, 6])  # This line will be flagged by PythonTA


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.PlainReporter',
        'disallowed-python-syntax': ['For']
    })
