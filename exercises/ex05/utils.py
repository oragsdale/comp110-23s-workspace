"""EX05 list utility functions"""

__author__ = "730560351"


def only_evens(input: list[int]) -> list[int]:
    """Given a list of ints, only_evens will return a new list containing only the even elements of the input list."""
    even_list: list[int] = []
    for item in input:
        if item % 2 == 0:
            even_list.append(item)
        
    return even_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Given two lists of ints, concat will return a new list containing all elements of both lists."""
    new_list : list[int] = []
    for item in xs:
        new_list.append(item)
    for item2 in ys:
        new_list.append(item2)

    return new_list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, and a start and end index, sub generates a list which contains the values of the given list within the given indexes."""
    if len(input_list) == 0 or start >= len(input_list) or end == 0:
        return input_list

    if start < 1:
        start = 0

    if end > len(input_list):
        end = input_list[-1]
    
    new_list: list[int] = []
    for item in range(start, end):
        new_list.append(input_list[item])
        
    return new_list