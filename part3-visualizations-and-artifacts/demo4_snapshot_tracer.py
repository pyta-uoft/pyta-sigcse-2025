"""Demo file to illustrate how to use PythonTA to create an interactive web visualization
of an executing block of code.

This requires Node.js to be installed (https://nodejs.org/en/download/current).
"""
from __future__ import annotations

from python_ta.debug import SnapshotTracer


def add_to_each(table: list[list[int]], number: int) -> None:
    """Append <number> to each row in the table."""
    with SnapshotTracer(output_directory='_out',
                        webstepper=True,
                        memory_viz_args=['--width=1000']):
        for row in table:
            row.append(number)


if __name__ == '__main__':
    row = [10, 20, 30]
    table = [row, row, row]
    add_to_each(table, 99)
    print(table)
