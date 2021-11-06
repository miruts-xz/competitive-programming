#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def _subsets(i,p=[]):
            nonlocal ans, n
            if i >= n:
                ans.append(p)
                return
            _subsets(i+1, p+[nums[i]])
            _subsets(i+1, p)
        _subsets(0, [])
        return ans
            
# @lc code=end

