# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.findSmallest(root, 0)[0]
    def findSmallest(self, root: TreeNode, depth)-> tuple:
        left = None
        right = None
        if not root.left and not root.right:
            return (root, depth)
        if root.left:
            left = self.findSmallest(root.left, depth+1)
        if root.right:
            right = self.findSmallest(root.right, depth+1)
        if left and right:
            if left[1] == right[1]:
                return (root, left[1])
            elif left[1] > right[1]:
                return left
            return right
        if left:
            return left
        return right
        
