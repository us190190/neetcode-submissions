# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum_lst = ListNode()
        itr = sum_lst
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + carry
            carry = s//10
            s = s%10
            itr.next = ListNode(s)
            itr = itr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return sum_lst.next
        


        