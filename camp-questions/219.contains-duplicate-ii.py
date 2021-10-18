#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l, r = 0, 0
        found = set()
        while r <= k:
            if nums[r] in found:
                return True
            found.add(nums[r])
            r += 1
        l += 1; r += 1
        while r < n:
            if nums[l] in found or nums[r] in found:
                return True
            found.remove(nums[l-1])
            found.add(nums[l])
            found.add(nums[r])
        return False
            
            
# @lc code=end

