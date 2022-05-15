import re
import time


def main():
    word = ''
    while True:
        input_text = input('What do you want to search?\n')
        words = re.split('[^a-zA-Z]', input_text)
        if len(words) == 1:
            word = input_text
            break
        print('Wrong input! Try again.')
    word = word.lower()

    start = time.time()
    file = open('SJP.txt')
    polish_dictionary = file.read().splitlines()
    lookup_start = time.time()
    if word in polish_dictionary:
        print('Nice, "', word, '" is a polish word!')
    else:
        print('Not a polish word.')
    end = time.time()
    print('Time of execution using list: ', end - start, ' Time taken by the lookup:', end - lookup_start)

    start = time.time()
    file = open('SJP.txt')
    polish_dictionary = set(file.read().splitlines())

    lookup_start = time.time()
    if word in polish_dictionary:
        print('Nice, "', word, '" is a polish word!')
    else:
        print('Not a polish word.')
    end = time.time()
    print('Time of execution using set: ', end - start, ' Time taken by the lookup:', end - lookup_start)
    print('Pierwszy czas został zmierzony od momentu otwarcia pliku do czasu wypisania, drugi mierzy czas potrzebny na sprawdzenie czy slowo jest secie/liście')


if __name__ == '__main__':
    main()
