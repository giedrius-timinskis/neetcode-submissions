class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        n = len(grid)
        queue = deque[tuple[int, int]]()
        fresh = 0

        # First pass - find all starting points (rotten fruit):
        for i in range(n):
            for j in range(len(grid[i])):
                c = grid[i][j]
                if c == 1:
                    fresh += 1
                if c == 2:
                    queue.append((i, j))

        result = 0

        # BFS
        while fresh > 0 and len(queue):
            times = len(queue)

            for _ in range(times):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < n and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1

            result += 1

        if fresh == 0:
            return result
        return -1