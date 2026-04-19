class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        # [1, 2, 2, 4, 5, 6, 9]
        def dfs(i: int, curr: List[int], total: int):
            if total == target:
                results.append(curr.copy())
                return True
            if total > target or i >= len(candidates):
                return False

            for j in range(i, len(candidates)):

                # Skip duplicates at the same recursion depth
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                curr.append(candidates[j])
                dfs(j+1, curr, total + candidates[j])
                curr.pop()
        dfs(0, [], 0)
        return results