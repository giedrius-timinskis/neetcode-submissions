class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROW_LEN, COL_LEN = len(grid), len(grid[0])
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
        seen = set[tuple[int, int]]()
        seen.add((0, 0))
        queue = deque[tuple[int, int]]([(0, 0)])

        result = 1

        while (queue):
            q_len = len(queue)

            for _ in range(q_len):
                r, c = queue.popleft()

                # Found shortest path
                if r == ROW_LEN-1 and c == COL_LEN-1:
                    return result

                for dir_r, dir_c in dirs:
                    next_r, next_c = r + dir_r, c + dir_c

                    if not (
                        min(next_r, next_c) < 0 or
                        next_r >= ROW_LEN or
                        next_c >= COL_LEN or 
                        (next_r, next_c) in seen
                    ):
                        if grid[next_r][next_c] == 0:
                            queue.append((next_r, next_c))
                        seen.add((next_r, next_c))

            result += 1

        return -1