"""Demo file to illustrate how PythonTA can check type annotations dynamically.
"""
from __future__ import annotations
from python_ta.contracts import check_contracts


@check_contracts
def add_to_list(numbers: list[int], new_num: int, n: int) -> list[int]:
    """Return a new list containing the elements of numbers followed by <new_num> repeated <n> times.
    """
    if n <= 0:
        return numbers.copy()
    elif n == 1:
        return numbers.append(new_num)  # This line has a bug!
    else:
        return numbers + ([new_num] * n)


if __name__ == '__main__':
    # Here is a valid call to transform
    print(add_to_list([1, 2, 3], 10, 4))

    # The following calls illustrate calling transform with arguments of invalid types.
    # Try calling them one at a time!
    # add_to_list([1, 2, 3], 'PythonTA', 10)
    # add_to_list([1, 2, '3'], 10, 4)

    # The following call illustrates calling transform and illustrating a bug:
    # the return value has the wrong type!
    # add_to_list([1, 2, 3], 10, 1)
