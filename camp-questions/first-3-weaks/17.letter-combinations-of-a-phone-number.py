#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        d_to_l = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        def _letterCombinations(i, path=[]):
            nonlocal n, d_to_l
            if i == n:
               ans.append(''.join(path))
               return
            for c in d_to_l[digits[i]]:
                _letterCombinations(i+1, path+[c])
        _letterCombinations(0)
        return ans     
# @lc code=end

