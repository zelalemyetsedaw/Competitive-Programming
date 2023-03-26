# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        temp = ListNode()
        answer = temp
        
        count = 1
        prev = head.val
        head = head.next
        while head != None:
            if head.val == prev:
                count += 1
            else:
                if count == 1:
                    temp.next = ListNode(prev)
                    temp = temp.next
                prev = head.val
                count = 1
                    
            head = head.next
            
        if count == 1:
            temp.next = ListNode(prev)
            temp = temp.next
            
        
            
        return answer.next
            
            