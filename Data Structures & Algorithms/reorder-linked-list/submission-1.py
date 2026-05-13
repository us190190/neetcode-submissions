# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        itr, second, end_of_head = head, head, None

        # find mid of the linked list using fast and slow pointers
        while itr and itr.next:
            itr = itr.next.next
            second = second.next
        
        if second == head:
            second = None
            
        end_of_first = second
        print(second)
        
        # reverse the second half of linked list
        reverse_second = None

        while second:
            tmp = second.next
            second.next = reverse_second
            reverse_second = second
            second = tmp
        
        second = reverse_second

        # construct reordered linked list
        first, final = head, None
        while first and second:
            if final is None:
                final = first
            else:
                final.next = first
                final = final.next
            first = first.next
            final.next = second
            final = final.next
            second = second.next

            first = first if first != end_of_first else None
        