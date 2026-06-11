class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if 0 <= row < m and 0 <= col < n and board[row][col] == "O":
                board[row][col] = "T"

                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        

        for row in range(m):
            for col in [0, n - 1]:
                if board[row][col] == "O":
                    dfs(row, col)
        
        for col in range(n):
            for row in [0, m - 1]:
                if board[row][col] == "O":
                    dfs(row, col)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "T":
                    board[row][col] = "O"
        