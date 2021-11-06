#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        ans = []
        def _permute(i, cum=[]):
            if i == n:
                return
            if len(cum) == n:
                ans.append(cum)
                return
            for j, m in enumerate(nums):
                if m not in visited:
                    visited.add(m)
                    _permute(j,cum+[nums[j]])
                    visited.remove(m)
        for i in range(n):
            visited.add(nums[i])
            _permute(i,[nums[i]])
            visited.remove(nums[i])
        return ans
            
                
# @lc code=end

