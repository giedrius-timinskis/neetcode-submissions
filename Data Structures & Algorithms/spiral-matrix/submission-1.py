class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # Remaining column width (start with full width)
        left = 0
        right = len(matrix[0])
        # Remaining row height (start with full height)
        top = 0
        bottom = len(matrix)

        # While we have unexplored tiles, keep iterating
        while left < right and top < bottom:
            # First go left -> right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # Then go right side top -> bottom
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1

            # Account for 1 row only inputs
            if not (left < right and top < bottom):
                break

            # Then go bottom side right -> left
            # This one is a bit tricky because we need to make sure that we don't include the column that we already iterated in the result (right) and the column we will iterate through next (left)
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            # lastly, go left side bottom -> top
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])
            left += 1

        return result