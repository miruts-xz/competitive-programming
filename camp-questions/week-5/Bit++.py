if __name__ == '__main__':
    X = 0
    n = int(input())
    while n:
        st = input()
        X += (1 if '+' in st else -1)
        n -= 1
    print(X)