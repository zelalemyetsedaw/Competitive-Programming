# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        temp = head
        current = head
        
        while temp != None:
            temp = temp.next
            current.next = prev
            prev = current
            current = temp
        
        return prev
        