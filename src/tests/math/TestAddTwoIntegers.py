import pytest
from src.tasks.math.AddTwoIntegers import add_two_numbers as add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 5) == 5
    assert add(0, 0) == 0

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)

def test_add_mixed_types():
    assert add(3, 2.5) == pytest.approx(5.5)