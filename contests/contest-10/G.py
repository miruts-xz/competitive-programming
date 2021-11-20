from collections import defaultdict

def solve(n, m, k, row_weights, col_weights):
  dp = [[0] * m for _ in range(n)]  
  def valid(i,j):
    return 0 <= i < n and 0 <= j < m
  if k % 2:
    return [[-1] * m for _ in range(n)] 
  for step in range(k // 2):
    new_dp = [[0] * m for _ in range(n)] 
    for i in range(n):
      for j in range(m):
        cur_min = float('inf')
        if valid(i, j-1):
          temp = col_weights[i][j-1]+dp[i][j-1]
          cur_min = min(temp, cur_min)
        if valid(i, j+1):
          temp = col_weights[i][j]+dp[i][j+1]
          cur_min = min(temp, cur_min)
        if valid(i-1, j):
          temp = row_weights[i-1][j]+dp[i-1][j]
          cur_min = min(temp, cur_min)
        if valid(i+1, j):
          temp = row_weights[i][j]+dp[i+1][j]
          cur_min = min(temp, cur_min)
        new_dp[i][j] = cur_min*(2 if step==k//2-1 else 1)
    dp = new_dp
  return dp

if __name__ == '__main__':
  n, m, k = [int(val) for val in input().split()]
  col_weights = []
  row_weights = []
  for _ in range(n):
    col_weights.append(list(map(int, input().split())))
  for i in range(n - 1):
    row_weights.append(list(map(int, input().split())))
  ans = solve(n, m, k, row_weights, col_weights)
  for a in ans:
    print(*a)