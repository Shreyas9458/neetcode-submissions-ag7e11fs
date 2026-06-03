class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        gold = 0
        water = -1
        land = 2147483647

        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= (x+dx) < len(grid) and 0 <= (y+dy) < len(grid[0]) and grid[x+dx][y+dy] == land:
                    grid[x+dx][y+dy] = grid[x][y] + 1
                    queue.append((x+dx, y+dy))
                