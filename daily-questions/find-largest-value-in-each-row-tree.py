# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        items = 1
        while q:
            newCount = 0
            mx = -sys.maxsize
            for _ in range(items):
                nd = q.popleft()
                mx = max(nd.val, mx)
                if nd.left:
                    q.append(nd.left)
                    newCount += 1
                if nd.right:
                    q.append(nd.right)
                    newCount += 1
            items = newCount
            result.append(mx)
        return result
