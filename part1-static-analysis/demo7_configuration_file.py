"""This demo illustrates how to provide PythonTA configuration from an external file. This line is > 80 characters.
"""
from __future__ import annotations
import datetime
import statistics


def do_something(days: list[int]) -> datetime.date:
    """Return a special date."""
    average_delta = datetime.timedelta(days=statistics.mean(days))
    return datetime.date(1867, 7, 1) + average_delta


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='demo-config/.pylintrc')
