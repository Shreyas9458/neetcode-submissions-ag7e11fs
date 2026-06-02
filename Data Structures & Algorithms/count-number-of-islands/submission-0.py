class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.dfs(row, col, grid)
                    result += 1
        return result
    def dfs(self, row, col, grid):

        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "0":
            grid[row][col] = "0"
            self.dfs(row + 1, col, grid)
            self.dfs(row - 1, col, grid)
            self.dfs(row, col + 1, grid)
            self.dfs(row, col - 1, grid)
        else:
            return
        