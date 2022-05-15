import csv
import random
from time import time

from bstArray import BSTArray


def test():
    n_arr = [50, 100, 500, 1_000, 10_000, 25_000, 50_000, 100_000, 250_000, 1_000_000]

    f = open('results2.csv', 'w')
    header = ['N', 'Insert', 'Min', 'Max', 'Search']
    writer = csv.writer(f, dialect='excel')
    writer.writerow(header)

    for N in range(10000):
        # list of N random floats from 0.00 to 10
        elems_to_insert = [round(random.uniform(.00, 10.00), 2) for _ in range(N)]

        tree_array = BSTArray()  # generate roots from 0.5 to 10 with step 1

        multiplication = 100_000

        insert_start = time()
        for elem in elems_to_insert:
            tree_array.insert(elem)  # insert elems to tree
        insert_end = time()

        min_start = time()
        for i in range(multiplication):
            minimum = tree_array.minimum_in_node(random.uniform(.00, 10.00))
        min_end = time()

        max_start = time()
        for i in range(multiplication):
            maximum = tree_array.maximum_in_node(random.uniform(.00, 10.00))
        max_end = time()

        random_float = round(random.uniform(.0, 10.0), 2)

        search_start = time()
        for i in range(multiplication):
            search = tree_array.exists(random_float)
        search_end = time()
        writer.writerow(
            [N, (insert_end - insert_start) / multiplication, (min_end - min_start) / multiplication,
             (max_end - max_start) / multiplication, (search_end - search_start) / multiplication])
