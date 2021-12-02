#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_node(root, key):
            if not root: return None
            if root.val < key:
                return get_node(root.right, key)
            if root.val > key:
                return get_node(root.left,key)
            return root
        def getNode(root, parent, left=True):
            if (not root.left if left else not root.right):
                if parent:
                    if left: parent.right = None
                    else: parent.right = None
                return root.val
            return getNode(root.left if left else root.right, root, left)
        target = get_node(root, key)
        if target is None: return root
        replacement = getNode(target.right, target) if target.right else getNode(target.left, target, False)
        target.val = replacement
        return root
        
        
    

# @lc code=end

