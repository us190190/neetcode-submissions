"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        ref_map = {}
        itr, new_head = head, None

        while itr:
            copied_node = Node(itr.val, None, None)
            ref_map[itr] = copied_node
            itr = itr.next
            if new_head is None:
                new_head = copied_node
        
        for old_node, new_node in ref_map.items():
            new_node.next = ref_map[old_node.next] if old_node.next else None
            new_node.random = ref_map[old_node.random] if old_node.random else None
        
        return new_head

        

        