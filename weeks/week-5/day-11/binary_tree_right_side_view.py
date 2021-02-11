# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        d = {}
        self.view(d, root, 0)
        r = []
        for _, v in d.items():
            r.append(v)
        return r

    def view(self, l: dict, root: TreeNode, idx: int):
        if not root:
            return
        l[idx] = root.val
        self.view(l, root.left, idx + 1)
        self.view(l, root.right, idx + 1)
