"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730560351"


class Simpy:
    """Simpy class."""

    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values):
        """Initialize the vlaues attribute of newly constructed objects."""
        self.values = values

    def __str__(self) -> str: 
        """Create a string representation of Simpy objects."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, num: int) -> None:
        """Fill a Simpy's values with a specific numbher of repeating values."""
        new_list: list[float] = []
        for item in range(num):
            new_list.append(value)
        self.values = new_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values attribute with range of values in terms of floats."""
        assert step != 0.0
        if step > 0: 
            value: float = start
            while value < stop: 
                self.values.append(value)
                value += step
        else: 
            value: float = start
            while value > stop: 
                self.values.append(value)
                value += step
        
    def sum(self) -> float:
        """Compute and returns the sum of all items in values attribute."""
        total: float = sum(self.values)
        return total
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Utilize __add__ magic method."""
        if type(rhs) == float:
            new: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new.values.append(self.values[idx] + rhs)
                idx += 1

        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new.values.append(self.values[idx] + rhs.values[idx])
                idx += 1        
        return new
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Utilize the power operator in conjunction with Simpy objects and floats."""
        if type(rhs) == float:
            new: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new.values.append(self.values[idx] ** rhs)
                idx += 1
            return new

        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new.values.append(self.values[idx] ** rhs.values[idx])
                idx += 1
            return new
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask based on the equality of each item in teh values attribute with some other Simpy object or float value."""
        if type(rhs) == float: 
            new_list: list[bool] = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == rhs:
                    new_list.append(True)
                else: 
                    new_list.append(False)
                idx += 1
            return new_list
        
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new_list: list[bool] = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == rhs.values[idx]:
                    new_list.append(True)
                else: 
                    new_list.append(False)
                idx += 1
            return new_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask based on the greater than relationsh9ip between each item in the values attribute wth some other Simpy or float value."""
        if type(rhs) == float: 
            new_list: list[bool] = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > rhs:
                    new_list.append(True)
                else: 
                    new_list.append(False)
                idx += 1
            return new_list
        
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new_list: list[bool] = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > rhs.values[idx]:
                    new_list.append(True)
                else: 
                    new_list.append(False)
                idx += 1
            return new_list
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]: 
        """Implement subscription operator with Simpy objects."""
        if type(rhs) == int:
            idx: int = 0
            while idx < len(self.values):
                if rhs == idx: 
                    return self.values[idx]
                idx += 1
        else:
            result: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                if rhs[idx] is True:
                    result.values.append(self.values[idx])
                idx += 1
            return result