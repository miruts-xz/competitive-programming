# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for val in range(1, len(preorder)):
            node = TreeNode(preorder[val])
            cur = None
            while stack and stack[-1].val < preorder[val]:
                cur = stack.pop()
            if cur:
                cur.right = node
            if not cur and stack:
                stack[-1].left = node
            stack.append(node)
        return root
