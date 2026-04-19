INF = 2147483647
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [0, 1], [1, 0], [0, -1], [-1, 0]
        ROWS, COLS = len(grid), len(grid[0])

        q = deque[(int, int)]()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == INF
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))