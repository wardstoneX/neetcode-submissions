# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head is not None and head.next is None:
            return head

        first = None
        second = head
        while second is not None:

            tmp = second.next
            second.next = first
            first = second
            second = tmp
        
        return first