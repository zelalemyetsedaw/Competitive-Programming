# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        result = head
        if head == None:
            return head
        valbefore = temp.val
        current = temp
        temp = temp.next
        while temp != None:
            if valbefore == temp.val:
                current.next = temp.next
                temp = current.next
            else:
                valbefore = temp.val
                current = temp
                temp = temp.next
        return result
        