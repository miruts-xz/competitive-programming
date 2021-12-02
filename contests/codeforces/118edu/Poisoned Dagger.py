
def solve(n, h, attacks):
    gaps = [attacks[i]-attacks[i-1] for i in range(1, n)]
    gaps.sort()
    mn = h//n + (1 if h%n else 0)
    rem = h
    
    spared = 0
    for i, gap in enumerate(gaps):
        if gap >= mn:
            if mn*(n-i) < rem:
                mn = min(gap, rem//(n-i) + (1 if rem%(n-i) else 0))
                rem -= mn
            else:
                rem = 0
                break
        else:
            # spared += mn-gap
            rem -= gap
    if rem-mn > 0:
        mn += rem-mn
    return mn
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, h = map(int, input().split())
        ans.append(solve(n, h, list(map(int, input().split()))))
    print(*ans, sep='\n')