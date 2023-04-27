# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
      
        queue =deque([root])
            
        while queue:
            l = len(queue)
            
            summ,count = 0,0
            for i in range(l):
                node = queue.popleft()
                summ += node.val
                if node.left:
                    queue.append(node.left)
                    
                    
                if node.right:
                    queue.append(node.right)
                    
            
            averages.append(summ/l)
               
                    
                    
        return averages