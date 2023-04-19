from __future__ import annotations

class Point: 

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        """Print [rettier version of our point"""
        return f"({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point: 
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled


    def __add__(self, rhs: float) -> Point:
        new_x: float = self.x + rhs
        new_y: float = self.y + rhs
        added_point: Point = Point(new_x, new_y)
        return added_point
        
    
a: Point = Point(1.0, 2.0)
print(a)
b: Point = a + 3.0
print(b)