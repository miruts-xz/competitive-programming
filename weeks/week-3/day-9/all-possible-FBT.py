# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        result = [None for i in range(n + 1)]
        result[0] = []
        result[1] = [TreeNode(0)]
        return self.allFBT(result, n)

    def allFBT(self, result: List[TreeNode], n: int):
        if not result[n]:
            ans = []
            for x in range(n):
                y = n - 1 - x
                for left in self.allFBT(result, x):
                    for right in self.allFBT(result, y):
                        nd = TreeNode(0)
                        nd.left = left
                        nd.right = right
                        ans.append(nd)
            result[n] = ans
        return result[n]
