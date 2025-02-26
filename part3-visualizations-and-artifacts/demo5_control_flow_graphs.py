"""This file illustrates how to use PythonTA to generate control flow graphs.

Note: this requires Graphviz to be installed and its executables to be on your PATH.
"""
from __future__ import annotations


def simple(n: int) -> int:
    """A simple function to illustrate a control flow graph."""
    x = 1
    if n > 0:
        y = x + n
    else:
        y = x + 1
    x += y
    return x


def greet(age: int) -> str:
    """Return an age-appropriate greeting.

    Preconditions:
    - age >= 0
    """
    if age >= 100:
        result = 'Wow, good for you!'
    elif age >= 18:
        result = 'Hello, you adult, you'
    elif age <= 17:
        result = 'Hi!'

    return result


def search_v1(numbers: list, x: int) -> int:
    """Return an index in numbers where x appears, or -1 if x doesn't appear.
    """
    for i in range(0, len(numbers)):
        if numbers[i] == x:
            return i

    return -1


def search_v2(numbers: list, x: int) -> int:
    """Return an index in numbers where x appears, or -1 if x doesn't appear.
    """
    for i in range(0, len(numbers)):
        if numbers[i] == x:
            return i
        else:
            return -1  # Bug!


def compare_counts_v1(numbers: list[int], x: int, y: int) -> bool:
    """Compare the number of occurrences of <x> and <y> in <numbers>."""
    count_x, count_y = 0, 0
    for number in numbers:
        if number == x:
            count_x += 1
        elif number == y:
            count_y += 1

    return count_x <= count_y


def compare_counts_v2(numbers: list[int], x: int, y: int) -> bool:
    """Compare the number of occurrences of <x> and <y> in <numbers>."""
    count_x, count_y = 0, 0
    for number in numbers:
        if number == x:
            count_x += 1
        if number == y:
            count_y += 1

    return count_x <= count_y


if __name__ == '__main__':
    from python_ta.cfg import generate_cfg

    generate_cfg(
        visitor_options={
            # Try commenting/uncommenting each of the versions below
            'functions': ['simple'],
            # 'functions': ['greet'],
            # 'functions': ['search_v1', 'search_v2'],
            # 'functions': ['compare_counts_v1', 'compare_counts_v2'],
            'separate-condition-blocks': True
        },
        auto_open=True
    )
