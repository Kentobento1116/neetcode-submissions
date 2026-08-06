# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        visited = []
        node = head
        while head:
            if node not in visited:
                visited.append(node)
            else:
                return True
            if node.next:
                node = node.next
            else:
                return False
