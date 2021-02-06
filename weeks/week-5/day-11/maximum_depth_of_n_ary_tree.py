"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root.children:
            m = []
            for i in range(len(root.children)):
                m.append(self.maxDepth(root.children[i]))
            return 1 + max(m)
        return 1

