if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        m, n = map(int, input().split())
        if m == n == 1: ans.append(0); continue
        ans.append(min(m, n, 2))
    print(*ans, sep='\n')