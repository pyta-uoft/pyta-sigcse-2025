"""Demo file to illustrate PythonTA's code style and documentation checks.
"""
from __future__ import annotations


def calculate_sum(numbers: list[int]) -> int:
    """Return the sum of all the numbers in the list."""
    current_sum = 0
    for i in range(len(numbers)):
        current_sum += numbers[i]
    return current_sum


def greet(age: int) -> str:
    """Return a greeting based on the given age."""
    if 10 < age and age < 13:
        return 'Hi!'
    else:
        return 'Hello'


# After running this file once, try uncommenting below and running it again
# def function_no_doc(x):
#     return x + 1


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.PlainReporter'
    })
