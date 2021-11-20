from math import inf
def solve(a, b):
    sa, la = inf, -inf
    a.sort(); b.sort()
    for na, nb in zip(a, b):
        if nb-na < 0 or nb-na > 1: return 'NO'
    return 'YES'
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        a, b = list(map(int, input().split())), list(map(int, input().split()))
        ans.append(solve(a, b))
    print(*ans, sep='\n')