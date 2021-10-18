#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s)-1
        while r >= 0 and s[r] == " ":
            r -= 1
        size = 0
        while r >= 0 and s[r] != " ":
            size += 1
            r -= 1
        return size
# @lc code=end

