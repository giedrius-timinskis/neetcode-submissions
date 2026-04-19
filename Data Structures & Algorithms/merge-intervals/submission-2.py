class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(end, last_end)
            else:
                merged.append([start, end])

        return merged
