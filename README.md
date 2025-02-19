# Introducing PythonTA (SIGCSE '25 tutorial)

Hello! This repository contains materials for _Introducing Python: A Suite of Code Analysis and Visualization Tools_, a tutorial held at the [2025 Technical Symposium on Computer Science Education (SIGCSE TS)](https://sigcse2025.sigcse.org/).

On this page you'll find information about tutorial logistics and (lightweight) software setup.
If you have any questions about the tutorial, please contact David Liu at [david@cs.toronto.edu](mailto:david@cs.toronto.edu).

As we get closer to the date of the tutorial, additional materials and demos will be posted in this respository.
Participants will be notified by email when all materials are present.

## Tutorial logistics

**When**: Wednesday February 26 2025, 7-10pm

**Where**: Meeting rooms 306-307, [David L. Lawrence Convention Center (DLCC)](https://www.pittsburghcc.com/) in Pittsburgh, Pennsylvania ([Venue floor plan](https://sigcse2025.sigcse.org/attending/Venue))

**Organizer**: [David Liu](https://www.cs.toronto.edu/~david/), University of Toronto

**What you'll need**: a laptop with the [necessary software installed](#software-setup)

## Software setup

PythonTA is a Python library, and can be installed using standard Python packaging tools like pip.

Steps:

1. Download [Python](https://www.python.org/downloads/).
    - I'll be using Python 3.13 during the workshop
    - Older versions: PythonTA is compatible with Python 3.10+
2. Open up a terminal and install the `python-ta` package, including some extra dependencies:

    ```console
    # Windows
    $ python -m pip install 'python-ta[z3,cfg]'

    # macOS/Linux
    $ python3 -m pip install 'python-ta[z3,cfg]'
    ```

3. To check your installation, run the following command. You should see `2.10.0` printed out.

    ```console
    # Windows
    $ python -m python_ta --version

    # macOS/Unix
    $ python3 -m python_ta --version

While the bulk of PythonTA's functionality is implemented in pure Python, some of its visualizations require additional software to be installed:

1. Install [Graphviz](https://graphviz.org/download/), a graph visualization software. PythonTA uses this to visualize control flow graphs.
    - If prompted during the installation, ensure that Graphviz is added to your PATH
    - After the installation, you can verify the installation by running the following in a terminal:

        ```console
        $ dot -V
        dot - graphviz version 12.2.1 (20241206.2353)
        ```

2. Install [Node.js](https://nodejs.org/en/download), a Javascript engine. PythonTA uses a Javascript package called [memory-viz](https://github.com/david-yz-liu/memory-viz) to create memory model diagrams.
    - Please verify the installation by running the following in a terminal:

    ```console
    $ node --version   # Older versions (v20, v18) should be fine
    v22.14.0
    $ npx --version    # Same here
    11.1.0

## Additional resources

If you're interested in learning more about the project, please check out the [GitHub repository](https://github.com/pyta-uoft/pyta) and the [project documentation](https://www.cs.toronto.edu/~david/pyta/).
