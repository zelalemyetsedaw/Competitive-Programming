# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        odd = oddhead = head
        even = evenhead = head.next
        
        temp = head.next.next
        
        while odd.next and even.next and temp.next and temp:
            odd.next = temp
            odd = odd.next
            even.next = temp.next
            even = even.next
            temp = temp.next.next
            
        
        if temp:
            even.next = None
            odd.next = temp
            odd.next.next = evenhead
            
        else:
            odd.next = evenhead
        
        
        
            
        return oddhead
        
            
        
            
        
            