class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        seen = {}

        def dfs(i, j):
            if len(text1) == i or len(text2) == j:
                return 0

            if (i, j) in seen:
                return seen[(i, j)]

            if text1[i] == text2[j]:
                seen[(i, j)] = 1+dfs(i+1, j+1)
            else:
                seen[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))

            return seen[(i, j)]
        return dfs(0, 0)