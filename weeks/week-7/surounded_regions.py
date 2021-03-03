class Solution:
    def solve(self, board: List[List[str]]) -> None:
        uncaptured = set()
        first = 0
        last = len(board) - 1
        for j in range(len(board[0])):
            if board[first][j] == "O":
                self.dfs(board, uncaptured, first, j)
            if board[last][j] == "O":
                self.dfs(board, uncaptured, last, j)
        last = len(board[0]) - 1
        for i in range(len(board)):
            if board[i][first] == "O":
                self.dfs(board, uncaptured, i, first)
            if board[i][last] == "O":
                self.dfs(board, uncaptured, i, last)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in uncaptured:
                    board[i][j] = "X"

    def dfs(self, board: List[List[int]], uncaptured: set, r, c):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in uncaptured or board[r][c] == "X":
            return
        uncaptured.add((r, c))
        for r, c in [(r + 1, c), [r, c + 1], (r - 1, c), (r, c - 1)]:
            self.dfs(board, uncaptured, r, c)




