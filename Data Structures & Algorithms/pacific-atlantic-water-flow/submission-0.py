class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, seen, prev_height):
            if (
                (r, c) in seen or  # Already explored
                r < 0 or c < 0 or r >= ROWS or c >= COLS or  # out of bounds
                heights[r][c] < prev_height  # Curr tile is higher - invalid
            ):
                return

            seen.add((r, c))
            for nr, nc in dirs:
                dfs(r+nr, c+nc, seen, heights[r][c])

        for c in range(COLS):
            # Run dfs for every pacific (top edge) column
            dfs(0, c, pacific, heights[0][c])
            # Then run dfs for every atlantic (bottom edge) column
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            # run dfs for every pacific (left edge) column
            dfs(r, 0, pacific, heights[r][0])
            # run dfs for every atlantic (right edge) column
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        result = []
        # Iterate through every cell and see if it can reach both oceans (in both pacific and atlantic sets)
        for r in range(ROWS):
            for c in range(COLS):
                curr = (r, c)
                if curr in pacific and curr in atlantic:
                    result.append([r, c])

        return result