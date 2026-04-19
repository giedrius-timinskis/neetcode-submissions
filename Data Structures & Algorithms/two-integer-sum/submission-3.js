class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const cache = {};

        for (let i = 0; i < nums.length; i++) {
            let currentNumber = nums[i];
            let remainder = target - currentNumber;
            
            if (cache[remainder] !== undefined) {
                return [cache[remainder], i]
            }

            cache[currentNumber] = i;

        }

        return [-1, -1]
    }
}
