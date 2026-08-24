# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.status = True

        def dfs(node):
            if not node:
                return 0
            
            left_depth = (1+dfs(node.left)) if node.left else 0
            right_depth = (1+dfs(node.right)) if node.right else 0

            if abs(left_depth - right_depth)>1:
                self.status = False
            return max(left_depth, right_depth)
        
        dfs(root)

        return self.status

        