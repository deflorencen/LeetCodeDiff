import pytest
from src.tasks.array.easy.RichestCustomerWealth import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("input_value, expected", [
    ([[1, 2, 3], [3, 2, 1]], 6),
    ([[1_000_000, 1_000_000], [10, 20]], 2_000_000),
    ([[0, 0], [0, 0]], 0),
    ([[], [1, 2]], 3),
    ([[42]], 42),
    ([[1, 1]] * 1000, 2),
    ([], 0),
])
def test_different_value(solution, input_value, expected):
    assert solution.maximumWealth(input_value) == expected