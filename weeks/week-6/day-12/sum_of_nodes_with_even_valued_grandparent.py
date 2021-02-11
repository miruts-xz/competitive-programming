# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.grandpa(root.left, p=root.val) + self.grandpa(root.right, p=root.val)

    def grandpa(self, root: TreeNode, p, gp=float('inf')) -> int:
        if not root:
            return 0
        r = self.grandpa(root.left, root.val, p) + self.grandpa(root.right, root.val, p)
        return r if gp == float('inf') or gp % 2 else r + root.val
