# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k==0 or head.next == None :
            return head
        temp = head
        temp2 = head
        temp3 = head
        count = 0
        startnode = None
        
        
        while  temp!= None:
            count += 1
            temp = temp.next
            
        if 0 == k%count:
            return head
            
        for i in range(count - k%count):
            temp3 = temp2
            temp2 = temp2.next
            
        temp3.next = None    
        startnode = temp2
        
        while temp2.next != None:
            temp2 = temp2.next
        temp2.next = head
            
        
        
        return startnode
        
            
            