# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        answer = set([False])
        def dfs(root,summ,flag):
            if root == None:
                return summ
            
            summ += root.val
            if root.left == None and root.right == None and summ == targetSum:
                answer.add(True)
            
            
            
            
            summ= dfs(root.left,summ,flag)
            
            summ = dfs(root.right,summ,flag)
            summ -= root.val
            
            return summ
        
        
        summ = 0
        dfs(root,summ,False)
        
        return True in answer