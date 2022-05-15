iterations_in_iterative = 0
checks_in_iterative = 0
steps_in_recursive = 0


# Implement the iterative version of hanoi tower
def hanoi_iterative(n, source, destination, buffer):
    i = 1
    while source or buffer:
        print(source, destination, buffer)
        if i % 3 == 1:
            if can_move(source, destination):
                disk = source.pop()
                destination.append(disk)
            else:
                disk = destination.pop()
                source.append(disk)
        if i % 3 == 2:
            if can_move(source, buffer):
                disk = source.pop()
                buffer.append(disk)
            else:
                disk = buffer.pop()
                source.append(disk)
        if i % 3 == 0:
            if can_move(buffer, destination):
                disk = buffer.pop()
                destination.append(disk)
            else:
                disk = destination.pop()
                buffer.append(disk)
        i += 1
    global iterations_in_iterative
    iterations_in_iterative = i


# function which checks if you can move a disk between two pegs, depending on the size of the disk
def can_move(source, destination):
    global checks_in_iterative
    checks_in_iterative += 1
    if not source:
        return False
    if not destination:
        return True
    return source[-1] < destination[-1]


# implement the recursive version of hanoi tower
# assuming that when the function is called, the disks are in the correct order.
def hanoi_recursive(n, source, destination, buffer):
    global steps_in_recursive
    steps_in_recursive += 1

    if n == 1:
        disk = source.pop()
        destination.append(disk)
        return
    hanoi_recursive(n - 1, source, buffer, destination)
    disk = source.pop()
    destination.append(disk)
    print(source, destination, buffer)
    hanoi_recursive(n - 1, buffer, destination, source)


def main():
    # test your code
    n = 3
    source = [i for i in range(n, 0, -1)]
    destination = []
    buffer = []
    hanoi_iterative(n, source, destination, buffer)
    print('\n')
    source = [i for i in range(n, 0, -1)]
    destination = []
    buffer = []
    hanoi_recursive(n, source, destination, buffer)
    print(source, destination, buffer)


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
