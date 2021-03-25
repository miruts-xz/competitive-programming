class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        return self.getMinPath(grid,memo,0,0)
    def getMinPath(self, grid: List[List[int]], memo, i, j)-> int:
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return sys.maxsize
        if memo.get((i,j), -1) != -1:
            return memo.get((i,j))
        if (i,j) == (len(grid)-1,len(grid[0])-1):
            return grid[i][j]
        memo[(i,j)] = grid[i][j] + min(self.getMinPath(grid,memo,i, j+1), self.getMinPath(grid, memo, i+1,j))
        return memo[(i,j)]
