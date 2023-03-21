"""Unit tests for ex05 utils."""

__author__ = "730560351"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty() -> None:
    """Tests each function when receiving an empty list."""
    assert only_evens([]) == []
    assert sub([], 1, 2) == []
    assert concat([], []) == []


def test_only_evens() -> None:
    """Tests only_evens when receiving a list of only even numbers."""
    even_test_list: list[int] = [2, 4, 6]
    assert only_evens(even_test_list) == even_test_list


def test_only_odds() -> None:
    """Tests only_evens when receiving only a list of odd numbers."""
    odd_test_list: list[int] = [1, 3, 5]
    assert only_evens(odd_test_list) == []


def test_concat_one_empty() -> None:
    """Tests concat when one of the lists received is an empty list."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == test_list1


def test_concat_one_item() -> None:
    """Tests concat when each list only has one item."""
    test_list1: list[int] = [1]
    test_list2: list[int] = [2]
    assert concat(test_list1, test_list2) == [1, 2]


def test_sub_start_greater_end() -> None:
    """Tests sub when the start value is greater than the end value."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    test_start: int = 4
    test_end: int = 2
    assert sub(test_list, test_start, test_end) == []


def test_sub_negative() -> None:
    """Tests sub with a negative start index."""
    test_list: list[int] = [1, 2, 3, 4]
    test_start: int = -1
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [1, 2, 3]