class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const char_indices = new Map();
        let longest = 0;
        let l = 0;

        for (let r = 0; r < s.length; r++) {
            if (char_indices.get(s[r]) != undefined) {
                l = Math.max(l, char_indices.get(s[r]) + 1);
            }

            char_indices.set(s[r], r);
            longest = Math.max(longest, r - l + 1);
        }

        return longest;
    }
}
