# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lwa(root,p,q):
            if root == None:
                return
            elif root.val == p.val or root.val== q.val:
                return root
            
            elif p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
                return root
            elif p.val <root.val and q.val < root.val:
                return lwa(root.left,p,q)
            else:
                return lwa(root.right,p,q)
                
        return lwa(root,p,q)