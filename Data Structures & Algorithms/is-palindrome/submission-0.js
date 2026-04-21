class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
    const str = s.toLowerCase().replace(/[^a-z0-9]/g, "");

    let l = 0;
    let r = str.length - 1;

    while (l < r) {
      console.log(str[l], str[r]);
      if (str[l] !== str[r]) {
        return false;
      }
      l++;
      r--;
    }

    return true;
  }
}
