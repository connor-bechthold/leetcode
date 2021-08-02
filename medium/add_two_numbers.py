# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        carry = 0
        total = (p.val + q.val) % 10
        carry = (p.val + q.val) // 10
        head = ListNode(total)
        curr = head
        if p.next == None and q.next != None:
            p.next = ListNode(0)
        if p.next != None and q.next == None:
            q.next = ListNode(0)
        while p.next != None and q.next != None:
            p = p.next
            q = q.next
            total = (p.val + q.val + carry) % 10
            carry = (p.val + q.val + carry) // 10
            curr.next = ListNode(total)
            curr = curr.next
            if p.next == None and q.next != None:
                p.next = ListNode(0)
            if p.next != None and q.next == None:
                q.next = ListNode(0)
        if (carry > 0):
            curr.next = ListNode(carry)
        return head
