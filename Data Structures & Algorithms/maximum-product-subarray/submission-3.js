class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
        let result = nums[0];
        // Best/worst product of a subarray ending at current index
        let maxEndingHere = nums[0];
        let minEndingHere = nums[0];

        for (let i = 1; i < nums.length; i++) {
        const num = nums[i];
        // Make sure we calculate from prev state before overwriting
        const prevMax = maxEndingHere;
        const prevMin = minEndingHere;

        // Three possibilities:
        // 1. Start new subarray at current number
        // 2. Extend previous max product subarray
        // 3. Extend previous min product subarray
        maxEndingHere = Math.max(num, prevMax * num, prevMin * num);
        minEndingHere = Math.min(num, prevMax * num, prevMin * num);

        result = Math.max(result, maxEndingHere);
        }

        return result;
    }
}
