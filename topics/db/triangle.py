class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.getMin(triangle, memo)
    def getMin(self,tr, memo: map, i: int = 0, j: int = 0)-> int:
        if i == len(tr)-1:
            return tr[i][j]
        if memo.get((i,j),-1) != -1:
            return memo[(i,j)]
        memo[(i,j)] = tr[i][j] + min(self.getMin(tr,memo, i+1, j), self.getMin(tr,memo, i+1,j+1))
        return memo[(i,j)]
        
