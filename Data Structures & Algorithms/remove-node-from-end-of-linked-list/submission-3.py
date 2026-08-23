# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast, slow = head, head
        while n:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        itr = head
        prev = None

        while itr:
            if itr.next == slow:
                prev = itr
                break
            itr = itr.next
        
        # [1,2,3,4]

        if prev:
            tmp = prev.next
            prev.next = tmp.next
            del tmp
            return head
        else:
            nxt = head.next
            del head
            return nxt


        

        

        