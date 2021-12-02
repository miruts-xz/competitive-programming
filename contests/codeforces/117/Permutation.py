
def solve(n, a, b):
    left = [a]
    right = [b]
    r = n
    while r > 0 and len(left) < n//2 and r > a:
        if r != b: left.append(r)
        r -= 1
    l = 1
    while l <= n and len(right) < n//2 and l < b:
        if l != a: right.append(l)
        l += 1
    if len(left) < n//2 or  len(right) < n//2:
        return [-1]
    return left+right 

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        ans.append(solve(*list(map(int, input().split()))))
    for a in ans:
        print(*a)
