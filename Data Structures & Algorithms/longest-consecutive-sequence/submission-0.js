class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const seen = new Set(nums);
        let longest = 0;

        for (let num of seen) {
        if (!seen.has(num - 1)) {
            let currLongest = 1;
            let curr = num;
            while (seen.has(curr + 1)) {
            currLongest += 1;
            curr += 1;
            }
            longest = Math.max(longest, currLongest);
        }
        }

        return longest;
    }
}
