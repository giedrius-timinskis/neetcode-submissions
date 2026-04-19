class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {n: True}

        def recurse(i):
            if i in memo:
                return memo[i]

            if i > n:
                return False
            if i == n:
                return True

            for word in wordDict:
                w_len = len(word)
                substr = s[i:i+w_len]
                if substr == word:
                    if recurse(i+w_len):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        res = recurse(0)
        return res
