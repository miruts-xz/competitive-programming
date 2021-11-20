def dosth(n, st):
    arr = []
    ids = sorted(st)
    for x, (i, j) in enumerate(zip(st, ids)):
        if i != j:
            arr.append(x + 1)
    if not arr:
        print(0)
        return
    print(1)
    print(len(arr), *arr)


t = eval(input())
for _ in range(t):
    n = eval(input())
    st = input()
    dosth(n, st)