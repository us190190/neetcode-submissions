# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        q = deque([root])

        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                status = self._isSameTree(node,subRoot)
                if status:
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
    
    def _isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return (p.val == q.val) and self._isSameTree(p.left, q.left) and self._isSameTree(p.right, q.right)
