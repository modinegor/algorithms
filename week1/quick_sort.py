import random


def quick_sort(array):
    if len(array) <= 1:
        return array

    array_middle = len(array) / 2

    if len(array) > 2 and array[0] > array[array_middle]:
        a = array[0]
        array[0] = array[array_middle]
        array[array_middle] = a
    if array[0] > array[-1]:
        a = array[0]
        array[0] = array[-1]
        array[-1] = a
    if len(array) > 2 and array[array_middle] > array[-1]:
        a = array[array_middle]
        array[array_middle] = array[-1]
        array[-1] = a

    a = array[array_middle]

    if len(array) <= 3:
        return array

    to_sort = array[1:array_middle] + array[array_middle + 1:-1]
    left = quick_sort([array[0]] + [x for x in to_sort if x <= a])
    right = quick_sort([x for x in to_sort if x > a] + [array[-1]])

    return left + [a] + right
