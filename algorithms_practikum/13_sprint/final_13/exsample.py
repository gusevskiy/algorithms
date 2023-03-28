import math
from functools import total_ordering


class point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'Point(a={self.a}, b={self.b})'

    @property
    def compare(self):
        return math.sqrt(self.a * self.a + self.b * self.b)

    def __lt__(self, other):
        return self.compare < other.compare


print(sorted([
    point(10, 5), point(30, 10), point(17, 7), point(2, 0)
]))
