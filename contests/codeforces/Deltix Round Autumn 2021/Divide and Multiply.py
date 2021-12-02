from math import log2
"""
1 3 4 6 8
"""
def solve(_, nums):
    maxx = 0
    for i, n in enumerate(nums):
        temp = n
        for j, m in enumerate(nums):
            if i == j: continue
            if m%2: temp += m; continue
            while m%2==0:
                temp += n
                n *= 2
                m //= 2
            temp += m
        maxx = max(maxx, temp)
    return maxx
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        ans.append(solve(n, list(map(int, input().split()))))
    print(*ans, sep='\n')