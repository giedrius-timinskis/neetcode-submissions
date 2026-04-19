class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree can't have more or less edges than nodes-1
        if len(edges) != (n-1):
            return False

        adj_list = [[] for _ in range(n)]
        for parent, child in edges:
            # Undirected graph - nodes go both ways
            adj_list[parent].append(child)
            adj_list[child].append(parent)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for next_node in adj_list[node]:
                # Since it's an undirected graph, child node will point back to its parent. When this happens, just skip.
                if next_node == parent:
                    continue
                # DFS until we go through all nodes or detect a cycle
                if not dfs(next_node, node):
                    return False
            # No cycle detected
            return True

        # Make sure to check that len(visited) == n to make sure there are no dangling, unconnected nodes (otherwise it's an invalid tree)
        return dfs(0, -1) and len(visited) == n