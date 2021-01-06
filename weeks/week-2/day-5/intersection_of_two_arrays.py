#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    smaller = []
    larger = []
    result = []
    if len(nums1) >= len(nums2):
        smaller = nums2
        larger = nums1
    else:
        smaller = nums1
        larger = nums2
    for n in smaller:
        if n in larger:
            result.append(n)
    return list(set(result))


print(intersection([1, 2, 3, 2], [2, 2]))
