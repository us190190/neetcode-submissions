# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        enc = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                enc.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                enc.append('N')
        
        return ','.join(enc)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dec_tree = data.split(',')
        idx = 0

        if dec_tree[idx]=='N':
            return None

        tree = TreeNode(int(dec_tree[idx]))
        q = deque()
        q.append(tree)

        while q:
            node = q.popleft()
            idx += 1
            if dec_tree[idx]!='N':
                node.left = TreeNode(int(dec_tree[idx]))
                q.append(node.left)
            idx += 1
            if dec_tree[idx]!='N':
                node.right = TreeNode(int(dec_tree[idx]))
                q.append(node.right)
        
        return tree


