#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from typing import List


# Method implements sort colors leetcode challenge @@https://leetcode.com/problems/sort-colors
def sort_colors(nums: List[int]) -> List[int]:
    r, w, b = 0, 0, 0
    for n in nums:
        if n == 0:
            r += 1
        elif n == 1:
            w += 1
        else:
            b += 1
    idx = 0
    for i in range(r):
        nums[idx] = 0
        idx += 1
    for j in range(w):
        nums[idx] = 1
        idx += 1
    for k in range(b):
        nums[idx] = 2
        idx += 1
    return nums


print(sort_colors([0, 2, 0, 1, 1, 2, 1]))
