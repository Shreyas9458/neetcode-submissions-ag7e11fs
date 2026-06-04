class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return list()

        m, n = len(heights), len(heights[0])

        def dfs(row, col, seen):
            seen.add((row, col))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = dr + row, dc + col
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen and heights[x][y] >= heights[row][col]:
                    dfs(x, y, seen)
        
        pacific, atlantic = set(), set()
        for j in range(n):
            dfs(0, j, pacific)
        for i in range(m):
            dfs(i, 0, pacific)
        
        for j in range(n):
            dfs(m - 1, j, atlantic)
        for i in range(m):
            dfs(i, n-1, atlantic)

        return list(pacific & atlantic)
        