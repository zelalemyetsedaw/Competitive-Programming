# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = [root.val/1]
      
        queue =deque([root])
            
        while queue:
            l = len(queue)
            node = queue.popleft()
            summ,count = 0,0
            for i in range(l):
                if node.left:
                    queue.append(node.left)
                    summ += node.left.val
                    count += 1
                if node.right:
                    queue.append(node.right)
                    summ += node.right.val
                    count += 1
                if i==(l-1) and count:
                    
                    averages.append(summ/count)
                elif queue:
                    node = queue.popleft()
                    
                    
                    
        
        return averages