def solve(n,k,walks):
    extra = 0
    prev = walks[0]
    for day in range(1, n):
        min_walk = k-walks[day-1]
        if min_walk > walks[day]:
            additional = min_walk-walks[day]
            walks[day] += additional 
            extra += additional
    return extra, walks

if __name__ == '__main__':
    n, k = map(int, input().split())
    ans = solve(n,k,list(map(int, input().split())))
    print(ans[0])
    print(*ans[1])