"""Unit tests for the functions conatined in dictionary.py."""

__author__ = "730560351"


from dictionary import invert, favorite_color, count


# Unit tests for invert
def test_invert_empty_dict() -> None: 
    """Use case test for invert(). This test tests what invert will return when it recieves an empty dictionary."""
    assert invert({}) == {}


def test_invert_one_value() -> None: 
    """Edge case test for invert(). Tests invert when only given one key in the dictionary."""
    inp_dict: dict[str, str] = {'apple': 'cat'}
    assert invert(inp_dict) == {'cat': 'apple'}


def test_invert_multiple_values() -> None: 
    """Edge case test for invert(). Tests invert when the dictionary ƒit recieves has multiple keys."""
    inp_dict: dict[str, str] = {'kettle': 'corn', 'mac': 'cheese'}
    assert invert(inp_dict) == {'corn': 'kettle', 'cheese': 'mac'}


# Unit tests for favorite_color
def test_favorite_color_empty_dict() -> None: 
    """Use case test for favorite_color(). This test tests what favorite_color will return when it recieves an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_one_value() -> None: 
    """Edge case test for favorite_color(). This test tests favorite_color() when it only recieves one key in the dictionary."""
    inp_dict: dict[str, str] = {"mark": "blue"}
    assert favorite_color(inp_dict) == "blue"


def test_favorite_color_multiple_values() -> None: 
    """Edge case test for favorite_color(). Tests favorite_color() when the input list has multiple keys and values."""
    inp_dict: dict[str, str] = {"mark": "blue", "bryan": "blue"}
    assert favorite_color(inp_dict) == "blue"


# Unit tests for count
def test_count_empty_list() -> None:
    """Use case test for count(). This test tests what count will return when it recieves an empty list."""
    assert count([]) == {}


def test_count_one_value() -> None: 
    """Edge case test for count(). Tests the count function when the list it recieves only has one value."""
    inp_list: list[str] = ["Chicken"]
    assert count(inp_list) == {"Chicken": 1}


def test_count_multiple_same() -> None: 
    """Edge case test for count(). Tests count when the input list contains multiple of the same string."""
    inp_list: list[str] = ["beef", "beef"]
    assert count(inp_list) == {"beef": 2}