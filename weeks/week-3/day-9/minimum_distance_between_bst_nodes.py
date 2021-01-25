import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largest(self, root: TreeNode) -> int:
        if not root.right:
            return root.val
        return self.largest(root.right)

    def minimum(self, root: TreeNode) -> int:
        if not root.left:
            return root.val
        return self.minimum(root.left)

    def minDiffInBST(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return sys.maxsize
        if root.left and root.right:
            return min(abs(self.minimum(root.right) - root.val), abs(self.largest(root.left) - root.val),
                       self.minDiffInBST(root.left), self.minDiffInBST(root.right))
        if root.left:
            return min(abs(self.largest(root.left) - root.val), self.minDiffInBST(root.left))
        if root.right:
            return min(abs(self.minimum(root.right) - root.val), self.minDiffInBST(root.right))
