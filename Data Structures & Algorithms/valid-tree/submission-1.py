class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree can't have more or less edges than nodes-1
        if len(edges) != n-1:
            return False

        adj_list = [[] for _ in range(n)]
        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)

        visited = set()
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, parent = q.popleft()

            for next_node in adj_list[node]:
                if next_node == parent:
                    continue
                if next_node in visited:
                    return False
                visited.add(next_node)
                q.append((next_node, node))

        return len(visited) == n