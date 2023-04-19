from __future__ import annotations

class Point: 

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def scale(self, factor: float) -> Point: 
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p1.x)
print(p1.y)