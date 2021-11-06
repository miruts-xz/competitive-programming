#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#

# @lc code=start
from math import atan, asin, acos,pi,tan


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        temp = q
        nxt = 1
        teta = atan(q/p)*pi
        while temp != p:
            compl = p-temp
            teta = pi/2-teta*pi
            temp = tan(teta*pi)*compl
            nxt += 1
            nxt %= 3
        return nxt
        
# @lc code=end

