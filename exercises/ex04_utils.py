"""ex04 list utility functions."""
__author__ = "730560351"


def all(input: list[int], x: int) -> bool: 
    """All compares a list of integers to a single integer, then determines whether all the integers in the list are the same as the single integer."""
    if len(input) == 0:
        raise ValueError("all() arg is an empty List")
        
    idx = 0
    while idx < len(input):
        if input[idx] != x:
            return False
        idx += 1

    return True


def max(input: list[int]) -> int:
    """Max receives a list of integers, then determines the largest integer from this list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empy List")

    largest: int = input[0]
    idx = 0
    while idx < len(input):
        if input[idx] > largest:
            largest = input[idx]
        idx += 1
    
    return largest


def is_equal(input_a: list[int], input_b: list[int]) -> bool: 
    """is_equal compares two lists and determines whether all values within each list are equal."""
    idx = 0
    while idx < len(input_a) or idx < len(input_b):
        if idx >= len(input_a) or idx >= len(input_b):
            return False
        else:
            if input_a[idx] != input_b[idx]:
                return False
        idx += 1
    
    return True