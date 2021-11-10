
def solve(n, jumps, slips):
    visited = set()
    jmps = -1
    def dfs(i, path=[]):
        nonlocal n, jumps, jmps
        if i == 0:
            if jmps == -1:
                jmps = path
            elif len(path) < len(jmps):
                jmps = path+[0]
            return
        if i in visited or jmps != -1:
            return
        visited.add(i)
        d = jumps[i]
        while jmps == -1 and d > 0:
            nxt = i-d+slips[i-d]
            if nxt in visited or nxt <= i: d -= 1; continue
            dfs(nxt, path+[max(0,i-d)])
            d -= 1
    dfs(n)
    return jmps



if __name__ == '__main__':
    ans = []
    n = int(input())
    jumps = [0]+list(map(int, input().split()))
    slips = [0]+list(map(int, input().split()))
    ans = solve(n, jumps, slips)
    
    if ans == -1:
        print(-1)
    else:
        print(len(ans))
        print(*ans)