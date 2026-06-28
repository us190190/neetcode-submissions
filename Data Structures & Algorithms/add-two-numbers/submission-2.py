# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head, itr, carry = None, None, 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + carry
            carry = 0 if s<10 else s//10
            s = s if s<10 else s%10
            tmp = ListNode(s)
            if head is None:
                head = tmp
                itr = tmp
            else:
                itr.next = tmp
                itr = itr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head

        