import numpy
from python_tsp.exact import solve_tsp_dynamic_programming

from closest_neighbour import closest_neighbour
from path_length import calculate_path_length
import numpy as np
from python_tsp.distances import euclidean_distance_matrix
from python_tsp.heuristics import solve_tsp_simulated_annealing

from plot_path import plot_path


def main():
    # read the path from the file
    path = []
    with open('TSP.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                index, x, y = line.split()
                path.append([float(x), float(y)])
    # path from the files
    print(calculate_path_length(path))
    # closest neighbour starting at a random point
    print(calculate_path_length(closest_neighbour(path)))
    distance_matrix = euclidean_distance_matrix(numpy.array(path))
    min_distance = float('inf')
    min_dist_permutation = []

    for i in range(20):
        permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
        if distance < min_distance:
            min_distance = distance
            min_dist_permutation = permutation
    print(distance)
    plot_path([permutation], path)


if __name__ == '__main__':
    main()
