class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {n-2: cost[n-2], n-1: cost[n-1]}
        return min(self.getMinCost(cost,memo, 0),self.getMinCost(cost,memo,1))
    def getMinCost(self, cost: List[int],memo, i: int)-> int:
        if memo.get(i, -1) != -1:
            return memo.get(i)
        memo[i] = cost[i] + min(self.getMinCost(cost,memo,i+1), self.getMinCost(cost,memo,i+2))
        return memo[i]
