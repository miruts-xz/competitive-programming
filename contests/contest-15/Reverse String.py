from functools import lru_cache
import sys
sys.setrecursionlimit(5000)
def solve(s, t):

    @lru_cache(maxsize=None)
    def dfs(i, j, turn=True):
        if j == len(t): return True
        if i+1 < len(s) and s[i+1] == t[j] and turn:
            if dfs(i+1, j+1, turn): return True
        if i-1 >= 0 and s[i-1] == t[j]:
            if dfs(i-1, j+1, False): return True
        
        return False
    for i,c in enumerate(s):
        if c != t[0]: continue
        if dfs(i, 1, 1): return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(input(), input()))
    print(*ans, sep='\n')