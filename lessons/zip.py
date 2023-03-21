"""Challenge quesition 04 Dictionary function writing"""

__author__ = "730560351"

def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """The function zip produces a dictionary using the items of the first list as the keys, and the items of the second list as the values."""
    if len(keys) != len(values):
        return {}
    if len(keys) and len(values) == 0:
        return {}

    new_dict: dict[int] = {}

    idx: int = 0
    while idx < len(keys):
        new_dict[keys[idx]] = values[idx]
        idx += 1

    return new_dict