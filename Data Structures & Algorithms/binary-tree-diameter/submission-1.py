# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0
        
        def edges(node):
            if not node:
                return 0
            
            left = (1+edges(node.left)) if node.left else 0
            right = (1+edges(node.right)) if node.right else 0
            curr_diameter = left + right
            self.diameter = max(self.diameter, curr_diameter)

            return max(left, right)
        
        edges(root)

        return self.diameter
        