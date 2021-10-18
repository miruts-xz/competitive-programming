#
# @lc app=leetcode id=1977 lang=python3
#
# [1977] Number of Ways to Separate Numbers
#

# @lc code=start
from functools import lru_cache


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        sub_nums = {}
        for i in range(len(num)):
            for j in range(i+1, len(num)+1):
                sub_nums[(i,j)] = num[i:j]
        @lru_cache(maxsize=None)
        def combs(p, i, prev)->int:
            if p == 0 and num[p] == '0':
                return 0
            cur = sub_nums[(p, i)]
            print(cur)
            if i >= n:
                return 1 if cur >= prev else 0
            commaed = 0
            if cur >= prev and num[i] != '0':
                commaed = combs(i, i+1, cur)
            uncommaed = combs(p,i+1,prev)
            return commaed+uncommaed
        return combs(0,1,"0")        
# @lc code=end
print(Solution().numberOfCombinations("9999"))

