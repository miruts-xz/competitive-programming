# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.mirrored(root.left, root.right)

    def mirrored(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.mirrored(left.left, right.right) and self.mirrored(left.right, right.left)
        return False
