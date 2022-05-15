# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bstArray import BSTArray
from testing import test


def main():
    elements_to_insert = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]
    bst = BSTArray()
    for element in elements_to_insert:
        bst.insert(element)
    bst.print_array()

    test()


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
