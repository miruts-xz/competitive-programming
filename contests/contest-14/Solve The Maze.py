
import sys
from collections import deque
sys.setrecursionlimit(10000)
def valid(i, j):
    return 0 <= i < n and 0 <= j < m
def solve(n, m, maze, gcount):
    dirs = (1, 0, -1, 0, 1)
    count = 0
    visited = [[False]*m for _ in range(n)]
    queue = deque([(n-1, m-1)])
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            newr, newc = i+dirs[k], j+dirs[k+1]
            if not valid(newr, newc) or maze[newr][newc] == '#' or visited[newr][newc]: continue
            visited[newr][newc] = True
            count += (1 if maze[newr][newc] == 'G' else 0)
            queue.append((newr, newc))
    return 'Yes' if gcount == count else 'No'
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        matrix = []
        countG = 0
        bindices = []
        for i in range(n):
            current = []
            for j,c in enumerate(input()):
                if c == 'B':
                    bindices.append((i,j))
                if c == 'G':
                    countG += 1
                current.append(c)
            matrix.append(current)
        dirs = (1, 0, -1, 0, 1)
        invalid = False
        for i, j in bindices:
            if invalid: break
            for k in range(4):
                newr, newc = i+dirs[k], j + dirs[k+1]
                if valid(newr, newc) and (matrix[newr][newc] == '.' or matrix[newr][newc] == 'G'):
                    if matrix[newr][newc] == 'G' or (newr, newc) == (n-1, m-1) and countG:
                        ans.append('No')
                        invalid = True
                        break
                    matrix[newr][newc] = '#'
        if not invalid:
            ans.append(solve(n, m, matrix, countG))
    print(*ans, sep='\n')