from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        visited = set()
        self.dfs(board, visited, click[0], click[1])
        return board

    def dfs(self, board, visited, r, c):
        if (r, c) in visited:
            return
        count = self.adjMines(board, r, c)

        if count == 0:
            board[r][c] = "B"
        else:
            board[r][c] = str(count)
        for i, j in [[r, c + 1], [r, c - 1], [r - 1, c], [r + 1, c], [r + 1, c + 1], [r + 1, c - 1], [r - 1, c + 1],
                     [r - 1, c - 1]]:
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == "E" and board[r][c] == "B" and (
            i, j) not in visited:
                self.dfs(board, visited, i, j)

    def adjMines(self, board, r, c):
        count = 0
        for i, j in [[r, c + 1], [r, c - 1], [r - 1, c], [r + 1, c], [r + 1, c + 1], [r + 1, c - 1], [r - 1, c + 1],
                     [r - 1, c - 1]]:
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                if board[i][j] == "M":
                    count += 1
        return count



