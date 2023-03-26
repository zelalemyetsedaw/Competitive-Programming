# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        monotonicstack  = []
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
            
        answer = [0] * count
        
        for i in range(count):
            j = i-1
            if not monotonicstack:
                monotonicstack.append([head.val,i])
            elif head.val <= monotonicstack[-1][0]:
                    monotonicstack.append([head.val,i])
            else:
                while monotonicstack and monotonicstack[-1][0] < head.val:
                    answer[monotonicstack[-1][1]] = head.val
                    j -= 1
                    monotonicstack.pop()
                    
                monotonicstack.append([head.val,i])
            head = head.next
                
        return answer
                    
                    
                
                    