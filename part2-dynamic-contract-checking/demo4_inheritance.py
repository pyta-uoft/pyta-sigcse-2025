"""Demo file to illustrate how PythonTA contract checking works with inheritance.
"""
from python_ta.contracts import check_contracts

from demo3_class_contracts import Person


@check_contracts
class Student(Person):
    """A student.

    As a subclass of Person, this class "inherits" specifications from Person.

    Representation Invariants:
    - self.school != ''
    """
    school: str

    def __init__(self, name: str, age: int, school: str) -> None:
        """Initialize a new student."""
        super().__init__(name, age)
        self.school = school


if __name__ == '__main__':
    # This creates a valid instance of Student
    student = Student('David', 18, 'University of Toronto')

    # Each of the following are copied from class_specification_checking.py.
    # These illustrate that type annotation and invariants are "inherited" by the Student subclass.

    # This sets the student's age to an invalid value (wrong type)
    # student.age = 'David'

    # This sets the student's age to an invalid value (violates invariant)
    # student.age = -1

    # This calls a method that sets the student's age to an invalid value
    # student.change_age(-100)

    # These statements create invalid instances of Student
    # person2 = Student('David', -100, 'University of Toronto')
    # person3 = Student('David', 100, '')
