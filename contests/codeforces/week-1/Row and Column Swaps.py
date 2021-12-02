
def solve(opt, a, b):
    if opt == 'A': return matrix[rmap[a-1]][cmap[b-1]]
    if opt == 'R':
        rmap[a-1], rmap[b-1] = rmap[b-1], rmap[a-1]
    else:
        cmap[a-1], cmap[b-1] = cmap[b-1], cmap[a-1]
        
if __name__ == '__main__':
    ans = []
    n, k = map(int, input().split())
    matrix = []

    rmap = {i: i for i in range(n)}
    cmap = {i: i for i in range(n)}

    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    for _ in range(k):
        opt, a, b = input().split()
        a, b = int(a), int(b)
        res = solve(opt, a, b)
        if opt == 'A':
            ans.append(res)
    print(*ans, sep='\n')