# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_bottom_left_tree_value(root: TreeNode) -> int:
    q = deque()
    q.append((root, 0))
    prev = None
    while q:
        prev = q.popleft()
        if prev[0].right:
            q.append((prev[0].right, prev[1] + 1))
        if prev[0].left:
            q.append((prev[0].left, prev[1] + 1))
    return prev[0].val


root = TreeNode(2, left=TreeNode(1, right=TreeNode(7)), right=TreeNode(3))

print(find_bottom_left_tree_value(root))
