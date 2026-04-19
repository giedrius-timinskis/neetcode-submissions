class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = []
        for i in range(len(grid)):
            seen.append([])
            for _ in grid[i]:
                seen[i].append(False)

        def dfs(grid, r, c):
            if (
                min(r, c) < 0 or
                r >= len(grid) or
                c >= len(grid[0])
                or seen[r][c]
            ):
                return False

            if grid[r][c] == '0':
                seen[r][c] = True
                return False

            seen[r][c] = True

            dfs(grid, r+1, c)  # up
            dfs(grid, r-1, c)  # down
            dfs(grid, r, c+1)  # right
            dfs(grid, r, c-1)  # left

            return True

        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[i])):
                if seen[r][c]:
                    continue

                if grid[r][c] == '0':
                    seen[r][c] = True
                    continue

                dfs(grid, r, c)

                result += 1

        return result