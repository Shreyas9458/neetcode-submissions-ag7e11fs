class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False

        def dfs(i, j, curr):
            if not curr:
                nonlocal result
                result = True
                return
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                    if board[x+i][y+j] in curr[0]:
                        letter = board[x + i][y + j]
                        board[i + x][j + y] = "#"
                        dfs(x+i, y+j, curr[1:])
                        if result:
                            break
                        board[i+x][j+y] = letter
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    letter = board[i][j]
                    board[i][j] = "#"
                    dfs(i, j, word[1:])
                    if result:
                        break
                    board[i][j] = letter
                    
        return result