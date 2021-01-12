#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from typing import List


# Class implements binary search leetcode challenge @https://leetcode.com/problems/binary-search
class Solution:
    def find(self, nums: List[int], target, lo, hi) -> int:
        mid = (hi + lo) // 2
        if lo > hi:
            return -1
        if nums[mid] > target:
            return self.find(nums, target, lo, mid - 1)
        elif nums[mid] < target:
            return self.find(nums, target, mid + 1, hi)
        return mid

    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums, target, 0, len(nums) - 1)
