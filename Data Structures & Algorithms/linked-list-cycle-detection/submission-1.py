# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        idx = 0
        curr_node = head
        while curr_node:
            if curr_node.val in visited:
                return True
            visited[idx] = curr_node.val
            idx += 1
            curr_node = curr_node.next
        
        return False