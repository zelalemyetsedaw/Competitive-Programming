# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        dummynode =  ListNode(0,head)
        prev,cur = head,head.next
        
        while cur:
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
            else:
                
                temp = dummynode
                while temp.next.val < cur.val:
                    temp = temp.next
                    
                prev.next = cur.next  
                cur.next = temp.next   
                temp.next = cur
                
                
                
                cur = prev.next
                
        return dummynode.next