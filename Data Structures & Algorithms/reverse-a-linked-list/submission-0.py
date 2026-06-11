# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head, curr = None, head

        while curr:
            temp_node = curr.next # save state of original
            curr.next = new_head # cut off original link
            new_head = curr # reassign new head to original minus curr node
            curr = temp_node 
        return new_head