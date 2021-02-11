from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            visited.add(i)
            count += 1
            self.dfs(isConnected, visited, i)
        return count

    def dfs(self, isConnected: List[List[int]], visited: set(), i=0):
        for j in range(len(isConnected)):
            if i != j and isConnected[i][j] and j not in visited:
                visited.add(j)
                self.dfs(isConnected, visited, j)
