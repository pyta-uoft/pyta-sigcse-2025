"""Demo file to illustrate how PythonTA check_contracts can be used in unit tests.
"""
import unittest
from python_ta.contracts import check_contracts

from demo2_function_contracts import inner_product


class TestInnerProduct(unittest.TestCase):
    """Sample test suite for inner_product."""
    def test_simple(self):
        actual = inner_product([1, 2, 3], [4, 5, 6])
        expected = 32  # 4 + 10 + 18

        self.assertEqual(actual, expected)

    def test_different_input_lengths(self):
        """Test that an AssertionError is raised when given lists of different lengths.
        """
        with self.assertRaises(AssertionError):
            inner_product([1, 2, 3], [4, 5])


###############################################################################

# Assume this function is imported from a student file.
# Note that this function is *not* decorated with check_contracts.
def reciprocal(x: float) -> float:
    """Return the reciprocal of x.

    Preconditions:
    - x != 0
    """
    return 1 / x


class TestReciprocal(unittest.TestCase):
    """Sample test suite for reciprocal."""
    @classmethod
    def setUpClass(cls):
        """Execute before executing tests in this test suite."""
        cls.checked_reciprocal = check_contracts(reciprocal)

    def test_simple(self):
        """A simple test using the wrapped reciprocal."""
        actual = type(self).checked_reciprocal(2.5)
        expected = 0.4  # 2/5

        self.assertAlmostEqual(actual, expected)

    def test_zero(self):
        """This test illustrates that checked_reciprocal was wrapped by check_contracts."""
        with self.assertRaises(AssertionError):
            type(self).checked_reciprocal(0.0)

    def test_zero_original(self):
        """This test illustrates that the original reciprocal function is preserved."""
        with self.assertRaises(ZeroDivisionError):
            reciprocal(0.0)


if __name__ == '__main__':
    unittest.main()
