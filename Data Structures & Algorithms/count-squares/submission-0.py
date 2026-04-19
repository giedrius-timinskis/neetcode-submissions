class CountSquares:

    def __init__(self):
        self.points_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points_count[(point[0], point[1])] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point

        for x, y in self.points:

            # Skip straight lines
            if x == px or y == py:
                continue
            # Skip non-squares
            # Try to find the diagonal of provided point
            # This checks that the distance of diagonal is the same on x and y axis.
            # If it's equal, that means we have a candidate for a valid square
            if abs(y-py) != abs(x-px):
                continue

            # At this point we know that we have two opposite (diagonal) points that CAN form a valid square
            # Calculate how many squares use this diagonal
            corner1 = (x, py)   # horizontal from query
            corner2 = (px, y)   # vertical from query
            count1 = self.points_count[corner1]
            count2 = self.points_count[corner2]

            result += count1 * count2

        return result