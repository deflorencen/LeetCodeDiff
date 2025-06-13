import pytest
from src.tasks.math.easy.FizzBuzz import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.fixture
def example_input():
    return 23

@pytest.fixture
def example_output():
    return ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16',
            '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23']

def test_default_value(solution, example_input, example_output):
    result = solution.fizzBuzz(example_input)
    assert result == example_output

@pytest.mark.parametrize("invalid_input", [
    "15",
    3.14,
    None,
    [],
    {},
    (5,),
])
def test_non_integer_input_param(invalid_input, solution):
    with pytest.raises(TypeError):
        solution.fizzBuzz(invalid_input)

def test_output_content(solution, example_input):
    result = solution.fizzBuzz(example_input)
    assert all(isinstance(x, str) for x in result)
