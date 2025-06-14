import pytest
from src.tasks.math.easy.NumberofStepstoReduceaNumbertoZero import Solution

@pytest.fixture
def example_input():
    return 30

@pytest.fixture
def example_output():
    return 8

def test_value(example_input, example_output):
    result = Solution.numberOfSteps(example_input)
    assert result == example_output

@pytest.mark.parametrize("input_value, expected", [
    (0, 0),
    (1, 1)
])
def test_edge(input_value, expected):
    result = Solution.numberOfSteps(input_value)
    assert result == expected

@pytest.mark.parametrize("input_value, expected", [
    (14, 6),
    (123, 12),
    (8, 4),
    (1024, 11),
])
def test_typical_cases(input_value, expected):
    assert Solution.numberOfSteps(input_value) == expected

@pytest.mark.parametrize("input_value", [
    "10",
    3.14,
    None,
    [5],
    {"num": 4}
])
def test_invalid_types(input_value):
    if not isinstance(input_value, int):
        with pytest.raises(TypeError):
            raise TypeError("Input must be an integer")