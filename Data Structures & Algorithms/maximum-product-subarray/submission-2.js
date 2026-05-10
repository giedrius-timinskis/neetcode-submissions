class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
    let result = nums[0];
    let currMin = 1;
    let currMax = 1;

    for (let i = 0; i < nums.length; i++) {
      const num = nums[i];
      const temp = currMax * num;
      currMax = Math.max(num, Math.max(num * currMax, num * currMin));
      currMin = Math.min(num, Math.min(temp, num * currMin));

      result = Math.max(result, currMax);
    }

    return result;
    }
}
