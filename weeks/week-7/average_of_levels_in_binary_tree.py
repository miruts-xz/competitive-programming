from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        bfs = deque()
        result = []
        bfs.append(root)
        while bfs:
            count = len(bfs)
            s = 0
            for i in range(len(bfs)):
                curr = bfs.popleft()
                s += curr.val
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
            result.append(s / count)
        return result


