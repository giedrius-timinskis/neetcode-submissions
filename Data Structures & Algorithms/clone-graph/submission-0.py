"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def dfs(n: Node):
            if n in cloned:
                return cloned[n]

            copy = Node(n.val)
            cloned[n] = copy

            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        if node:
            return dfs(node)
        return None