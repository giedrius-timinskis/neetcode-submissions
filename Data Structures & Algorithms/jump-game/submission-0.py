class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])

        while q:
            idx = q.popleft()
            val = nums[idx]

            if idx == len(nums)-1:
                return True

            for r in range(val):
                candidate = 1+r+idx
                if candidate < len(nums):
                    q.append(candidate)

        return False