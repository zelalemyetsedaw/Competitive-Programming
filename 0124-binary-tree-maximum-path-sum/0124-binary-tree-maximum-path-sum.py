# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        answer = [root.val]
        
        def dfs(root):
            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            leftmax = left if left>0 else 0
            rightmax = right if right > 0 else 0
            
            answer[0] = max(answer[0],root.val + leftmax + rightmax)
            
            return root.val + max(leftmax,rightmax)
        
        dfs(root)
        return answer[0]
        