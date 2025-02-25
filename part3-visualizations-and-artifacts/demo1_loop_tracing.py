"""This file illustrates the use of PythonTA's AccumulationTable context manager.
"""
from python_ta.debug import AccumulationTable


def calculate_sum(numbers: list[int]) -> int:
    """Return the sum of the given numbers."""
    current_sum = 0

    with AccumulationTable(['current_sum']):
        for number in numbers:
            current_sum += number

    return current_sum


def calculate_sum_positives(numbers: list[int]) -> int:
    """Return the sum of the given numbers that are positive."""
    current_sum = 0

    with AccumulationTable(['current_sum']):
        for number in numbers:
            if number > 0:
                current_sum = number  # Bug on this line!

    return current_sum


def euclidean_gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b.

    Preconditions:
    - a >= 0
    - b >= 0

    >>> euclidean_gcd(20, 14)
    2
    >>> euclidean_gcd(16, 96)
    16
    """
    x, y = a, b
    with AccumulationTable(['a', 'b', 'x', 'y']):
        while y > 0:
            x, y = y, x % y

    return x


def extended_euclidean_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the greatest common divisor of a and b, and integers p and q such that:

        a * p + q * b = gcd(a, b)

    Preconditions:
    - a >= 0
    - b >= 0

    >>> extended_euclidean_gcd(20, 14)
    (2, -2, 3)
    >>> 20 * -2 + 14 * 3
    2
    """
    x, y = a, b
    px, qx = 1, 0
    py, qy = 0, 1

    with AccumulationTable(['x', 'y', 'px', 'qx', 'py', 'qy', 'px*a + qx*b', 'py*a + qy*b']):
        while y != 0:
            quotient = x // y
            x, y = y, x % y

            px, qx, py, qy = py, qy, px - quotient * py, qx - quotient * qy

    return x, px, qx


def longest_substring_uniques(s: str) -> int:
    """Return the length of the longest substring of s that contains no repeating characters.

    >>> longest_substring_uniques('abcabcbb')
    3
    >>> longest_substring_uniques('abcabdc')  # 'cabd'
    4
    """
    max_length = 0
    start = 0
    length = 0
    seen = {}

    with AccumulationTable(['s', 's[i]', 'last_seen', 'start', 'length', 's[start:start+length]', 'seen']):
        for i in range(len(s)):
            last_seen = seen.get(s[i], -1)
            if last_seen < start:  # The current substring doesn't have s[i]
                length += 1
                max_length = max(max_length, length)
            else:  # The current substring has s[i]
                start = last_seen + 1
                length = i - last_seen

            seen[s[i]] = i

    return max_length


if __name__ == '__main__':
    result = calculate_sum([10, 20, 30, 40])
    print(result)

    # result = calculate_sum_positives([10, -3, -4, 20, 5])
    # print(result)

    # result = euclidean_gcd(20, 14)
    # print(result)

    # result = extended_euclidean_gcd(20, 14)
    # print(result)

    # result = longest_substring_uniques('abacde')
    # print(result)
