#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0]*n
        print(prefix)
        for i, m in enumerate(nums):
            prefix[i+1] = prefix[i]+nums[i]
        print(prefix)
        i = 0
        valid_nums = []
        while i*k <= prefix[-1]:
            valid_nums.append(i*k)
            i += 1
        print(valid_nums)
        lookup = {}
        for p in prefix:
            for compl in valid_nums:
                if p-compl in lookup:
                    return True
                lookup[p] = 1
        return False

        
        
# @lc code=end

