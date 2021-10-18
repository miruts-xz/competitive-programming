#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0]*(n+1)
        for i, m in nums:
            prefix[i+1] = prefix[i]+nums[i]
        print(prefix)
# @lc code=end

