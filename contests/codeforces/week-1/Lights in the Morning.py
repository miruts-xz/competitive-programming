
def solve(N, D, lights):

    for loc, start, g, r in lights:
        total = g+r
        if (loc-start)%total > g or loc-start < 0: return 'NO'
    return 'YES'
if __name__ == '__main__':
    ans = []
    N, D = map(int, input().split())
    lights = []
    for _ in range(N):
        lights.append(list(map(int, input().split())))
    print(solve(N, D, lights))