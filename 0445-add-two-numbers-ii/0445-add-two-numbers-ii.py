# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2
        
        head = ListNode(0)
        if x == 0: return head
        while x:
            v, x = x%10, x//10
            head.next, head.next.next = ListNode(v), head.next
            
        return head.next