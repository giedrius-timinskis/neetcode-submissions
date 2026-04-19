class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(    s)
        res = 0

        for i in range(n):

            left, right = i, i
            while left > -1 and right < n and s[left] == s[right]:
                res += 1
                left = left-1
                right = right+1

            left, right = i, i+1
            while left > -1 and right < n and s[left] == s[right]:
                res += 1
                left = left-1
                right = right+1

        return res