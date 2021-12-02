

def solve(n ,visits):
    ans = [0]*(n+1)
    building = [(visits[i], i+1) for i in range(n)]
    building.sort(reverse=True)
    cost = 0
    l,r = -1, 1
    for vt, ind in building:
        if abs(l) < abs(r):
            ans[ind] = l
            cost += vt*2*abs(l)
            l -= 1
            
        else:
            ans[ind] = r
            cost += vt*2*abs(r)
            r += 1
            
    return [cost, *ans]

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n = int(input())
        visits = list(map(int, input().split()))
        ans.append(solve(n, visits))
    for a in ans:
        print(a[0])
        print(*a[1:])
