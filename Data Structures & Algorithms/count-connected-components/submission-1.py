class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])

            return parents[x]

        def union(a, b):
            par_a, par_b = find(a), find(b)

            parents[par_b] = par_a

        for a, b in edges:
            union(a, b)

        uniques = set()
        for i in range(n):
            uniques.add(find(i))

        return len(uniques)