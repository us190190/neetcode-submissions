# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle of list
        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # [0, 1, 2, 3, 4, 5, 6]
        #.          S        F

        # reverse second half of list and return new head
        prev = None
        second_head = slow.next
        slow.next = None

        while second_head:
            nxt = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = nxt
        
        second_head = prev

        # read first element from L1 and second element from L2 untill finished
        final_lst = ListNode()
        itr_lst = final_lst

        while head and second_head:
            itr_lst.next = head
            head = head.next
            itr_lst = itr_lst.next
            itr_lst.next = second_head
            second_head = second_head.next
            itr_lst = itr_lst.next
        
        if head:
            itr_lst.next = head
        
        if second_head:
            itr_lst.next = second_head
        
        head = final_lst.next




        