"""Demo file to illustrate how PythonTA can check function pre- and postconditions dynamically.
"""
from __future__ import annotations
from python_ta.contracts import check_contracts


@check_contracts
def inner_product(v1: list[int], v2: list[int]) -> int:
    """Return the inner product of v1 and v2.

    Preconditions:
    - len(v1) == len(v2)
    """
    result = 0
    for x1, x2 in zip(v1, v2):
        result += x1 * x2
    return result


@check_contracts
def binary_search(numbers: list[int], x: int) -> int:
    """Return the index of an occurrence of x in numbers, or -1 if it doesn't appear.

    Preconditions:
    - is_sorted(numbers)

    Postconditions:
    - $return_value == -1 or numbers[$return_value] == x
    """
    i = 0
    j = len(numbers)
    while i < j:
        mid = i + (j - i) // 2
        if numbers[mid] == x:
            return mid
        elif numbers[mid] < x:
            i = mid + 1
        else:
            j = mid

    # Bug: incorrect value is returned
    return mid


def is_sorted(numbers: list[int]) -> bool:
    """Returns whether numbers is sorted in non-decreasing order.
    """
    for i in range(0, len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


if __name__ == '__main__':
    # This is a valid call to inner_product
    print(inner_product([1, 2, 3], [4, 5, 6]))

    # This is an invalid call to inner_product (try it!)
    # inner_product([1, 2, 3], [4, 5])

    # This is a valid call to binary_search
    numbers = [10, 20, 30, 40, 50]
    print(binary_search(numbers, 30))

    # This is an invalid call to binary_search (violates precondition)
    # binary_search([10, 30, 20, 40, 50], 30)

    # This call to binary_search reveals a bug (-1 is not returned)
    # binary_search(numbers, 60)
