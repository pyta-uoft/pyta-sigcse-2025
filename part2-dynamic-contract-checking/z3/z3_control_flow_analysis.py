"""Demo file to illustrate how PythonTA can incorporate Z3 when performing
control-flow-based analysis.

Note: this requires the z3-solver Python library to be installed.
"""


def greet_v3(age: int) -> str:
    """Return an age-appropriate greeting.

    Preconditions:
    - age >= 0
    """
    if age >= 100:
        return 'Wow, good for you!'
    elif age >= 18:
        return 'Hello, you adult, you'
    elif age <= 17:
        return 'Hi!'


def greet_v4(age: int) -> str:
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


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.PlainReporter',

        # Try switching the z3 option value between True and False
        'z3': False,
    })
