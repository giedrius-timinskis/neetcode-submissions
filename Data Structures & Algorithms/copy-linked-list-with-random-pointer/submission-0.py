"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_nodes = {None: None}

        curr = head
        while curr:
            clone = Node(curr.val)
            old_nodes[curr] = clone
            curr = curr.next

        curr = head
        while curr:
            copy = old_nodes[curr]
            copy.next = old_nodes[curr.next]
            copy.random = old_nodes[curr.random]
            curr = curr.next

        return old_nodes[head]