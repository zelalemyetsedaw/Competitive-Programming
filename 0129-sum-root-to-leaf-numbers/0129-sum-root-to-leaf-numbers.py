# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root,cursum,total):
            if root == None:
                return cursum,total
            if root.left == None and root.right == None:
                cursum += str(root.val)
                total += int(cursum)
                return cursum[:-1],total
            
            cursum += str(root.val)
            cursum,total = dfs(root.left,cursum,total)
            cursum,total = dfs(root.right,cursum,total)
            
            return cursum[:-1],total
        
        cur = ""
        cur,total = dfs(root,cur,0)
        
        return total
            
            
            