# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.findValueHeight(root.left, root.val)
        right = self.findValueHeight(root.right, root.val)
        return max(left + right, self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))

    def findValueHeight(self, n, val):
        if not n:
            return 0
        if n.val != val:
            return 0
        return 1 + max(self.findValueHeight(n.left, val), self.findValueHeight(n.right, val))
