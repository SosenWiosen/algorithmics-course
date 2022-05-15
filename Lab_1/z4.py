def main():
    some_list = [1] * 15
    try:
        some_list[15] = 1
    except IndexError:
        print('wrong index!')

    try:
        some_list12[15] = 1
    except NameError:
        print('wrong variable name!')

    try:
        some_list[2] / 0
    except ZeroDivisionError:
        print('Division by zero!')


if __name__ == '__main__':
    main()
