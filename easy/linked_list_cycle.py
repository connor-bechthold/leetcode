# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = head
        slow = head
        while (slow.next and fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
