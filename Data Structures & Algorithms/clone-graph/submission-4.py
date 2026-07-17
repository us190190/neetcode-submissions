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
        
        ref = {}

        def cloneNode(n):
            if not n:
                return None
            
            if n.val not in ref:
                ref[n.val] = Node(val=n.val)
                for nbr in n.neighbors:
                    ref[n.val].neighbors.append(cloneNode(nbr))
            
            return ref[n.val]
        
        cloneNode(node)
        
        return ref[node.val]



        