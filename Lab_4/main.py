import time

from numpy import random


def insertion_sort(arr):
    for i in range(len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x


def merge(arr, left_arr, right_arr):
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:(len(arr) // 2)]
        right_arr = arr[(len(arr) // 2):]
        merge_sort(left_arr)
        merge_sort(right_arr)
        merge(arr, left_arr, right_arr)


def main():
    length = 1000
    iterations = 100
    max_num_size = 10000
    merge_max_time = insert_max_time = 0
    merge_min_time = insert_min_time = 10000000000

    start_i = time.time()
    for i in range(iterations):

        arr = random.randint(max_num_size, size=length)
        start_ii = time.time_ns()
        insertion_sort(arr)
        end_ii = time.time_ns()
        insert_max_time = max(insert_max_time, end_ii - start_ii)
        insert_min_time = min(insert_min_time, end_ii - start_ii)
    end_i = time.time()
    time_i = end_i - start_i

    start_m = time.time()
    for i in range(iterations):
        arr = random.randint(1000000, size=length)
        start_mm = time.time_ns()
        merge_sort(arr)
        end_mm = time.time_ns()
        merge_max_time = max(merge_max_time, end_mm - start_mm)
        merge_min_time = min(merge_min_time, end_mm - start_mm)
    end_m = time.time()
    time_m = end_m - start_m

    print("Max time[ns] in insertion sort: ", insert_max_time, " Min time[ns] in insertion sort: ", insert_min_time)
    print("Max time[ns] in merge sort: ", merge_max_time, " Min time[ns] in insertion sort: ", merge_min_time)

    print("Full time in insertion sort: ", time_i)

    print("Full time in merge sort", time_m)

    print("Avg time in insertion sort: ", time_i / iterations, "for ", iterations, "iterations")
    print("Avg time in merge sort: ", time_m / iterations, "for ", iterations, "iterations")


if __name__ == '__main__':
    main()
