"""Demo file to illustrate PythonTA's formatting checks.

Most of these are based on checks detected by pycodestyle:
https://pycodestyle.pycqa.org/en/latest/
"""

def my_function()->int:
    """This function illustrates some poor code formatting.
    """


    x=1
    y =    x * 1;
    return y




if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'output-format': 'python_ta.reporters.PlainReporter'
    })
