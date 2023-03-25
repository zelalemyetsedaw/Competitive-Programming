# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        for i in range(left-1):
            temp = temp.next
        
        templist = []
        temp2 = temp
        for i in range(right-left+1):
            templist.append(temp.val)
            temp = temp.next
        templist.reverse()  
        
        for i in range(right-left+1):
            temp2.val = templist[i]
            temp2 = temp2.next
            
        return head
            
            