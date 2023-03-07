# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def maxdepth(root):
            if root == None:
                return 0
            left = 1 + maxdepth(root.left)
            right = 1 + maxdepth(root.right)
            
            return max(left,right)
        
        return maxdepth(root)