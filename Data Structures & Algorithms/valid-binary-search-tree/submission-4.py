# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        self.status = True
        self.prev = None

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if self.prev is not None and self.prev>=node.val:
                self.status = False
            self.prev = node.val
            dfs(node.right)
        
        dfs(root)

        return self.status



        