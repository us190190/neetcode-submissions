# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class CustomListNode:

    def __init__(self, node:ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        root = ListNode()
        itr = root

        for lst in lists:
            if lst:
                heapq.heappush(min_heap, CustomListNode(lst))

        while min_heap:
            lst_head = heapq.heappop(min_heap)
            node = lst_head.node

            prev = itr
            itr = node
            node = node.next
            if node:
                heapq.heappush(min_heap, CustomListNode(node))
            prev.next = itr
        
        return root.next





        