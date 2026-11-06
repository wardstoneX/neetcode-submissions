# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        node = result
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None and l2 is not None:
                val = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                node.next = ListNode(val)
                node = node.next
                l2 = l2.next
            elif l1 is not None and l2 is None:
                val = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                node.next = ListNode(val)
                node = node.next 
                l1 = l1.next

            else:
                val = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
                node.next = ListNode(val)
                node = node.next
                l1 = l1.next
                l2 = l2.next
        if carry != 0:
            node.next = ListNode(1)
        return result.next
        
        