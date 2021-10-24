#
# @lc app=leetcode id=910 lang=python3
#
# [910] Smallest Range II
#

# @lc code=start
from typing import List
from math import inf

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        """
        [0, 10] k = 10
        |
        [2, 8]
        [1,3,6] k = 3
        |
        [4,6,3]
        [7,8,8,5,2]
        [2,5,7,8,8]
        4
        """
        nums.sort()
        minimum = nums[-1]-nums[0]
        if k >= minimum:
            return minimum
        n = len(nums)
        mean = sum(nums)/n
        min_element = inf
        max_element = -inf
        for num in nums:
            if num <= mean:
                min_element = min(min_element, num+k)
                max_element = max(max_element, num+k)
            else:
                max_element = max(max_element, num-k)
                min_element = min(min_element, num-k)
        print(max_element, min_element)
        return max_element-min_element
# @lc code=end

