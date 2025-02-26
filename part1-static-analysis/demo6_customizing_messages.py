"""Demo file to illustrate PythonTA's ability to customize messages.

Compare the report with the one generated by running demo2_style_checks.py.
"""
from __future__ import annotations


def greet(age: int) -> str:
    """Return a greeting based on the given age."""
    if 10 < age and age < 13:
        return 'Hi!'
    else:
        return "Hello"


def calculate_sum(numbers: list[int]) -> int:
    """Return the sum of all the numbers in the list."""
    current_sum = 0
    for i in range(len(numbers)):
        current_sum += numbers[i]
    return current_sum


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.PlainReporter',
        # NOTE: the path below is relative to the current working directory
        'messages-config-path': 'demo-config/custom_messages.toml'
    })
