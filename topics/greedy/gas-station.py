class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        memo = {}
        can = False
        for i in range(len(gas)):
            if self.dfs(gas,cost,gas[i],i,i):
                return i
        return -1
    def dfs(self, gas, cost,curr, start, dest)-> bool:
        if curr >= cost[start]:
            nxt = (start+1)%len(gas)
            if dest == nxt:
                return True
            return self.dfs(gas,cost, curr+gas[nxt]-cost[start],nxt, dest)
        return False
