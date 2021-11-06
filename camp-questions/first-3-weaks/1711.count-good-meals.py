#
# @lc app=leetcode id=1711 lang=python3
#
# [1711] Count Good Meals
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        n = len(deliciousness)
        compl = defaultdict(int)
        res = 0
        maxx = max(deliciousness)
        for n1 in deliciousness:
            res += compl.get(n1, 0)
            k = 1
            while k <= n1+maxx:
                if k-n1 >= 0:
                    compl[k-n1] += 1
                k*=2
        return res%(10**9+7)
                
        
# @lc code=end

