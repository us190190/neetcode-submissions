"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        q = deque([node]) # keep original nodes

        cloned_map = {} # keep cloned nodes only
        cloned_map[node.val] = Node(node.val)

        while q:
            n = q.popleft()
            for nbr in n.neighbors:
                if nbr.val not in cloned_map:
                    cloned_map[nbr.val] = Node(nbr.val)
                    q.append(nbr)
                cloned_map[n.val].neighbors.append(cloned_map[nbr.val])
        
        return cloned_map[node.val]

        