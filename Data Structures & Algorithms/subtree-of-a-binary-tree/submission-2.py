# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = deque()
        q.append(root)

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        res = None
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
        

        