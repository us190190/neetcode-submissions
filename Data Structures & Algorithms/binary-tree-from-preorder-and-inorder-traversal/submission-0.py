# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # preorder: [1,2,3,4]

        # inorder: [2,1,3,4]

        if not len(preorder):
            return None
        
        node = TreeNode(preorder[0])

        left_len = 0
        for i in range(len(inorder)):
            if inorder[i]==node.val:
                left_len = i
                break
        node.left = self.buildTree(preorder[1:1+left_len], inorder[:left_len])
        node.right = self.buildTree(preorder[left_len+1:], inorder[left_len+1:])

        return node
        