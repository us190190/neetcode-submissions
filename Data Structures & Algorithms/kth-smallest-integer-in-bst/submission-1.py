# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.result = None
        self.count = k

        def dfs(node):
            if not node or not self.count:
                return
            
            dfs(node.left)
            self.count -= 1
            if not self.count:
                self.result = node.val
            dfs(node.right)
        
        dfs(root)

        return self.result
                
        