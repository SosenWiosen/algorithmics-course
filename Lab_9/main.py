import csv
import time
import numpy as np


# greedy algorithm
def check_fit(x, y, knapsack):
    for x_start in range(len(knapsack) - x + 1):
        for y_start in range(len(knapsack) - y + 1):
            fits = True
            for x_iter in range(x):
                for y_iter in range(y):
                    if knapsack[x_start + x_iter][y_start + y_iter]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return x_start, y_start, False
    # checking if you can fit it after rotation
    for x_start in range(len(knapsack) - x + 1):
        for y_start in range(len(knapsack) - y + 1):
            fits = True
            for x_iter in range(x):
                for y_iter in range(y):
                    if knapsack[y_start + y_iter][x_start + x_iter]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return (x_start, y_start, True)

    return False


def main():
    f = open('results.csv', 'w')
    header = ['N', 'time', 'value', 'max_value']
    writer = csv.writer(f, dialect='excel')

    for size in ['20', '100', '500', '1000']:
        start = time.time()
        with open('packages' + size + '.txt') as txt:
            items = [line.split(',') for line in txt]
            # remove header
        del (items[0])
        del (items[0])
        for item in items:
            item[-1] = item[-1].strip()
        items = [[int(j) for j in i] for i in items]
        # add a column which stores the value
        for item in items:
            item.append(item[3] / (item[1] * item[2]))

        # sort by value descending
        items.sort(key=lambda x: -x[4])

        # empty knapsack
        knapsack = np.zeros((int(size), int(size)), dtype=int)
        value = 0
        iter = 0

        for item in items:
            fit = check_fit(item[1], item[2], knapsack)
            if fit:
                iter += 1

                # x,y placement
                if (fit[2]):
                    for x in range(fit[0], item[1] + fit[0]):
                        for y in range(fit[1], item[2] + fit[1]):
                            knapsack[y][x] = iter
                # y,x placement
                else:
                    for x in range(fit[0], item[1] + fit[0]):
                        for y in range(fit[1], item[2] + fit[1]):
                            knapsack[x][y] = iter

                value += item[3]

        print(knapsack)
        print("greedy, " + str(size) + ", " + str(time.time() - start))
        print("gathered value:", value)

        # value of all items
        sum = 0
        for item in items:
            sum += item[3]

        print("max possible:", sum)
        writer.writerow([size, time.time() - start, value, sum])


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
