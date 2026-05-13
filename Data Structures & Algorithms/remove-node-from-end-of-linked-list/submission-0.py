# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev, slow, fast = None, head, head

        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        if prev is None:
            head = slow.next
        else:
            prev.next = slow.next
        del slow
        return head
        

        