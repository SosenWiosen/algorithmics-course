import math
import random


def main():
    print(circle_area(1))
    print(sin_area(0, 2))


def monte_carlo(check_if_inside, a, b, n):
    max_v = 2
    min_v = -2
    inside = 0
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(min_v, max_v)
        if check_if_inside(x, y):
            inside += 1
    return (inside / n) * (max_v - min_v) * (b - a)


def circle_area(r):
    return monte_carlo(lambda x, y: x * x + y * y < r, -r, r, 1000000)


def check_if_under_sin(x, y):
    if math.sin(x) > y > 0:
        return True
    return False


def sin_area(a, b):
    return monte_carlo(check_if_under_sin, a, b, 1000000)


if __name__ == '__main__':
    main()
