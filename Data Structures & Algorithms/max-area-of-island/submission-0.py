class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 0),  # up
        ]
        rows, cols = len(grid), len(grid[0])
        seen = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r >= rows or
                c >= cols or
                seen[r][c] or
                grid[r][c] == 0
            ):
                return 0

            seen[r][c] = True

            # Starting with 1 because we know that we started on a valid field
            area = 1
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)

            return area

        highest = 0
        for i in range(rows):
            for j in range(cols):
                curr = grid[i][j]
                if not seen[i][j] and curr == 1:
                    res = dfs(i, j)
                    highest = max(res, highest)

        return highest