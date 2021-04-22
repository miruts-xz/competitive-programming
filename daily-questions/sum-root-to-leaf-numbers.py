# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        self.parent = {}
    def sumNumbers(self, root: TreeNode) -> int:
        self.parent[root] = None
        self.traverse(root)
        return self.sum
    def traverse(self, root: TreeNode)-> int:
        if root.left:
            self.parent[root.left] = root
            self.traverse(root.left)
        if root.right:
            self.parent[root.right] = root
            self.traverse(root.right)
        if root.left or root.right:
            return
        pr = self.parent[root]
        i = 1
        num = root.val
        while pr is not None:
            num += pr.val*10**i
            pr = self.parent[pr]
            i += 1
        self.sum += num
