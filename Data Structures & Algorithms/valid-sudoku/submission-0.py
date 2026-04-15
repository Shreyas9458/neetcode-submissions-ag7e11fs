from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board[0])

        row = defaultdict(set)
        col = defaultdict(set) 
        box = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    val = board[i][j]
                    if val in row[i] or val in col[j] or val in box[(i//3, j//3)]:
                        return False
                    row[i].add(val)
                    col[j].add(val)
                    box[(i//3, j//3)].add(val)
        
        return True