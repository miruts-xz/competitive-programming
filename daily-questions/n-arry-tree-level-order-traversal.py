from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        rem = 1
        while q:
            new_rem = 0
            temp = []
            for _ in range(rem):
                n = q.popleft()
                temp.append(n.val)
                for nn in n.children:
                    q.append(nn)
                    new_rem += 1
            res.append(temp)
            rem = new_rem
        return res


if __name__ == "__main__":
    print(Solution().levelOrder(Node(2, children=[Node(2, []), Node(3, [])])))
