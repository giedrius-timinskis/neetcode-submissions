class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_len = 0
        longest_start = 0
        for i in range(len(s)):

            # Odd s length
            l, r = i, i
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                length = r - l + 1
                if length >= longest_len:
                    longest_len = length
                    longest_start = l
                l = l-1
                r = r+1

            l, r = i, i+1
            # Even s length
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                length = r - l + 1
                if length >= longest_len:
                    longest_len = length
                    longest_start = l
                l = l-1
                r = r+1

        return s[longest_start:longest_start+longest_len]