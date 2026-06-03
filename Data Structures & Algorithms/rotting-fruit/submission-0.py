class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        freshOranges = 0
        mins = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    freshOranges += 1
        
        if not freshOranges:
            return 0
        
        while queue and freshOranges > 0:
            mins += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshOranges -= 1
                        queue.append((nr, nc))
        return mins if freshOranges == 0 else -1