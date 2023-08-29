# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        averages = []
        queue = deque([root])
        
        while queue:
            levelcount = len(queue)
            levelsum = 0
            
            for i in range(levelcount):
                node = queue.popleft()
                levelsum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            averages.append(levelsum/levelcount)
            
        return averages