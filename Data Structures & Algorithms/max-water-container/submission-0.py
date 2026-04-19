class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = 0

        while l < r:
            distance = r-l
            lower_height = min(heights[l], heights[r])
            area = distance*lower_height

            max_area = max(area, max_area)

            if heights[l] < heights[r] or heights[r] == heights[l]:
                l += 1
            else:
                r -= 1

        return max_area