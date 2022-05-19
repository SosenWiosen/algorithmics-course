from naive_pattern_search import naive_pattern_search
from rabin_karp_pattern_matching import rabin_karp_pattern_matching


def main():
    # load 1000_pattern into a 2d array\
    sample_data = []

    sample_data = [char for char in open('1000_pattern.txt', 'r').read().splitlines()]
    pattern = ['ABC', 'B??', 'C??']
    naive_pattern_search(sample_data, pattern)
    rabin_karp_pattern_matching(sample_data, pattern)


if __name__ == '__main__':
    main()
