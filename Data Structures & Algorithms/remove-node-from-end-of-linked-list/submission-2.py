# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        result = ListNode()
        result.next = head

        fast = result
        while n:
            fast = fast.next
            n -= 1
        
        slow = result
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        if slow and slow.next:
            slow.next = slow.next.next
        
        return result.next
        
        