from closest_neighbour import closest_neighbour
from path_length import calculate_path_length


def main():
    # read the path from the file
    path = []
    with open('TSP.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                index, x, y = line.split()
                path.append((float(x), float(y)))
    # path from the files
    print(calculate_path_length(path))
    # closest neighbour starting at a random point
    print(calculate_path_length(closest_neighbour(path)))


if __name__ == '__main__':
    main()
