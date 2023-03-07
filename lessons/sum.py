"""Example function for unit tests"""

__author__ = "730560351"

def sum(xs: list[float]) -> float:
    """return sum off all elements in xs"""
    sum_total: float = 0.0
    for item in range(0, len(xs)):
        sum_total += xs[item]
    return sum_total