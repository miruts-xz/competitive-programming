#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# camp-questions/437.path-sum-iii.py
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import DefaultDict, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        lookup = DefaultDict(int)
        def _pathSum(root, rem):
            nonlocal ans
            if not root:
                return
            if root.val == rem:
                ans += 1
            ans += lookup[targetSum+rem-root.val]
            lookup[rem-root.val] += 1
            _pathSum(root.left, rem-root.val)
            _pathSum(root.right,rem-root.val)
            lookup[rem-root.val] -= 1
        _pathSum(root,targetSum)
        return ans
    
# @lc code=end

