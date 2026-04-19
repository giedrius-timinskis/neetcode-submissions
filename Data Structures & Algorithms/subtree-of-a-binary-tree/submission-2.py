# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(root: Optional[TreeNode], sub: Optional[TreeNode]):
            # Reached the end of both nodes. Equal!
            if root == None and sub == None:
                return True

            # One of the nodes is empty - Not equal!
            if root == None or sub == None:
                return False

            if root.val != sub.val:
                return False

            return dfs(root.left, sub.left) and dfs(root.right, sub.right)

        if dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)