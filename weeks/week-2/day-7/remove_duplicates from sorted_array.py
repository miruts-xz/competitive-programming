#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from typing import List


# Method implements remove duplicates in array leetcode challenge
# @https://leetcode.com/problems/remove-duplicates-from-sorted-array
def remove_duplicates(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.remove(nums[i])
            continue
        i += 1
    return len(nums)
