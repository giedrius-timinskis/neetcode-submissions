# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        q1 = deque[TreeNode]([p])
        q2 = deque[TreeNode]([q])

        while q1:
            t1, t2 = q1.popleft(), q2.popleft()

            # Both empty nodes. Equal, so continue.
            if not t1 and not t2:
                continue

            # Only one node is empty. Not equal.
            if not t1 or not t2:
                return False

            # Values are not the same. Not equal.
            if t1.val != t2.val:
                return False

            q1.append(t1.left)
            q1.append(t1.right)
            q2.append(t2.left)
            q2.append(t2.right)

        return True
        