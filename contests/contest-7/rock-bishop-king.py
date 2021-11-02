from collections import deque
def bfs(x, y, dx, dy):
    queue = deque([(x, y, 0)])
    visited = [[0 for _ in range(9)] for _ in range(9)]
    visited[x][y] = 1
    def valid(row, col):
        return 1 <= row < 9 and 1 <= col < 9 and not visited[row][col]
    DIR1 = ((1, 0),(0, -1), (-1, 0),(0, 1),(1, 1), (1, -1), (-1, 1), (-1, -1))
    while queue:
        curx, cury, steps = queue.popleft()
        if (curx, cury) == (dx, dy):
            return steps
        for ii, jj in DIR1:
            newr, newc = curx+ii, cury+jj
            if valid(newr, newc):
                visited[newr][newc] = 1
                queue.append((newr, newc, steps+1))

import math
if __name__ == '__main__':
    ix, iy, dx, dy = map(int, input().split())
    # rock
    rock, bishop, king = 0, 0, 0
    if ix == dx or iy == dy:
        rock = 1
        king = abs(dx-ix)+abs(dy-iy)
    else:
        king = bfs(ix, iy, dx, dy)
        rock = 2
    if ix != dx and iy != dy and (dy-iy)/(dx-ix) in [-1, 1]:
        bishop = 1
    elif (ix+iy)%2 == (dx+dy)%2:
        bishop = 2
    else:
        bishop = 0
    print(rock, bishop, king, sep=' ')