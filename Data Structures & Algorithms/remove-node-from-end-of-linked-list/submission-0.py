# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        new_head = ListNode(0, head)
        prev = new_head
        while n > 0:
            n -= 1
            curr = curr.next
        
        while curr:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        
        return new_head.next
        
