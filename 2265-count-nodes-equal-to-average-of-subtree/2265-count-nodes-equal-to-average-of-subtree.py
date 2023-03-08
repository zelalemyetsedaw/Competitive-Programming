# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        length = 0
        summation = 0
        
        def sum(root,length):
            if root == None:
                return 0,0,length
            leftsum,leftcount,length = sum(root.left,length)
            rightsum,rightcount,length = sum(root.right,length)
            
            summation = root.val + leftsum + rightsum
            
            count = 1 + leftcount + rightcount
            
            if summation//count == root.val:
                length += 1
                
           
            return summation,count,length
        
        summaion,count,length = sum(root,length)
        
        return length
            
            