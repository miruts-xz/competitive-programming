#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


# Implements relative sort array leetcode problem @https://leetcode.com/problems/relative-sort-array
def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    maximum = arr1[0]
    for c in arr1:
        if maximum < c:
            maximum = c
    a = [0] * (maximum + 1)
    sorted_array = []
    for c in arr1:
        a[c] += 1
    j = 0
    while j < len(arr2):
        for i in range(a[arr2[j]]):
            sorted_array.append(arr2[j])
            a[arr2[j]] -= 1
        j += 1
    for i in range(len(a)):
        for j in range(a[i]):
            sorted_array.append(i)
    return sorted_array


print(relative_sort_array([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
