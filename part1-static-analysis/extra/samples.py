"""This file contains some additional samples of (incorrect) solutions to
some short programming exercises. These are synthesized from common
student errors instructors have encountered at the University of Toronto.

Try running python_ta.check_all() and exploring the report!
"""
from __future__ import annotations


def first_even_v1(numbers: list[int]) -> int:
    """Return the first even number from <numbers>,
    or 0 if there are no even numbers.
    """
    for number in numbers:
        if number % 2 == 0:
            return nubmer

    return 0


def first_even_v2(numbers: list[int]) -> int:
    """Return the first even number from <numbers>,
    or 0 if there are no even numbers.
    """
    count = 0
    for i in range(len(numbers)):
        if numbers[i]%2 ==0:
            count += 1
        if count > 0:
            return numbers[i]
        elif count == 0:
            return count


def first_even_v3(numbers: list[int]) -> int:
    """Return the first even number from <numbers>,
    or 0 if there are no even numbers.

    NOTE: This version illustrates two technical limitations with PythonTA:
    1. It reports a "missing return statement" error even though the condition
       `if flag is False` will always be True.
    2. It does *not* report a "redundant assignment" error for the statement
       `flag = True`.
    """
    flag = False
    i = 0
    while flag is False and i < len(numbers):
        if numbers[i] % 2 != 0:
            flag = True
            return numbers[i]
        i += 1

    if flag is False:
        return 0


def contains_word(message: str, word: str) -> bool:
    """Return whether <word> appears in <message>,
    without using the in operator or string slicing.

    >>>contains_word('Example test case', 'test')
    True
    """
    for i in range(len(message)):
        if message[i] == word[0]:
            currIndex = i + 1
            count = 1
            while count < len(word) and currIndex < len(message):
                if message[currIndex] != word[count]:
                    break
                count += 1
                currIndex += 1

            return count == len(word) and currIndex == len(message)

    return False


def sum_nested(numbers: list) -> int:
    """Return the sum of the given numbers.

    numbers is an arbitrarily nested list of numbers.

    >>> sum_nested([[1, 2, [[3]]], [], [[4, 5]]])
    15
    """
    for obj in numbers:
        result = 0
        if isinstance(obj, int):
            result += obj
        else:
            result += sum_nested(obj)

    return result


def partition(items: list) -> int:
    """Partition <items> using items[0] as the pivot.

    Return the index of the pivot.

    Preconditions:
    - items != []
    """
    pivot = 0
    low = 1
    high = len(items)

    while low < high:
        if items[low] <= pivot:
            low += 1
        else:
            # Swap these two items
            items[low], items[high] = items[high], items[low]
            high -= 1

    # Swap the pivot into its correct position, with more variables
    pivot_pos = items[0]
    pivot_new = items[low + 1]
    pivot_pos, pivot_new = items[low + 1], items[0]
    return low + 1


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.HTMLReporter',
        'z3': False,
        'max-nested-blocks': 3
    })
