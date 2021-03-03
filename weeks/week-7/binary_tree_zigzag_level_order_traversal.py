from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = deque()
        result = []
        queue.append(root)

        # left to right
        dr = True

        while queue:
            tempr = []
            if dr:
                for i in range(len(queue)):
                    cur = queue.popleft()
                    tempr.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            else:
                for i in range(len(queue)):
                    cur = queue.pop()
                    tempr.append(cur.val)
                    if cur.right:
                        queue.appendleft(cur.right)
                    if cur.left:
                        queue.appendleft(cur.left)

            dr = not dr
            result.append(tempr)
        return result
