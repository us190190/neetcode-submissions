# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        itr, prev = head, None

        while itr:
            tmp = itr
            itr = itr.next
            tmp.next = prev
            prev = tmp
        
        return prev
        