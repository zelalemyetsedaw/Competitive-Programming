# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        
        def dfs(root,answer):
            if root == None:
                return ""
            answer = str(root.val)
            if root.left:
                answer += "(" + dfs(root.left,answer) + ")"
            elif root.right:
                answer += "()"
            if root.right: 
                answer += "(" + dfs(root.right,answer) + ")"
            
            
            return answer
        
          
        return dfs(root,"")
        
        
            
        