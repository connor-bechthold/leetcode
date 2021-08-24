# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fast = ListNode(-1)
        slow = ListNode(-1)
        fast.next = head
        slow.next = head
        for i in range(n+1):
            fast = fast.next
        if not fast:
            head = head.next
            return head
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
