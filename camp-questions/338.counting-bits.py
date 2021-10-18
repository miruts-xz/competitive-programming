#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(num)-> int:
            res = 0
            while num:
                num &= num-1
                res += 1
            return res
        ans = [0]*(n+1)
        for i in range(1, n+1):
            ans[i] = count_ones(i)
        return ans
# @lc code=end

