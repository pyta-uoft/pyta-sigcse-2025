"""Demo file to illustrate how PythonTA can check class specifications dynamically.
"""
from __future__ import annotations
from python_ta.contracts import check_contracts


@check_contracts
class Person:
    """A class representing a person.

    Representation Invariants:
    - self.name != ""
    - self.age >= 0
    """
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        """Initialize a new person."""
        self.name = name
        self.age = age

    def change_age(self, diff: int) -> None:
        """Change this person's age by <diff>."""
        self.age += diff


if __name__ == '__main__':
    # This creates a valid instance of Person
    person = Person('Justin Trudeau', 53)

    # This sets the person's age to an invalid value (wrong type)
    # person.age = 'David'

    # This sets the person's age to an invalid value (violates invariant)
    # person.age = -1

    # This calls a method that sets the person's age to an invalid value
    # person.change_age(-100)

    # This creates an invalid instance of Person
    # person2 = Person('David Liu', -10)
