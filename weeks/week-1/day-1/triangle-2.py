def triangle2(n: int):
    for i in range(1, n + 1):
        j = 2 * i + 1
        spaces = (2 * n + 1 - j) // 2
        print('{}{}'.format(' ' * spaces, '* ' * i), end='\n')


triangle2(10)
