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

        self.count = 0

        def dfs(node, prev_max):
            if not node:
                return
            
            if node.val >= prev_max:
                self.count += 1
                prev_max = node.val
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
        
        dfs(root, root.val)

        return self.count



        