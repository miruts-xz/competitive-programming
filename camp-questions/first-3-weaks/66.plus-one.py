#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = [0]+digits
        i = n-1
        carry = 1
        while i >= 0 and carry:
            r = digits[i]+carry
            carry = r//10
            ans[i+1] = r%10
            i -= 1
        if carry:
            ans[0] = carry
        return ans if ans[0] else ans[1:]
            
            
# @lc code=end

