# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def _get_kth(cur, count):
            while cur:
                count -= 1
                if count == 0:
                    return cur
                cur = cur.next
            return None
        
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            kth = _get_kth(group_prev.next, k)
            if kth is None:
                return dummy.next
            
            prev, group_next, cur = kth.next, kth.next, group_prev.next
            while cur!=group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        
        return dummy.next


        

        
        