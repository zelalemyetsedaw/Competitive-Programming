# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        length1 = 0
        length2 = 0
        
        l11 = l1
        l12 = l2
        while l11:
            length1 += 1
            l11 = l11.next
            
        while l12:
            length2 += 1
            l12 = l12.next
        
        ans = None
        if length1 > length2:
            ans = l1
        else:
            ans = l2
            
        answer = ans
        prev = None
        summ = 0
        while l1 and l2:
            summ += l1.val + l2.val
            if summ <= 9:
                ans.val = summ
                summ = 0
            else:
                ans.val = summ%10
                summ = summ // 10
            prev = ans
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
            
        while ans:
            summ += ans.val
            if summ <= 9:
                ans.val = summ
                summ = 0
            else:
                ans.val = summ % 10
                summ = summ // 10
            prev = ans
            ans = ans.next
            
            
        if summ != 0:
            prev.next = ListNode(summ)
            
        return answer
                