from typing import Deque, List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [set() for _ in range(n)]
        for st, dst in edges:
            adj_list[st].add(dst)
            adj_list[dst].add(st)
        q = Deque()
        for i, lst in enumerate(adj_list):
            if len(lst) == 1:
                q.append(i)
        while len(q) > 2:
            cur = q.popleft()
            for node in adj_list[cur]:
                adj_list[node].remove(cur)
                if len(adj_list[node]) == 1:
                    q.append(node)
        return list(q)        
print(Solution().findMinHeightTrees(2, [[0,1]]))

        
            