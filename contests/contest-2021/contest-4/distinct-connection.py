from collections import namedtuple

def construct(i, gangs, visited, roads):
    if i in visited:
        return
    visited.add(i)
    for j, nbr in enumerate(gangs):
        if j not in visited and gangs[i] != nbr:
            roads.append([i+1, j+1])
            construct(j, gangs,visited, roads)

if __name__ == '__main__':
    t = int(input())
    gangs = []
    for _ in range(t):
        input()
        gangs.append(list(map(int, input().split())))
    ans = []
    visited = set()
    for gang in gangs:
        roads = []
        visited.clear()
        construct(0, gang, visited, roads)
        ans.append(roads)
    for k, a in enumerate(ans):
        if len(a) != len(gangs[k])-1:
            print("NO")
            continue
        print("YES")
        for r1, r2 in a:
            print(r1, r2, sep=' ')
    
