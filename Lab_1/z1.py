from statistics import mean


def main():
    number_list = [1, 2]
    for x in range(2, 48):
        number_list.append((number_list[-1] + number_list[-2]) / (number_list[-1] - number_list[-2]))
    val_count_dict = {i: number_list.count(i) for i in number_list}

    diff_occur_num = 0
    last_occur_num = list(val_count_dict.values())[0]
    for key in val_count_dict:
        if val_count_dict[key] != last_occur_num:
            diff_occur_num += 1

    print('Mode: ', max(set(number_list), key=number_list.count) if diff_occur_num > 0 else "Doesn't exist")
    print('Avg: ', mean(number_list))

    print("Values which appeared more than one time: ",
          {key: value for (key, value) in val_count_dict.items() if value > 1} if {key: value for (key, value) in
                                                                                   val_count_dict.items() if
                                                                                   value > 1} else "none")


if __name__ == '__main__':
    main()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
