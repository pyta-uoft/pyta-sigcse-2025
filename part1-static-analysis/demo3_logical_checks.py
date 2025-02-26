"""Demo file to illustrate PythonTA's code correctness checks.
"""
from __future__ import annotations


def search(numbers: list[int], item: int) -> str:
    """Return 'Found' if <item> appears in <numbers>, and
    'Not found' otherwise.
    """
    for number in numbers:
        if number == item:
            return 'Found'
        else:
            return 'Not found'


def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of the given numbers."""
    current_sum = None
    for number in numbers:
        current_sum += number
    return current_sum


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.PlainReporter'
    })
