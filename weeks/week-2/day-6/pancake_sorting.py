
#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)

from typing import List

# Method implements pancake sorting leetcode challenge @https://leetcode.com/problems/pancake-sorting
def pancake_sort(arr: List[int]) -> List[int]:
    result = []

    def pancake_flip(arr, index):
        arr = arr[index - len(arr)::-1] + arr[index + 1:]
        return arr

    for i in range(len(arr), 1, -1):
        idx = arr.index(i)
        # Crazy author, inconsistent indexing
        result.append(idx + 1)
        # Flip to head
        arr = pancake_flip(arr, idx)
        result.append(i)
        # Flip to correct position
        arr = pancake_flip(arr, i - 1)
    return result


print(pancake_sort([2, 1, 4, 3]))
