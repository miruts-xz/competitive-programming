#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is illegal.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


def good_pairs(nums: List[int]) -> int:
    """
    # Method implements algorithm for counting good pairs in a list

    Two numbers are good pairs (good buddies if you will) if they have equal value and are not found in the same spot
    :param nums:
    :return: Good pairs count
    """
    i, j = 0, len(nums) - 1
    count = 0
    while i < j and i < len(nums) - 1:
        if nums[i] == nums[j]:
            count += 1
        j -= 1
        if j <= i:
            i += 1
            j = len(nums) - 1
    return count
