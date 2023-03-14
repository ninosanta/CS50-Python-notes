# `assert` keyword in Python is used to test conditions
# and raise an AssertionError if a condition is not met.
# Testing trough try - assert - except implies to write
# a lot of code lines.
# E.g.:
#    try:
#        assert square(2) == 4
#    except AssertionError:
#        print("2 squared was not 4!")
# and so on... for each test case!
#
# `pythest` is a third party library that can automate the
# testing process for you and permits to perform Unit Tests
# (i.e., test of individual functions) without have to write
# tons of code lines.
#
# To install `pytest`:
#    pip install pytest
# Then, to run the test:
#    In the terminal:   `pytest test_calculator.py`
# then, it will check all the asserions.

from calculator import square
import pytest


def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(1) == 1


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):  # expected exception
        square("cat")  # when
