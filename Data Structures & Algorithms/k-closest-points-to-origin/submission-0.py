class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            # Calculate distance from origin (0, 0) to x, y coords
            distance = x**2 + y**2
            heapq.heappush(heap, [-distance, x, y])
            # If we have more points than k, we can clean up the furthest points since we won't need them
            if len(heap) > k:
                heapq.heappop(heap)

        # Return the top K
        result = []
        while heap:
            _, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result
