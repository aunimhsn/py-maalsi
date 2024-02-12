from typing import Self
from math import sqrt

class Point2D:
    
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def distance_to_other(self, other:Self):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


if __name__ == '__main__':
    point_a = Point2D(2, 4)
    point_b = Point2D(2, 5)

    print(point_a.distance_from_origin())
    print(point_a.distance_to_other(point_b))
    