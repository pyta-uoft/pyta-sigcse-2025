"""This file contains a brief demo of Z3.

For more information, please see:
- Project documentation: https://github.com/Z3Prover/z3
- Z3 API in Python (tutorial): https://ericpony.github.io/z3py-tutorial/guide-examples.htm
"""
import z3


if __name__ == '__main__':
    x = z3.Int('x')
    y = z3.Int('y')
    z = z3.Int('z')

    z3.solve(
        x * x + y * y == z * z,
        x > 0,
        y > 0,
        z == 0,
    )
