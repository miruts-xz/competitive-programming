# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.maxSum(root)[0]
    def maxSum(self, root: TreeNode)-> int:
        right = 0
        left = 0
        if root.left and root.right:
            mx = -sys.maxsize
            right, ar = self.maxSum(root.right)
            left, al = self.maxSum(root.left)
            return (max(right, left, root.val, ar+root.val, al+root.val, al+ar+root.val), max(root.val, root.val + max(ar, al)))
        if root.right:
            mx = -sys.maxsize
            right,ar = self.maxSum(root.right)
            return (max(right, root.val, ar+root.val), max(root.val+ar, root.val))
        if root.left:
            left, al = self.maxSum(root.left)
            return (max(left, root.val, al+root.val), max(root.val+al, root.val))
        return (root.val, root.val)
