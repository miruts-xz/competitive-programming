from collections import deque, namedtuple
import sys
sys.setrecursionlimit(2500)
Loc = namedtuple('Loc', ('x', 'y'))
def can_move(dim, queen, king, target):
    danger = set()
    r, c = queen.x, queen.y
    DIR1 = ((1, 0),(0, -1), (-1, 0),(0, 1),(1, 1), (1, -1), (-1, 1), (-1, -1))
    for col in range(dim):
        danger.add((r, col))
    for row in range(dim):
        danger.add((row, c))
    for x, y in zip(range(r, 0, -1), range(c, 0, -1)):
        danger.add((x, y))
    for x, y in zip(range(r, dim), range(c, dim)):
        danger.add((x, y))
    for x, y in zip(range(r, dim), range(c, 0, -1)):
        danger.add((x, y))
    for x, y in zip(range(r, 0, -1), range(c, dim)):
        danger.add((x, y))
    visited = [[0 for _ in range(1, dim)] for _ in range(1, dim)]
    visited[king.x][king.y] = 1
    def valid(row,col):
        return 1 <= row < dim and 1 <= col < dim and (row, col) not in danger and not visited[row][col]
    def dfs(x, y):
        if (x, y) == (target.x, target.y):
            return True
        for ii, jj in DIR1:
            newr, newc = x+ii, y+jj
            if valid(newr, newc):
                visited[newr][newc] = 1
                if dfs(newr,newc):
                    return True
        return False
    return dfs(king.x, king.y)
if __name__ == "__main__":
    dim = int(input())+1
    qx, qy = map(int, input().split())
    kx, ky = map(int, input().split())
    tx, ty = map(int, input().split())
    queen = Loc(qx, qy)
    king = Loc(kx, ky)
    target = Loc(tx, ty)
    if (king.x < queen.x and target.x > queen.x) or (king.x > queen.x and target.x < queen.x) or (king.y > queen.y and target.y < queen.y) or (king.y < queen.y and target.y > queen.y):
        print("NO")
    else:
        print('YES')