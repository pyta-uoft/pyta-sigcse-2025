"""Demo file to illustrate how PythonTA can be used to generate memory model diagrams
with customization via modifying the raw JSON.

This requires Node.js to be installed (https://nodejs.org/en/download/current).

After running this file, a JSON file snapshot.json will be generated. To render
an SVG file from the JSON, run the command

$ npx memory-viz@latest --output=snapshot2.svg  --width=1000 snapshot.json
"""
from __future__ import annotations
from python_ta.debug.snapshot import snapshot, snapshot_to_json
import json


def add_to_each(table: list[list[int]], number: int) -> None:
    """Append <number> to each row in the table."""
    open('snapshot.json', 'w').write(json.dumps(snapshot_to_json(snapshot()), indent=2))

    for row in table:
        row.append(number)


if __name__ == '__main__':
    row = [10, 20, 30]
    table = [row, row, row]
    add_to_each(table, 99)
    print(table)
