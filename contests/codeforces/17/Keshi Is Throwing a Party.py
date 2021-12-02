from heapq import heappush, heappop

def solve(n, friends):
    heap = []
    for i, ls in enumerate(friends):
        poorer_support = min(ls[1], i-0)
        richer_support = min(ls[0], n-i)
        heappush((poorer_support, richer_support, i))
    


if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        friends = [list(map(int, input().split())) for _ in range(n)]
        ans.append(solve(n, friends))
    print(*ans, sep='\n')