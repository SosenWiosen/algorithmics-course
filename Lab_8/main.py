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
    plot_path([[i for i in range(len(path))]], path)
    # closest neighbour starting at a random point
    new_path= closest_neighbour(path)
    plot_path([[i for i in range(len(path))]], new_path)
    print(calculate_path_length(new_path))
    distance_matrix = euclidean_distance_matrix(numpy.array(path))
    min_distance = float('inf')
    min_dist_permutation = []

    permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
    print(distance)
    plot_path([permutation], path)


if __name__ == '__main__':
    main()
