# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        temp = head
        count = 0
        while head != None:
            count += 1
            head = head.next
        for i in range(count//2):
            temp = temp.next
        
        return temp
        