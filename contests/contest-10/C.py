from math import inf
def solve(n, matrix):
    prefix1 = [0]*(n+1)
    prefix2 = [0]*(n+1)
    for i in range(1, n+1):
        prefix1[i] = prefix1[i-1]+matrix[0][i-1]
    for i in range(1, n+1):
        prefix2[i] = prefix2[i-1]+matrix[1][i-1]
    min_so_far = inf
    for i in range(n):
        min_so_far = min(min_so_far, max(prefix1[n]-prefix1[i+1], prefix2[i]))
    return min_so_far
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        matrix = [
            list(map(int, input().split())),
            list(map(int, input().split()))
        ]
        ans.append(solve(n, matrix))
    print(*ans, sep='\n')
