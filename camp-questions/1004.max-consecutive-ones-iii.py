#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,n = 0,0,len(nums)
        count = 0
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+int(not nums[i])
        while r < n+1:
            zeros = prefix[r]-prefix[l]
            if zeros > k:
                count = max(count, r-l-1)
                l += 1
                r -= 1
            r += 1
        return max(count, r-l-1)
# @lc code=end

