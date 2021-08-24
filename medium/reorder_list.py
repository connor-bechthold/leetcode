# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         
        """
        Do not return anything, modify head in-place instead.
        """
        
        deq = deque()
        trav = head.next
        while trav:
            deq.append(trav)
            trav = trav.next
        trav = head
        pop = True 
        while len(deq):
            if pop:
                trav.next = deq.pop()
                trav = trav.next
                trav.next = None
                pop = False
            else:
                trav.next = deq.popleft()
                trav = trav.next
                trav.next = None
                pop = True
