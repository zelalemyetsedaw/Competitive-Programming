# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root,root.val)]
        
        while stack:
            
            x,summ = stack.pop()
            if summ == targetSum and not x.left and not x.right:
                return True
            if x.right:
                stack.append((x.right,x.right.val + summ))
            if x.left:
                stack.append((x.left,x.left.val + summ))
        return False
            
        
        