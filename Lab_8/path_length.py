import math


def calculate_path_length(path):
    length = 0
    for city_index in range(len(path)):
        length += math.sqrt(
            (path[city_index % len(path)][0] - path[(city_index + 1) % len(path)][0]) ** 2 + (
                    path[city_index % len(path)][1] - path[(city_index + 1) % len(path)][1]) ** 2)
    return length
