class Solution:
    def rob(self, nums: List[int]) -> int:
        def search(n):
            rob1, rob2 = 0, 0

            for num in n:
                temp = max(rob1+num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        if len(nums) == 1:
            return nums[0]

        return max(search(nums[:-1]), search(nums[1:]))