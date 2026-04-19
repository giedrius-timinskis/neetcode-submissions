class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        removed = 0
        last_kept = None

        for curr in intervals:
            start, end = curr

            if not last_kept:
                last_kept = curr
                continue

            prev_end = last_kept[1]

            if start >= prev_end:
                last_kept = curr
                continue

            removed += 1

            if end <= prev_end:
                last_kept = curr

        return removed