"""Demo file to illustrate PythonTA's autoformatting using Black.

The code in this file is duplicated from demo_1formatting_checks.py,
except the arguments passed to to python_ta.check_all.

For more information on Black, see https://black.readthedocs.io/en/stable/.
"""

def my_function()->int:
    """This function illustrates some poor code formatting.
    """


    x=1
    y =    x * 1;
    return y




if __name__ == '__main__':
    import python_ta
    python_ta.check_all(
        config={
            'output-format': 'python_ta.reporters.PlainReporter',
            'max-line-length': 100,
        },
        autoformat=True,
    )
