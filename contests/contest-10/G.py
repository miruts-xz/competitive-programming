from collections import defaultdict

def solve(n, m, k, adj):
  dp = [[0] * m for _ in range(n)]  

  if k % 2:
    return [[-1] * m for _ in range(n)] 

  for _ in range(k // 2):
    new_dp = [[0] * m for _ in range(n)] 
    for i in range(n):
      for j in range(m):
        cur_min = float('inf')
        for n_i, n_j, wt in adj[i, j]:
          cur_min = min(cur_min, dp[n_i][n_j] + wt)
        new_dp[i][j] = cur_min
    dp = new_dp


  for i in range(n):
    for j in range(m):
      dp[i][j] *= 2

  return dp

if __name__ == '__main__':
  n, m, k = [int(val) for val in input().split()]
  adj = defaultdict(list)

  for i in range(n):
    for j, weight in enumerate(list(map(int, input().split()))):
      adj[i, j].append([i, j + 1, weight])
      adj[i, j + 1].append([i, j, weight])

  for i in range(n - 1):
    for j, weight in enumerate(list(map(int, input().split()))):
      adj[i, j].append([i + 1, j, weight])
      adj[i + 1, j].append([i, j, weight])

  ans = solve(n, m, k, adj)
  for a in ans:
    print(*a)