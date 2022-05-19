""" Here we will implement the rabin karp matching algorithm for the given pattern. Note that it only works for patterns
where you have one row and one column of characters. """
d = 17
q = 101


def rabin_karp_pattern_matching(str_array, pattern):
    results = []
    p_w = len(pattern[0])
    p_h = len(pattern)
    s_w = len(str_array[0])
    s_h = len(str_array)
    pattern_horizontal_hash = 0
    pattern_vertical_hash = 0
    for i in range(p_w):
        pattern_horizontal_hash = (d * pattern_horizontal_hash + ord(pattern[0][i])) % q
    for i in range(p_h):
        pattern_vertical_hash = (d * pattern_vertical_hash + ord(pattern[i][0])) % q

    # note that for patterns where the row and column length is the same, h is also the same

    h = 1
    for i in range(p_w - 1):
        h = (d * h) % q
    rows_hashed = []
    row_index = 0
    for row in str_array:

        first_window_hash = 0
        for i in range(p_w):
            first_window_hash = (d * first_window_hash + ord(row[i])) % q
        rows_hashed.append([first_window_hash])
        window_hash = first_window_hash

        for i in range(len(row) - p_w):
            window_hash = (d * (window_hash - ord(row[i]) * h) + ord(row[i + p_w])) % q
            if window_hash < 0:
                window_hash = window_hash + q
            rows_hashed[row_index].append(window_hash)
            # calculate the hash for the first window of the pattern
        row_index += 1

    cols_hashed = []
    for col_index in range(s_w):
        first_column_hash = 0
        for row_index in range(p_h):
            first_column_hash = (d * first_column_hash + ord(str_array[row_index][col_index])) % q
        cols_hashed.append([first_column_hash])
        window_hash = first_column_hash
        for row_index in range(len(str_array) - p_h):
            window_hash = (d * (window_hash - ord(str_array[row_index][col_index]) * h) + ord(
                str_array[row_index + p_h][col_index])) % q
            cols_hashed[col_index].append(window_hash)

    for i in range(s_w - p_w):
        for j in range(s_h - p_h):
            if pattern_horizontal_hash == rows_hashed[i][j] and pattern_vertical_hash == cols_hashed[j][i]:
                is_correct = True
                for k in range(3):
                    for m in range(3):
                        if str_array[i + k][j + m] != pattern[k][m] and pattern[k][m] != '?':
                            is_correct = False
                if is_correct:
                    results.append((i, j))
    return results
