from collections import deque
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = [[] for i in range(len(edges) + 1)]
        for i in range(len(edges)):
            e = edges[i]
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        print(adj_list)
        result = self.dfs(adj_list, set(), hasApple, 0)
        if result > 0:
            result -= 2
        return result

    def dfs(self, matrix: List[List[int]], visited: set, hasApple: List[bool], r):
        if r in visited:
            return 0
        visited.add(r)
        total = 0
        for n in matrix[r]:
            total += self.dfs(matrix, visited, hasApple, n)
        if hasApple[r] or total > 0:
            total += 2
        return total
