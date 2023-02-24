# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        answer = ListNode()
        result = answer
        while list1!=None and list2 != None:
            if list1.val > list2.val:
                temp = ListNode()
                temp.val = list2.val
                answer.next = temp
                answer = answer.next
                list2 = list2.next
            else:
                temp = ListNode()
                temp.val = list1.val
                answer.next = temp
                answer = answer.next
                list1 = list1.next
        while list1 != None:
            temp = ListNode()
            temp.val = list1.val
            answer.next = temp
            answer = answer.next
            list1 = list1.next
        while list2 != None:
            temp = ListNode()
            temp.val = list2.val
            answer.next = temp
            answer = answer.next
            list2 = list2.next
            
        return result.next
            
                
        