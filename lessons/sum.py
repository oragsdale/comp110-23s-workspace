"""Example function for unit tests"""

__author__ = "730560351"

def sum_new(xs: list[float]) -> float:
    """return sum off all elements in xs"""
    sum_total: float = 0.0
    for item in xs:
        sum_total += item
    return sum_total