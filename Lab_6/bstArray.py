import math

import numpy as np

from bstNode import BSTNode


class BSTArray:
    def __init__(self, length=11):
        self.length = length
        self.array = [BSTNode(i) for i in np.arange(start=0.5, stop=length + 0.5, step=1)]

    def insert(self, val):
        self.array[math.floor(val)].insert(val)

    def minimum_in_node(self, val):
        return self.array[math.floor(val)].get_min()

    def maximum_in_node(self, val):
        return self.array[math.floor(val)].get_max()

    def exists(self, val):
        return self.array[math.floor(val)].exists(val)

    def print_array(self):
        for node in self.array:
            if node.left is not None or node.right is not None:
                node.print_tree()
