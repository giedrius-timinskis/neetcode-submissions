class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [
            [] for i in range(len(nums) + 1)
        ]  # Lowest count will start at 1, so we want to add an extra bucket so it doesn't go out of bounds

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            print(buckets[i])
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result