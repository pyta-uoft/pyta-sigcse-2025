"""This file illustrates how PythonTA can be used to generate memory model diagrams.

This requires Node.js to be installed (https://nodejs.org/en/download/current).
"""
from __future__ import annotations
from python_ta.debug.snapshot import snapshot


def add_to_each(table: list[list[int]], number: int) -> None:
    """Append <number> to each row in the table."""
    snapshot(save=True, memory_viz_args=['--output=snapshot.svg', '--width=1000'])

    for row in table:
        row.append(number)


if __name__ == '__main__':
    row = [10, 20, 30]
    table = [row, row, row]
    add_to_each(table, 99)
    print(table)
