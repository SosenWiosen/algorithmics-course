def naive_pattern_search(str_array, pattern):
    """
    Naive pattern search algorithm.
    """
    # initialize the result list
    result = []
    # iterate through the array
    for array_row in range(len(str_array) - len(pattern) + 1):
        for array_column in range(len(str_array[array_row]) - len(pattern[0]) + 1):
            # if the current element matches the first element of the pattern
            if str_array[array_row][array_column] == pattern[0][0]:
                # check if the rest of the pattern matches
                is_pattern = True
                for pattern_row in range(len(pattern)):
                    for pattern_column in range(len(pattern[pattern_row])):
                        if str_array[array_row + pattern_row][array_column + pattern_column] != pattern[pattern_row] \
                                [pattern_column] and pattern[pattern_row][pattern_column] != '?':
                            is_pattern = False
                            break
                if is_pattern:
                    result.append((array_row, array_column))

    return result
