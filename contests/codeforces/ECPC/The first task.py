from functools import lru_cache
import sys
sys.setrecursionlimit(100002)
def solve(n, nums):
    DP = [0]*(n+1)
    
    # for 
    nums.sort()
    @lru_cache(None)
    def dfs(i, look):
        if i == n: return 0
        
        if nums[i] == look:
            return dfs(i+1, look+1)
        if nums[i] < look:
            return 1 + dfs(i+1, look)
        return min(nums[i] - (nums[i-1] if i > 0 else 0) -1 + dfs(i+1, look+1), n-i+1)
    return dfs(0, 1)

if __name__ == '__main__':
    ans = []
    with open('task.in', 'r') as fin:
        q = int(fin.readline())
        for _ in range(q):
            n = int(fin.readline())
            ans.append(solve(n, list(map(int, fin.readline().split()))))
    print(*ans, sep='\n')