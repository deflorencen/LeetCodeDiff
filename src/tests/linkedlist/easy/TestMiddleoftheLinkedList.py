import pytest
from src.tasks.linkedlist.MiddleoftheLinkedList import Solution, build_linked_list, to_list

@pytest.mark.parametrize("input_list, expected_output", [
    ([1], [1]),
    ([1, 2], [2]),
    ([1, 2, 3], [2, 3]),
    ([1, 2, 3, 4], [3, 4]),
    ([10, 20, 30, 40, 50], [30, 40, 50]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
])
def test_middle_node(input_list, expected_output):
    head = build_linked_list(input_list)
    middle = Solution.middleNode(head)
    result = to_list(middle)
    assert result == expected_output

def test_empty_list():
    result = Solution.middleNode(None)
    assert result is None