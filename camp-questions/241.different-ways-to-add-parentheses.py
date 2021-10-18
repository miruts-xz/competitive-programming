#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        n = len(expression)
        operators = {'+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y}
        indices = [index for index in range(n) if expression[index] in ['-', '*', '+']]
        def _diffWaysToCompute(l, r):
            left = self.diffWaysToCompute(expression[:l+1])
            right = self.diffWaysToCompute(expression[r:])
            return [operators[expression[l+1]](n1, n2) for n1 in left for n2 in right]
        if indices:    
            for ind in indices:
                ans += _diffWaysToCompute(ind-1, ind+1)
            return ans
        return [int(expression)]
print(Solution().diffWaysToCompute("2-1-1-1"))
# @lc code=end

