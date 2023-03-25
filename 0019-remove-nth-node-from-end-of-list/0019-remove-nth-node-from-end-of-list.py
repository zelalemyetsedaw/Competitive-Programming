# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp  = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        if count == n:
            return head.next
        temp2 = None
        temp1 = head
        for i in range(count - n):
            temp2 = temp1
            temp1 = temp1.next
            
        
        temp2.next = temp1.next
        
        return head