# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # basically if either list is empty return the non-empty list
        if not list1: return list2
        if not list2: return list1

        trav_node = ListNode()
        head = trav_node

        while list1 and list2:
            if list1.val < list2.val:
                trav_node.next = list1
                list1 = list1.next
            else:
                trav_node.next = list2
                list2 = list2.next
            trav_node = trav_node.next

            trav_node.next = list1 or list2
        return head.next

