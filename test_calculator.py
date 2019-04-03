"""Test cases for calculator.py."""

from calculator import Calculator


class TestCalculator:
    """This class has 4 methods to test add, sub, mul, and div respectively.

    Note that the test class doesn't have a constructor.

    !!Don't forget to check all implementation covered by tests.
    """

    def test_add(self):
        """Test functionality of add method."""
        x = 1.0
        y = 1.0
        calc = Calculator()
        assert calc.add(x, y) == 2.0
