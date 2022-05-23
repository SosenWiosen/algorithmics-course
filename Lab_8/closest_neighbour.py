import math
from random import randint


def closest_neighbour(path):
    # solve tsp by creating a path in which the closest neighbour gets chosen
    # choose a random starting point first
    start_index = randint(0, len(path) - 1)
    new_path = [path[start_index]]
    path.remove(path[start_index])

    for city_index in range(len(path)):
        closest_city_index = 0
        closest_city_distance = float('inf')
        for city in path:
            distance = math.sqrt((city[0] - new_path[-1][0]) ** 2 + (city[1] - new_path[-1][1]) ** 2)
            if distance < closest_city_distance:
                closest_city_distance = distance
                closest_city_index = path.index(city)
        new_path.append(path[closest_city_index])
        path.remove(path[closest_city_index])
    return new_path
