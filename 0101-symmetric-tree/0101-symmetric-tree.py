# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def symmetric(left,right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            
            if left.val == right.val:
                return symmetric(left.left,right.right) and symmetric(left.right,right.left)
            else:
                return False
        
        return symmetric(root.left,root.right)