# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = [False]
        self.inOrder(root, result, k, [0])
        return result[0]

    def inOrder(self, root: TreeNode, result: List[int], k: int, current: List[int] = [0]):
        if not root:
            return
        self.inOrder(root.left, result, k, current)
        current[0] += 1
        if k == current[0]:
            result[0] = root.val
            print(result[0])
            return
        if result[0] != False:
            return
        self.inOrder(root.right, result, k, current)
