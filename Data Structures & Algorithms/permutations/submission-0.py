class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack([], nums, [False] * len(nums))
        return self.result

    def backtrack(self, permutation: List[int], nums: List[int], pick: List[bool]):
        if len(permutation) == len(nums):
            self.result.append(permutation.copy())
            return

        for i in range(len(nums)):
            if not pick[i]:
                permutation.append(nums[i])
                pick[i] = True
                self.backtrack(permutation, nums, pick)
                permutation.pop()
                pick[i] = False