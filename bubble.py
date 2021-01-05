from typing import List

"""



"""


def bubble_sort(a: List[int]) -> List[int]:
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
    return a


print(bubble_sort([5, 4, 4, 3, 2, 1]))


def selection_sort(a: List[int]) -> List[int]:
    for i in range(len(a)):
        n = i
        for j in range(i + 1, len(a)):
            if a[j] < a[n]:
                n = j
        a[i], a[n] = a[n], a[i]
    return a


def insertion_sort(a: List[int]) -> List[int]:
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


print(selection_sort([5, 4, 4, 3, 2, 1]))

print(insertion_sort([5, 4, 4, 3, 2, 1]))
