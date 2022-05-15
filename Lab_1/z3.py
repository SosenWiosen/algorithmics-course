from random import randrange
from time import time


def main():
    size = 50000000
    num_list = [0] * size

    start1 = time()
    for num in num_list:
        num = randrange(1, 10000)
    end1 = time()
    print('Time using iterative loop: ', end1 - start1)
    start2 = time()
    for i in range(1000):
        num_list[i] = randrange(1, 10000)
    end2 = time()

    print('Time using c style loop: ', end2 - start1)


if __name__ == '__main__':
    main()
