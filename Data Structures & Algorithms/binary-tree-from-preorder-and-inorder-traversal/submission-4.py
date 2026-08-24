# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        # Pre: 1,2,3,4
        # In:  2,1,3,4

        self.indices = {val:idx for idx,val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l, r):
            if l>r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            mid_idx = self.indices[root_val]
            node.left = dfs(l, mid_idx-1)
            node.right = dfs(mid_idx+1, r)
            return node
        
        return dfs(0, len(preorder)-1)


        


        