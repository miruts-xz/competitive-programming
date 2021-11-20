
def solve(u,v):
    return [-u**2, v**2]

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        u, v = map(int, input().split())
        ans.append(solve(u,v))
    for a in ans:
        print(*a)