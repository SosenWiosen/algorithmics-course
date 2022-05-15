def main():
    num_str = ''
    for i in range(500, 3001):
        if i % 7 == 0 and i % 5 != 0:
            num_str += str(i)
    num_str = num_str.replace('21', 'XX')
    print('Found ', num_str.count('XX'), ' occurrences of 21')


if __name__ == '__main__':
    main()
