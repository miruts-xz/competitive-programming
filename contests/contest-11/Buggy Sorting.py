def buggySort():
    n = int(input())
    if n <= 2:
        print(-1)
    else:
        print(*[i for i in range(n, 0, -1)])
buggySort()