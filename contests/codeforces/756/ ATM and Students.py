"""
2 9
"""
def solve(n, s, requests):
    prefix = [0]*(n+1)
    for i, r in enumerate(requests, 1):
        prefix[i] = r+prefix[i-1]
    left, right = -1, -1
    l , r = 0, 1
    maxx = 0
    while r <= n:
        if l == r: r += 1
        elif prefix[r]-prefix[l] >= -s:
            if r-l > maxx:
                left, right = l+1, r
                maxx = r-l
            r += 1
        else:
            l += 1
            
    if left == -1: return [-1]
    return [left, right]
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, s = map(int, input().split())
        requests = list(map(int, input().split()))
        ans.append(solve(n, s, requests))
    for a in ans:
        print(*a)