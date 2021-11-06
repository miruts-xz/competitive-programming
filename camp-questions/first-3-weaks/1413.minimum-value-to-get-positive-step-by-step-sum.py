#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

# @lc code=start
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        rsum = nums[0]
        min_so_far = rsum
        for n in nums[1:]:
            rsum += n
            min_so_far = min(min_so_far, rsum)
        return 1-(min_so_far) if min_so_far < 1 else 1
# @lc code=end

