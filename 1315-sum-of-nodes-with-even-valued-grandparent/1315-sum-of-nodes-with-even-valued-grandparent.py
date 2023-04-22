# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(root,summ):
            if root == None:
                return summ
            
            if root.val % 2 == 0 :
                if root.left and root.left.left:
                    summ += root.left.left.val
                if root.left and root.left.right:
                    summ += root.left.right.val
                if root.right and root.right.left:
                    summ += root.right.left.val
                if root.right and root.right.right:
                    summ += root.right.right.val
                
                
            summ = dfs(root.left,summ)
            summ = dfs(root.right,summ)
            return summ
        
        return dfs(root,0)
                