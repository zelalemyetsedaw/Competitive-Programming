# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        temp = None
        for item in lists:
            temp = item
            while item != None:
                heappush(heap,item.val)
                item = item.next
        
        answer = []
        for i in range(len(heap)):
            answer.append(heappop(heap))
        
        result = ListNode(0)
        final  = result
       
        for i in range(len(answer)):
            result.next = ListNode(answer[i])
            
            result = result.next
            
            
        return final.next
            
            
            