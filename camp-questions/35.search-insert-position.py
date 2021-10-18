#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(l,r,t)->int:
            mid = l+(r-l)//2
            while l <= r:
                if nums[mid] == t:
                    return mid
                if nums[mid] > t:
                    r = mid-1
                if nums[mid] < t:
                    l = mid+1
                return search(l,r,t)
            else:
                return l
        return search(0, len(nums)-1, target)
                    
# @lc code=end

