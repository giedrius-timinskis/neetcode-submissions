class Solution {
    /**
     * @param {string} s
     * @return {string[][]}
     */
    partition(s) {
    const result = [];

    const isPalindrome = (str) => {
      let l = 0;
      let r = str.length - 1;

      while (l < r) {
        if (str[l] !== str[r]) return false;
        l++;
        r--;
      }
      return true;
    };

    const substrings = [];
    const recurse = (idx) => {
      if (idx >= s.length) {
        result.push([...substrings]);
        return;
      }

      for (let j = idx + 1; j <= s.length; j++) {
        const sub = s.substring(idx, j);
        if (isPalindrome(sub)) {
          substrings.push(sub);
          recurse(j);
          substrings.pop();
        }
      }
    };

    recurse(0);

    return result;
    }
}
