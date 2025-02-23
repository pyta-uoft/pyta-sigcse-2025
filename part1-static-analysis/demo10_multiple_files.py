"""This file illustrates how to use PythonTA to check a collection of files.
"""


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(
        [
            'demo1_formatting_checks.py',
            'demo2_logic_checks.py',
            'demo3_style_checks.py',
            'demo4_forbidden_usage_checks.py'
        ],
        config={'output-format': 'python_ta.reporters.PlainReporter'}
    )
