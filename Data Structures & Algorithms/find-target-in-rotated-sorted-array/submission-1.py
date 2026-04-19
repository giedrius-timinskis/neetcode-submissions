class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            curr = nums[mid]

            if target == curr:
                return mid

            # This means left side is sorted
            if nums[l] <= curr:
                if nums[l] <= target < curr:
                    # We know that the target number is on the left side
                    r = mid - 1
                else:
                    # Otherwise we know that it's on the right side
                    l = mid + 1
            else:
                # This means that the right side is sorted
                if curr < target <= nums[r]:
                    # We know that target is on the right side
                    l = mid + 1
                else:
                    # We know that the target is on the left side
                    r = mid - 1

        return -1