import pytest
from src.tasks.string.easy.RansomNote import Solution

@pytest.mark.parametrize("input_value, magazine, expected", [
    ("a", "b", False),              # basic case — letter is missing
    ("aa", "aab", True),            # enough letters
    ("aa", "ab", False),            # missing one letter
    ("", "abc", True),              # empty ransom note — always True
    ("abc", "", False),             # no letters — False
    ("abc", "abc", True),           # exact match
    ("aaa", "aaaaa", True),         # extra letters
    ("abcd", "abc", False),         # missing 'd'
])
def test_can_construct(input_value, magazine, expected):
    result = Solution.canConstruct(input_value, magazine)
    assert result == expected