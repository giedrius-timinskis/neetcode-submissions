class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        currSum = 0

        for num in nums:
            # Kadane's algorithm - https://en.wikipedia.org/wiki/Maximum_subarray_problem
            if currSum < 0:
                currSum = 0
            currSum += num
            maximum = max(maximum, currSum)

        return maximum