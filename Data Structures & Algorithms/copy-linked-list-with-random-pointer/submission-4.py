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

        if not head:
            return None

        clone: Dict[Node, Node] = {}
        itr = head

        while itr:
            clone[itr] = Node(itr.val)
            itr = itr.next
        
        itr = head
        while itr:
            if itr.next:
                clone[itr].next = clone[itr.next]
            if itr.random:
                clone[itr].random = clone[itr.random]
            itr = itr.next

        return clone[head]



        