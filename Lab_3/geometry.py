import math


class Circle:
    radius = 0

    def __init__(self, radius):
        if radius <= 0:
            raise ArithmeticError
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        return 2 * self.radius * math.pi


class Triangle:
    a = 0
    b = 0
    c = 0

    def __init__(self, a, b, c):
        if a >= b + c or b >= a + c or c >= a + b or a <= 0 or b <= 0 or c <= 0:
            raise ArithmeticError
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class Square:
    a = 0

    def __init__(self, a):
        if a < 0:
            raise ArithmeticError
        self.a = a

    def perimeter(self):
        return self.a * 4

    def area(self):
        return self.a ** 2
