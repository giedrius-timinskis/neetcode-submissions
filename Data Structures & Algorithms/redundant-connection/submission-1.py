class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]

        def find(x: int):
            # If curr node is not the parent, then keep climbing until we find the parent
            if x != parents[x]:
                # This is basically memo - it creates a connection from current node to parent
                parents[x] = find(parents[x])

            # Parent found
            return parents[x]

        def union(a: int, b: int):
            par_a, par_b = find(a), find(b)

            # This pair creates a cycle!
            if par_a == par_b:
                return False

            parents[par_b] = par_a
            return True

        # Iterate through every pair and
        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []