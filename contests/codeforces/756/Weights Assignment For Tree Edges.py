
def solve(n, parent, permutation):
    dist = [0]*n
    root = None
    for i, p in enumerate(permutation):
        dist[p-1] = i
    ans = [0]*n
    for node, pr in enumerate(parent):
        if node == pr-1: root = pr-1
        ans[node] = dist[node]-dist[pr-1]
        if ans[node] < 0: return [-1]
    if ans[root] != 0: return [-1]
    return ans
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        parent = list(map(int, input().split()))
        permutation = list(map(int, input().split()))
        ans.append(solve(n, parent, permutation))
    for a in ans:
        print(*a)