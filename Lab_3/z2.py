import geometry


def main():
    tri = geometry.Triangle(3, 4, 5)
    print(tri.area())
    print(tri.perimeter())
    circ = geometry.Circle(1)
    print(circ.area())
    print(circ.perimeter())
    sq = geometry.Square(-2)


if __name__ == '__main__':
    main()
