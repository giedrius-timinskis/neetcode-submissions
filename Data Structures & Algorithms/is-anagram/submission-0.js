class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        let sCache = {};

        for (let i = 0; i < s.length; i++) {
            if (sCache[s[i]]) {
                sCache[s[i]] += 1;
                continue;
            }

            sCache[s[i]] = 1;
        }

        for (let i = 0; i < t.length; i++) {
            const c = t[i];

            if (!sCache[c]) return false;

            sCache[c] -= 1;
        }

        if(Object.values(sCache).reduce((a, v) => a+=v, 0) > 0) return false
        return true;
    }
}
