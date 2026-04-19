class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let found = false;
        let left = 0;

        while (!found) {       
            let right = left + 1;
            for (let i = 0; i < nums.length; i++) {
                
                let leftVal = nums[left];
                let rightVal = nums[right];

                if (leftVal + rightVal === target) {
                    return [left, right];
                }

                right++;
                if (right === nums.length) break;
            }

            left++;
        }
    }
}
