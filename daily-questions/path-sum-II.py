# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def __pathSum__(root: TreeNode, targetSum=targetSum) -> List[List[int]]:
            if not root:
                return []
            if not root.left and not root.right and targetSum - root.val == 0:
                return [[root.val]]
            paths_left = __pathSum__(root.left, targetSum - root.val)
            paths_right = __pathSum__(root.right, targetSum - root.val)
            res = [[root.val] + p for p in paths_left] + [[root.val] + p for p in paths_right]
            return res

        return __pathSum__(root)


if __name__ == "__main__":
    print(Solution().pathSum(TreeNode(left=TreeNode(1), right=TreeNode(4)), 3))
