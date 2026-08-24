# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        enc_data = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                enc_data.append('X')
            else:
                enc_data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return "#".join(enc_data)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        dec_data = data.split("#")

        if not len(dec_data):
            return None
        
        idx = 0
        root_val = dec_data[idx]
        if root_val == "X":
            return None

        root = TreeNode(int(root_val))
        q = deque([root])

        while q:
            node = q.popleft()
            idx += 1
            left = dec_data[idx]
            if left != "X":
                node.left = TreeNode(int(left))
                q.append(node.left)
            idx += 1
            right = dec_data[idx]
            if right != "X":
                node.right = TreeNode(int(right))
                q.append(node.right)
        
        return root

