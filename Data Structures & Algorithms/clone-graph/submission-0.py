"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        ref = defaultdict(Node)

        def dfs(start):
            if start in ref:
                return ref[start]

            cloned_node = Node(start.val)
            ref[start] = cloned_node
            for neighbor in start.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            return ref[start]
        
        return dfs(node) if node else None
        