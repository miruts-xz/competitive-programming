import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root)

    def isValid(self, root, mn: int = -sys.maxsize, mx: int = sys.maxsize) -> bool:
        if not root:
            return True
        if not mn < root.val < mx:
            return False
        return self.isValid(root.left, mx=root.val, mn=mn) and self.isValid(root.right, mx=mx, mn=root.val)
