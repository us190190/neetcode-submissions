# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        maxSoFar = root.val
        self.res = 0

        def dfs(node, msf):
            if not node:
                return
            
            if node.val>=msf:
                self.res += 1
            
            msf = max(msf, node.val)
            
            dfs(node.left, msf)
            dfs(node.right, msf)
        
        dfs(root, root.val)
        return self.res
            

            

        