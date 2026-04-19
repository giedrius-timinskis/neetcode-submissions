class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
            const ans = {};

    for (const s of strs) {
        const count = Array(26).fill(0);
        for (const c of s) {
            // This is kinda hacky but it will increment the index of the array for the current letter
            // i.e. for "abc" it will be [1, 1, 1, 0, 0, ... 0]
            count[c.charCodeAt(0) - "a".charCodeAt(0)]++;
        }

        // "Hash" the current letters and save this hash to our answer obj
        // After it's been hashed the order of the letters doesn't matter anymore since we're hashing by indexes
        const key = count.join("#");
        if (!ans[key]) {
            ans[key] = [];
        }

        ans[key].push(s);
    }

    return Object.values(ans);
    }
}
