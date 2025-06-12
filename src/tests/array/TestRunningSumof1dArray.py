import pytest
from src.tasks.array.RunningSumof1dArray import Solution


@pytest.fixture
def running_solution_sum_func():
    return Solution.runningSum


# Functional and limit tests with parameterization
@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([5], [5]),
    ([], []),
    ([0, 0, 0], [0, 0, 0]),
    ([10, -5, 3], [10, 5, 8]),
    ([1.5, 2.5, -1.0], [1.5, 4.0, 3.0]),
    ([-1, -2, -3], [-1, -3, -6]),
])
def test_running_sum_functionality(running_solution_sum_func, input_list, expected):
    assert running_solution_sum_func(input_list) == expected


# Check result length = input length
@pytest.mark.parametrize("input_list", [
    [1, 2, 3],
    [10],
    [],
    [0, 0, 0],
])
def test_running_sum_length(running_solution_sum_func, input_list):
    result = running_solution_sum_func(input_list)
    assert len(result) == len(input_list)


# Checking that the function does not change the input list
@pytest.mark.parametrize("input_list", [
    [1, 2, 3],
    [-1, -1],
    [],
])
def test_input_not_mutated(running_solution_sum_func, input_list):
    original = input_list[:]
    running_solution_sum_func(input_list)
    assert input_list == original


# Checking that an error is thrown when an invalid input is entered
@pytest.mark.parametrize("bad_input", [
    None,
    "123",
    123,
    {"a": 1},
    [1, "2", 3],
])
def test_invalid_input(running_solution_sum_func, bad_input):
    with pytest.raises((TypeError, ValueError)):
        running_solution_sum_func(bad_input)