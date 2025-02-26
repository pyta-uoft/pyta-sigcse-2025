"""This file illustrates some short programming exercises that incorporate check_contracts
"""
from __future__ import annotations
from python_ta.contracts import check_contracts


# Exercise 1:
# Given the following function, translate the English preconditions into valid Python syntax.
# Check your work using PythonTA by calling your function on inputs that violate the preconditions.
@check_contracts
def replace_n_times(numbers: list[int], new_item: int, old_item: int, n: int) -> None:
    """Replace the first <n> occurrences of <old_item> with <new_item> in <numbers>.

    Preconditions:
    - n is positive
    - old_item appears at least n times in numbers
    - new_item and old_item are distinct numbers

    Postconditions:
    - new_item appears at least n times in numbers
    """
    # Here's a sample implementation
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == old_item:
            numbers[i] = new_item
            count += 1


# Exercise 2:
# Given the following class, write two representation invariants in Python
# syntax that would be appropriate to enforce.
# Check your work using PythonTA by creating instances of this class that
# violate your representation invariants; you should see an AssertionError.
@check_contracts
class Person:
    """A class representing a person.

    Representation Invariants:
    - ...
    - ...
    """
    given_name: str        # The person's given name
    family_name: str       # The person's family name
    age: int               # The person's age (in years)
    friends: list[Person]  # A list of the person's friends

    def __init__(self, given_name: str, family_name: str, age: int) -> None:
        """Initialize a new person."""
        self.given_name = given_name
        self.family_name = family_name
        self.age = age
        self.friends = []
