if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        ans.append(n*m//3 + (1 if m*n%3 else 0))
    print(*ans, sep='\n')