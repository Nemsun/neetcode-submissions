# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        curr_node = head

        while curr_node:
            if curr_node.val in visited:
                return True
            visited.append(curr_node.val)
            curr_node = curr_node.next
        
        return False