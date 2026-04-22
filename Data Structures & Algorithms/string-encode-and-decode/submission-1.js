class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = "";

        // ['Hello', 'World'] => '5#Hello5#World'
        // This is resilient to input like '#5', because we would encode it as '2##5'
        // So when we decode we just need to parse number until we hit the #, then we can safely skip the string length
        for (const str of strs) {
        encoded += `${str.length}#${str}`;
        }

        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(s) {
        const decoded = [];

        let i = 0;
        let currLen = "";

        while (i < s.length) {
        // This condition means we are currently parsing the length
        if (s[i] !== "#") {
            currLen += s[i];
            i++;
            // This condition means we know the length of the string so we can determine what the string is
        } else {
            // Get substring, append to decoded, skip i
            const len = Number(currLen);
            const res = s.substring(i + 1, i + 1 + len);
            decoded.push(res);
            currLen = "";
            i += len + 1;
        }
        }

        return decoded;
    }
}
