# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        temp = head
        temp2 = head
        breakingpoint = None
        
        count = 0
        while temp2 != None:
            count += 1
            temp2 = temp2.next
            
        for i in range(count//2):
            breakingpoint = temp
            temp = temp.next
        
        current = temp
        while temp != None:
            temp = temp.next
            current.next = prev
            prev = current
            current = temp
            
        breakingpoint.next = prev
            
        # after this the remaining part is to use two pointers
        
        left = head
        right = prev
        maxsum = 0
        
        for i in range(count//2):
            maxsum = max(left.val + right.val,maxsum)
            left = left.next
            right = right.next
            
        return maxsum
        
            
        
        
        
            
       
        
        
        