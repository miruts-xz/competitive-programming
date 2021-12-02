#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right: max_length = max(max_length, left+right)
            elif right >= left: left=right=0
        left = right = 0
        for j in range(len(s)-1, -1, -1):
            c = s[j]
            if c == ')':
                right += 1
            else:
                left += 1
            if left == right: max_length = max(max_length, right+left)
            elif left >= right: left = right = 0
        return max_length

# @lc code=end
# couldn't solve it.

