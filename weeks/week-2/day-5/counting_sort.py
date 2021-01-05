#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


def counting_sort(nums: List[int]) -> List[int]:
    maximum = nums[0]
    for n in nums:
        if maximum < n:
            maximum = n
    a = [0] * (maximum + 1)
    for n in nums:
        a[n] += 1
    sorted_array = []
    for i in range(len(a)):
        for j in range(a[i]):
            sorted_array.append(i)
    return sorted_array


print(counting_sort([9, 3, 2, 2]))
