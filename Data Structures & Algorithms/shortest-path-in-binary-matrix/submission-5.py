class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW_LEN, COL_LEN = len(grid), len(grid[0])
        # Entrance or exit is blocked - invalid input
        if grid[0][0] == 1 or grid[ROW_LEN-1][COL_LEN-1] == 1:
            return -1

        dirs = [
            [0, 1],  # Right
            [1, 0],  # Bottom
            [0, -1],  # Left
            [-1, 0],  # Top
            [-1, -1],  # Top-lft
            [-1, 1],  # Top-right
            [1, -1],  # Bottom-left
            [1, 1],  # Bottom-Right
        ]
        seen = set[tuple[int, int]]((0, 0))
        queue = deque[tuple[int, int]]([(0, 0)])

        result = 1

        while (queue):
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Found shortest path
                if r == ROW_LEN-1 and c == COL_LEN-1:
                    return result

                for dir_r, dir_c in dirs:
                    next_r, next_c = r + dir_r, c + dir_c

                    if (
                        0 <= next_r < ROW_LEN and
                        0 <= next_c < COL_LEN and
                        grid[next_r][next_c] == 0 and
                        (next_r, next_c) not in seen
                    ):
                        seen.add((next_r, next_c))
                        queue.append((next_r, next_c))

            result += 1

        return -1