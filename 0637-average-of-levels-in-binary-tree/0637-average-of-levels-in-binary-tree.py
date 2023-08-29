# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        averages = []
        queue = [root]
        
        while queue:
            summ = 0
            count = 0
            nextlevel = []
            
            for node in queue:
                summ += node.val
                count += 1
                
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            averages.append(summ/count)
            queue = nextlevel
            
        return averages