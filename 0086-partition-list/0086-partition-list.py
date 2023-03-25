# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        headLess = ListNode()
        headl = headLess
        headgreater = ListNode()
        headg = headgreater
        
        while head != None:
            if head.val < x:
                headLess.next = ListNode(head.val)
                headLess = headLess.next
            else:
                headgreater.next = ListNode(head.val)
                headgreater = headgreater.next
                
            head = head.next
                
        headLess.next = headg.next
        
        return headl.next
            