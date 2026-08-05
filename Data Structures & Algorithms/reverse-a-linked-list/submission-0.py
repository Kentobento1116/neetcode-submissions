# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        current = head
        next_node = head.next
        head.next = prev
        while next_node:
            prev = current
            current = next_node
            next_node = current.next
            current.next = prev
        return current