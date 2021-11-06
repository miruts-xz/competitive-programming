#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = prev_max = nums[0]
        for n in nums[1:]:
            prev_max = max(n, prev_max+n)
            max_so_far = max(prev_max, max_so_far)
        return max_so_far
# @lc code=end

