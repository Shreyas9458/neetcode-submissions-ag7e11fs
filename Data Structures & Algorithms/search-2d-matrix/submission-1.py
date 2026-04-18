class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS*COLS - 1

        while left <= right:
            m = left + (right - left) //2
            row = m // COLS
            col = m % COLS
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                left = m + 1
            elif target < matrix[row][col]:
                right = m - 1
        return False