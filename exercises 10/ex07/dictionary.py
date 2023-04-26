"""The function skeletons for ex07 will be implemented within this file."""


__author__ = "730560351"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Invert returns a new dictionary which contains the values of the input dictionary as its keys, and the keys of the input dictionary as its values."""
    new_dict: dict[str, str] = {}
    for key in inp_dict:
        if inp_dict[key] in new_dict:
            raise KeyError("There cannot be two of the same key in a dictionary.")
        else:
            new_dict[inp_dict[key]] = key

    return new_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Favorite_color returns the string within the input dictionary that occurs the most as a value."""
    blue: int = 0
    yellow: int = 0
    for key in inp_dict: 
        if inp_dict[key] == "blue":
            blue += 1
        elif inp_dict[key] == "yellow":
            yellow += 1
    
    if blue > yellow:
        return "blue"
    elif blue < yellow:
        return "blue"
    elif len(inp_dict) == 0: 
        return ""
    elif blue == yellow: 
        return list(inp_dict.values())[0]


def count(inp_list: list[str]) -> dict[str, int]:
    """Count counts the number of times a unique value in the input list appears then assigns this count to  a dictionary."""
    new_dict: dict[str, int] = {}
    for item in inp_list: 
        if item in new_dict:
            new_dict[item] += 1
        else: 
            new_dict[item] = 1

    return new_dict