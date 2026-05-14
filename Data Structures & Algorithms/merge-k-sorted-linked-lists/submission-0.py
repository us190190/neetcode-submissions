# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class CustomNode:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other: ListNode):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap, head = [], ListNode(0)
        itr = head

        for lst in lists:
            heapq.heappush(min_heap, CustomNode(lst))
        
        while min_heap:
            min_custom_node = heapq.heappop(min_heap)
            itr.next = min_custom_node.node
            min_custom_node.node = min_custom_node.node.next
            if min_custom_node.node:
                heapq.heappush(min_heap, CustomNode(min_custom_node.node))
            itr = itr.next
        
        return head.next

        