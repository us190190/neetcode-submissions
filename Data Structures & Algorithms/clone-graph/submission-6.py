"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        ref = {}

        def dfs(n):
            if not n:
                return None
            
            if n.val not in ref:
                ref[n.val] = Node(n.val)
                for nbr in n.neighbors:
                    ref[n.val].neighbors.append(dfs(nbr))
            
            return ref[n.val]
        
        dfs(node)

        return ref[node.val] if node else None

        