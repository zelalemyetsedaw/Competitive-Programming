# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp2 = []
        prev = None
        temp = head
        current = head
        
        while temp != None:
            temp = temp.next
            current.next = prev
            temp2.append(current.val)
            prev = current
            current = temp
        
        
        
        for i in range(len(temp2)):
            if temp2[i] != prev.val:
                return False
            prev = prev.next
        
        return True
        