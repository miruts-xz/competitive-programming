class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        i,j = 0,0
        mx = 0
        memo = {}
        # visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mx = max(mx, 1+self.dfs(matrix,memo,i,j,matrix[i][j]))
        return mx   
    def dfs(self, matrix,memo,i,j, prevNum)-> int:
        if memo.get((i,j), -1) != -1:
            return memo.get((i,j))
        mx = 0
        for k,m in [[i+1, j],[i, j+1],[i-1, j],[i, j-1]]:
            if 0 <= k< len(matrix) and 0 <= m < len(matrix[0]) and matrix[k][m] > prevNum:
                mx = max(mx, 1+self.dfs(matrix,memo, k,m,matrix[k][m]))
        memo[(i,j)] = mx
        return memo[(i,j)]
      
