class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for idx, curr in enumerate(nums):
            # We can end calc here because we know that all calulations to the right of current number will result in more than 0
            if curr > 0:
                break

            # Skip duplicate values
            if idx > 0 and curr == nums[idx-1]:
                continue

            l_idx, r_idx = idx+1, len(nums)-1
            while l_idx < r_idx:
                sum = curr + nums[l_idx] + nums[r_idx]
                if sum < 0:
                    l_idx += 1
                elif sum > 0:
                    r_idx -= 1
                else:
                    result.append([curr, nums[l_idx], nums[r_idx]])
                    l_idx += 1
                    r_idx -= 1
                    # Optional: Skip duplicates again to avoid recalculating them
                    while nums[l_idx] == nums[l_idx-1] and l_idx < r_idx:
                        l_idx += 1

        return result