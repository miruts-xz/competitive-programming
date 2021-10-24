from typing import List


class Solution:
    def paintHouses(self, costs: List[List[int]]):
        m, n = len(costs), len(costs[0])
        def exclude(i)->List[int]:
            return [j for j in range(n) if j != i]
        dp = {}
        def dfs(i,g=-1)->int:
            if i == m-1:
                return min([costs[i][j] for j in exclude(g)])
            if (i,g) not in dp:
                dp[(i,g)] = min([costs[i][c]+dfs(i+1, c) for c in exclude(g)])
            return dp[(i,g)]
        return dfs(0)
print(Solution().paintHouses([[17,2,17],[16,16,5],[14,3,19]]))
print(Solution().paintHouses([[7,6,2]]))
