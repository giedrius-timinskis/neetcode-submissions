class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [
            [0, 1],  # Right
            [1, 0],  # Down
            [0, -1],  # Left
            [-1, 0]  # Up
        ]
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]
            board[r][c] = '#'  # Mark current tile as seen

            # Attempt to find the full string
            for dr, dc in dirs:
                if dfs(r+dr, c+dc, i+1):
                    return True

            # Full string not found - backtrack
            board[r][c] = temp
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False