#
# @lc app=leetcode id=1702 lang=python3
#
# [1702] Maximum Binary String After Change
#

# @lc code=start
from collections import deque

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        visited = set()
        maximum = binary
        q = deque([binary])
        while q:
            cur = q.popleft()
            for i in range(len(cur)-1):
                if cur[i:i+2] == "00":
                    temp = cur[:i]+"10"+cur[i+2:]
                    maximum = max(maximum, cur[:i]+"10"+cur[i+2:])
                    q.append(temp)
                if cur[i:i+2] == "10":
                    temp = cur[:i]+"01"+cur[i+2:]
                    maximum = max(maximum, temp)
                    q.append(temp)
        return maximum
                
# @lc code=end

