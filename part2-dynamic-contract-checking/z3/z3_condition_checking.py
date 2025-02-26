"""Demo file to illustrate how PythonTA can incorporate Z3 when analysing
if conditions.

Note: this requires the z3-solver Python library to be installed.
"""
from __future__ import annotations


def greet_v1(age: int) -> str:
    """Return an age-appropriate greeting.

    Preconditions:
    - age >= 0
    """
    if age >= 18:
        return 'Hello, you adult, you'
    elif age >= 100:                    # This condition will never be true
        return 'Wow, good for you!'
    else:
        return 'Hi!'


def greet_v2(age: int) -> str:
    """Return an age-appropriate greeting.

    Preconditions:
    - age >= 0
    """
    if age < 0:  # This condition will never be true
        return 'You are not born yet'
    elif age >= 18:
        return 'Hello, you adult, you'
    else:
        return 'Hi!'


def calculate(x: int, numbers: list[int]) -> int:
    """Return the sum of <numbers> multiplied by <x>."""
    if x == 0:
        return 0

    current_sum = 0
    for number in numbers:
        if x != 0:
            current_sum += number * x
    return current_sum


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.PlainReporter',

        # Try switching the z3 option value between True and False
        'z3': True,
    })
