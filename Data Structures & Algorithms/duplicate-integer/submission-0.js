class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const cache = {}

        for (let i = 0; i < nums.length; i++) {
            if (cache[nums[i]]) return true;
            cache[nums[i]] = true;
        }

        return false;
    }
}
