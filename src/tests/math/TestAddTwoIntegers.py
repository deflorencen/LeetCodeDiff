import pytest
from src.tasks.math.AddTwoIntegers import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (1, 2, 3),
        (-5, 5, 0),
        (0, 0, 0),
        (100, 200, 300),
        (-10, -20, -30)
    ]
)
def test_sum(solution, num1, num2, expected):
    assert solution.sum(num1, num2) == expected


