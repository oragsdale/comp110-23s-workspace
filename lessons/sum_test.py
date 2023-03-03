"""Unit tests for sum function"""

from lessons.sum import sum_new

def test_empty() -> None:
    assert sum_new([]) == 0.0

def test_one_element() -> None: 
    test_list: list[float] = [0.0]
    assert sum_new(test_list) == 0.0

def test_many() -> None:
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert sum_new(test_list) == 6.0

def test_many_with_negatives() -> None:
    test_list: list[float] = [1.0, -2.0, 1.0]
    assert sum_new(test_list) == 0.0