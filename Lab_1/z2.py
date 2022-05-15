import array as arr
from statistics import mean
import time
import z1


def main():
    start1 = time.time()
    z1.main()
    end1 = time.time()
    print('Time it takes to execute using lists', end1 - start1)

    start2 = time.time()

    num_array = arr.array("d", [1.0, 2.0])
    for x in range(2, 48):
        num_array.append((num_array[-1] + num_array[-2]) / (num_array[-1] - num_array[-2]))
    val_count_dict = {i: num_array.count(i) for i in num_array}

    diff_occur_num = 0
    last_occur_num = list(val_count_dict.values())[0]
    for key in val_count_dict:
        if val_count_dict[key] != last_occur_num:
            diff_occur_num += 1

    print('Mode: ', max(set(num_array), key=num_array.count) if diff_occur_num > 0 else "Doesn't exist")

    print("Avg: ", mean(num_array))

    print("Values which appeared more than one time: ",
          {key: value for (key, value) in val_count_dict.items() if value > 1} if {key: value for (key, value) in
                                                                                   val_count_dict.items() if
                                                                                   value > 1} else "none")

    end2 = time.time()
    print('Time it takes to execute using arrays', end2 - start2)


if __name__ == '__main__':
    main()
