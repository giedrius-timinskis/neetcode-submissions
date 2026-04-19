class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        dirs = [0, 1], [1, 0], [0, -1], [-1, 0]
        ROWS, COLS = len(grid), len(grid[0])

        q = deque[(int, int)]()
        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.appendleft((r, c))

        while q:
            distance += 1

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc

                    if (
                       nr < 0 or nr == ROWS or  # out of bounds rows
                       nc < 0 or nc == COLS or  # out of bounds cols
                       # next tile untraversable or treasure
                       grid[nr][nc] in (-1, 0) or
                       # Next tile already explored AND tile's distance is higher than curr distance
                       (grid[nr][nc] != INF and distance > grid[nr][nc])
                       ):
                        continue
                    grid[nr][nc] = distance
                    q.append((nr, nc))