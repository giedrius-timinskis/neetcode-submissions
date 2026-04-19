class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_col_zero = False
        rows = len(matrix)
        cols = len(matrix[0])

        # First pass - mark all locations of rows and columns that should be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_zero = True
                    if c == 0:
                        first_col_zero = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Second pass - iterate through the first row and first col to see which rows+cols in matrix need to be zeroed out
        # initial_row = False
        # [1, 0, 3],
        # [0, 0, 5],
        # [6, 7, 8]
        # Mark columns (Skip 0 because we use it for tracking)
        for col_to_nuke in range(1, cols):
            if matrix[0][col_to_nuke] == 0:
                for r in range(rows):
                    matrix[r][col_to_nuke] = 0

        # Mark rows (Skip 0 because we use it for tracking)
        for row_to_nuke in range(1, rows):
            if matrix[row_to_nuke][0] == 0:
                for c in range(cols):
                    matrix[row_to_nuke][c] = 0

        # Now clean up the first row/col
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

        