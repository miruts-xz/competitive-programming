if __name__ == '__main__':
    n,m,a = map(int, input().split())
    verts = n//a + (n%a > 0)
    horz = m//a + (m%a > 0)
    print(verts*horz)